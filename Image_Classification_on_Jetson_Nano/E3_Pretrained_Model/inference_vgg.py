########## Import Library ##########
import torch
from torch.utils.data import DataLoader
from torchvision import transforms
from torchvision.models import vgg16_bn

from torchsummary import summary
from tqdm import tqdm

from dataloader import PyTorchCustomDataset


########## Inference Code ##########
def main(src="cats_and_dogs_filtered/validation", img_size=224, img_channels=3) :
    # Load Dataset
    transform = transforms.Compose([transforms.Resize((img_size, img_size)),
                                    transforms.ToTensor(),
                                    transforms.Normalize(mean=[0.485, 0.456, 0.406],
                                                         std=[0.229, 0.224, 0.225])])
    
    # Create Custom Dataset Instance
    test_dataset = PyTorchCustomDataset(src, transform)
    
    # Create DataLoader
    test_loader = DataLoader(test_dataset, batch_size=1, shuffle=False)
    
    # Check Device
    device = "cuda" if torch.cuda.is_available() else "cpu"
    print(f"Current Device : {device}")
    
    # Create Model Instance
    model = vgg16_bn(pretrained=True).eval().to(device)
    
    # Summarize Model
    summary(model, (img_channels, img_size, img_size))
    
    # Create List Instance
    cat_label_dict, dog_label_dict = {}, {}
    
    # Inference
    with torch.no_grad() :
        # Create TQDM Bar Instance
        test_bar = tqdm(test_loader)
    
        for data in test_bar :
            img, label = data
            img = img.to(device)
            pred = model(img)
            pred = torch.argmax(pred, dim=-1).cpu().item()
            
            if label == 0 : # 0 for Cat / 1 for Dog
                if pred not in cat_label_dict.keys() :
                    cat_label_dict[pred] = 1
                else :
                    cat_label_dict[pred] += 1
            else :
                if pred not in dog_label_dict.keys() :
                    dog_label_dict[pred] = 1
                else :
                    dog_label_dict[pred] += 1
            
            # Show Inference Status
            test_bar.set_description(desc=f"[Inference]")
        
    # Sort by Keys
    cat_label_dict_sorted = sorted(cat_label_dict.items(), key=lambda x:x[1], reverse=True)
    dog_label_dict_sorted = sorted(dog_label_dict.items(), key=lambda x:x[1], reverse=True)
    print(f"Cat Predictions : {cat_label_dict_sorted}")
    print(f"Dog Predictions : {dog_label_dict_sorted}")


########## Execute Code ##########
if __name__ == "__main__" :
    main()