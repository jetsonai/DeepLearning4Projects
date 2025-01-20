########## Import Library ##########
from os import makedirs

import numpy as np
import matplotlib.pyplot as plt

import torch
from torch.utils.data import DataLoader
from torchvision import datasets, transforms

from torchmetrics import Accuracy
from torchsummary import summary
from tqdm import tqdm

from vgg import VGG16, VGG16withBN
from utils import AverageMeter


########## Inference Code ##########
def main(img_channels=1, width=16, img_size=32, num_classes=10, p=0.25, batch_size=64) :
    # Load Dataset
    transform = transforms.Compose([transforms.Resize((img_size, img_size)), 
                                    transforms.ToTensor()])
    
    # Download Fashion MNIST Dataset
    test_dataset = datasets.FashionMNIST("data/", train=False, transform=transform, download=True)
    
    # Create DataLoader
    test_loader = DataLoader(test_dataset, batch_size=batch_size, shuffle=False, num_workers=4)
    
    # Check Device
    device = "cuda" if torch.cuda.is_available() else "cpu"
    print(f"Current Device : {device}")

    # Create Model Instance
    model_vgg16 = VGG16(img_channels, width, num_classes).to(device)
    model_vgg16_bn = VGG16withBN(img_channels, width, num_classes, p).to(device)
    
    # Load Pretraind Weight
    model_vgg16.load_state_dict(torch.load("ckpt/vgg16/best.pth"), strict=True)
    model_vgg16_bn.load_state_dict(torch.load("ckpt/vgg16_bn/best.pth"), strict=True)
    
    # Summarize Model
    summary(model_vgg16, (img_channels, img_size, img_size))
    summary(model_vgg16_bn, (img_channels, img_size, img_size))
    
    # Create Metric Instance
    metric = Accuracy("multiclass", num_classes=num_classes).to(device)
    
    # Create AverageMeter Instance
    test_acc_vgg16, test_acc_vgg16_bn = AverageMeter(), AverageMeter()
    
    # Create Directory
    graph_dir = f"result/test/"
    makedirs(graph_dir, exist_ok=True)
        
    # Create TQDM Bar Instance
    test_bar = tqdm(test_loader)
    
    # Evaluate Model
    with torch.no_grad() :
        # Set Test Mode
        model_vgg16.eval(), model_vgg16_bn.eval()
        
        for data in test_bar :
            img, label = data
            img, label = img.to(device), label.to(device)
            
            # Inference
            pred_vgg16, pred_vgg16_bn = model_vgg16(img), model_vgg16_bn(img)
            
            # Compute Metric
            acc_vgg16, acc_vgg16_bn = metric(pred_vgg16, label), metric(pred_vgg16_bn, label)
            
            # Update AverageMeter
            test_acc_vgg16.update(acc_vgg16.cpu().item()), test_acc_vgg16_bn.update(acc_vgg16_bn.cpu().item())

            # Show Test Status
            test_bar.set_description(desc=f"[Test] < VGG16:{test_acc_vgg16.avg:.4f} | VGG16-BN:{test_acc_vgg16_bn.avg:.4f} >")

    # Plot Accuracy Bar Chart
    plt.clf()
    plt.bar(np.arange(2), [test_acc_vgg16.avg, test_acc_vgg16_bn.avg])
    plt.xticks(np.arange(2), ["VGG16", "VGG16-BN"])
    plt.title("Accuracy Comparison")
    plt.ylabel("Accuracy")
    plt.savefig(f"{graph_dir}/accuracy.png")


########## Execute Code ##########
if __name__ == "__main__" :
    main()