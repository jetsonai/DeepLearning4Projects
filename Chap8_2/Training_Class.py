import os
import torch
import torch.optim as optim
import torchvision.transforms as transforms
import torch.nn.functional as F
from tqdm import tqdm

from .Model_Class_From_the_Scratch import MODEL_From_Scratch
from .Model_Class_Transfer_Learning_MobileNet import MobileNet
from .Dataset_Class import PyTorch_Classification_Dataset_Class as Dataset

class PyTorch_Classification_Training_Class():
    def __init__(self
                , dataset_dir = "/content/Recycle_Classification_Dataset"
                , batch_size = 16
                , train_ratio = 0.75
                ):
        if not os.path.isdir(dataset_dir):
            os.system("git clone https://github.com/JinFree/Recycle_Classification_Dataset.git")
            os.system("rm -rf ./Recycle_Classification_Dataset/.git")
            dataset_dir = os.path.join(os.getcwd(), 'Recycle_Classification_Dataset')        
        self.USE_CUDA = torch.cuda.is_available()
        self.DEVICE = torch.device("cuda" if self.USE_CUDA else "cpu")
        self.transform = transforms.Compose([
                transforms.Resize(256)
                , transforms.RandomCrop(224)
                , transforms.ToTensor()
                , transforms.Normalize(mean=[0.485, 0.456, 0.406],
                        std=[0.229, 0.224, 0.225]) 
                ])
        dataset = Dataset(dataset_dir = dataset_dir, transform = self.transform)
        dataset.__save_label_map__()
        self.num_classes = dataset.__num_classes__()
        train_size = int(train_ratio * len(dataset))
        test_size = len(dataset) - train_size
        train_dataset, test_dataset = torch.utils.data.random_split(dataset, [train_size, test_size])
        self.train_loader = torch.utils.data.DataLoader(
            train_dataset
            , batch_size=batch_size
            , shuffle=True
        )
        self.test_loader = torch.utils.data.DataLoader(
            test_dataset
            , batch_size=batch_size
            , shuffle=False
        )
        self.model = None
        self.model_str = None
        
    def prepare_network(self
            , is_scratch = True):
        if is_scratch:
            self.model = MODEL_From_Scratch(self.num_classes)
            self.model_str = "PyTorch_Training_From_Scratch"
        else:
            self.model = MobileNet(self.num_classes)
            self.model_str = "PyTorch_Transfer_Learning_MobileNet"
        self.model.to(self.DEVICE)
        self.model_str += ".pt" 
    
    def training_network(self
            , learning_rate = 0.0001
            , epochs = 10
            , step_size = 3
            , gamma = 0.3):
        if self.model is None:
            self.prepare_network(False)
        optimizer = optim.Adam(self.model.parameters(), lr=learning_rate)
        scheduler = optim.lr_scheduler.StepLR(optimizer, step_size=step_size, gamma=gamma)
        acc = 0.0
        for epoch in range(1, epochs + 1):
            self.model.train()
            for data, target in tqdm(self.train_loader):
                data, target = data.to(self.DEVICE), target.to(self.DEVICE)
                optimizer.zero_grad()
                output = self.model(data)
                loss = F.cross_entropy(output, target)
                loss.backward()
                optimizer.step()
            scheduler.step()
            self.model.eval()
            test_loss = 0
            correct = 0
            with torch.no_grad():
                for data, target in tqdm(self.test_loader):
                    data, target = data.to(self.DEVICE), target.to(self.DEVICE)
                    output = self.model(data)
                    test_loss += F.cross_entropy(output, target, reduction='sum').item()
                    pred = output.max(1, keepdim=True)[1]
                    correct += pred.eq(target.view_as(pred)).sum().item()
            test_loss /= len(self.test_loader.dataset)
            test_accuracy = 100. * correct / len(self.test_loader.dataset)
            print('[{}] Test Loss: {:.4f}, Accuracy: {:.2f}%'.format(epoch, test_loss, test_accuracy))
            if acc < test_accuracy or epoch == epochs:
                acc = test_accuracy
                torch.save(self.model.state_dict(), self.model_str)
                print("model saved!")
        
if __name__ == "__main__":
    training_class = PyTorch_Classification_Training_Class()
    training_class.prepare_network(True)
    training_class.training_network()
