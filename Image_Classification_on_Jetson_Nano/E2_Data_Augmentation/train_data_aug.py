########## Import Library ##########
from os import makedirs

import numpy as np
import matplotlib.pyplot as plt

import torch
from torch import nn
from torch import optim
from torch.utils.data import DataLoader
from torchvision import datasets, transforms

from torchmetrics import Accuracy
from torchsummary import summary
from tqdm import tqdm

from vgg import VGG16withBN
from utils import fix_seed, AverageMeter


########## Training Code ##########
def main(img_channels=3, width=16, img_size=32, num_classes=10, p=0.25,
         lr=1e-2, total_epochs=10, seed=42, batch_size=64) :
    # Load Dataset
    train_transform = transforms.Compose([transforms.Resize((img_size, img_size)), 
                                          transforms.RandomHorizontalFlip(0.5),
                                          transforms.RandomApply([
                                              transforms.ColorJitter(brightness=0.4, contrast=0.4, 
                                                                     saturation=0.2, hue=0.1)], p=0.8),
                                          transforms.ToTensor()])
    test_transform = transforms.Compose([transforms.Resize((img_size, img_size)), 
                                         transforms.ToTensor()])
    
    # Download CIFAR-10 Dataset
    train_dataset = datasets.CIFAR10("data/", train=True, transform=train_transform, download=True)
    test_dataset = datasets.CIFAR10("data/", train=False, transform=test_transform, download=True)

    # Fix Seed
    fix_seed(seed)
    
    # Create DataLoader
    train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True, num_workers=4, drop_last=True)
    test_loader = DataLoader(test_dataset, batch_size=batch_size, shuffle=False, num_workers=4)
    
    # Check Device
    device = "cuda" if torch.cuda.is_available() else "cpu"
    print(f"Current Device : {device}")

    # Fix Seed
    fix_seed(seed)
    
    # Create Model Instance
    model = VGG16withBN(img_channels, width, num_classes, p).to(device)
    
    # Summarize Model
    summary(model, (img_channels, img_size, img_size))
    
    # Create Optimizer Instance
    optimizer = optim.SGD(model.parameters(), lr=lr)
    
    # Create Loss Instance
    criterion = nn.CrossEntropyLoss()
    
    # Create Metric Instance
    metric = Accuracy("multiclass", num_classes=num_classes).to(device)
    
    # Create AverageMeter Instance
    train_loss, train_acc = AverageMeter(), AverageMeter()
    test_loss, test_acc = AverageMeter(), AverageMeter()
    
    # Create List Instance
    train_loss_list, train_acc_list = [], []
    test_loss_list, test_acc_list = [], []
    
    # Create Directory
    ckpt_dir, graph_dir = "ckpt/data_aug", "result/data_aug"
    makedirs(ckpt_dir, exist_ok=True), makedirs(graph_dir, exist_ok=True)
    
    # Set Best Accuracy
    best_acc = 0
    
    # Start Training
    for epoch in range(total_epochs) :
        # Create TQDM Bar Instance
        train_bar = tqdm(train_loader)
        
        # Reset AverageMeter
        train_loss.reset(), train_acc.reset()
        
        # Set Training Mode
        model.train()
        
        # Training Phase
        for data in train_bar :
            img, label = data
            img, label = img.to(device), label.to(device)
            
            # Update Classifier Weights
            optimizer.zero_grad()
            pred = model(img)
            loss = criterion(pred, label)
            loss.backward()
            optimizer.step()
            
            # Compute Metric
            acc = metric(pred, label)
            
            # Update AverageMeter
            train_loss.update(loss.cpu().item()), train_acc.update(acc.cpu().item())

            # Show Training Status
            train_bar.set_description(desc=f"[Train] [{epoch+1}/{total_epochs}] < Loss:{train_loss.avg:.4f} | Acc.:{train_acc.avg:.4f} >")
        
        # Add Training Loss and Accuracy
        train_loss_list.append(train_loss.avg), train_acc_list.append(train_acc.avg) 
        
        # Create TQDM Bar Instance
        test_bar = tqdm(test_loader)
        
        # Reset AverageMeter
        test_loss.reset(), test_acc.reset()
        
        # Evaluate Model
        with torch.no_grad() :
            # Set Test Mode
            model.eval()
            
            for data in test_bar :
                img, label = data
                img, label = img.to(device), label.to(device)
                
                # Update Classifier Weights
                pred = model(img)
                loss = criterion(pred, label)
                
                # Compute Metric
                acc = metric(pred, label)
                
                # Update AverageMeter
                test_loss.update(loss.cpu().item()), test_acc.update(acc.cpu().item())

                # Show Training Status
                test_bar.set_description(desc=f"[Test] [{epoch+1}/{total_epochs}] < Loss:{test_loss.avg:.4f} | Acc.:{test_acc.avg:.4f} >")

        # Add Test Loss and Accuracy
        test_loss_list.append(test_loss.avg), test_acc_list.append(test_acc.avg)
        
        # Save Network
        if test_acc.avg > best_acc :
            best_acc = test_acc.avg
            torch.save(model.state_dict(), f"{ckpt_dir}/best.pth")
        torch.save(model.state_dict(), f"{ckpt_dir}/latest.pth")
        
        # Plot Training vs. Test Loss Graph
        plt.clf()
        plt.plot(np.arange(epoch+1), train_loss_list, label="Training Loss")
        plt.plot(np.arange(epoch+1), test_loss_list, label="Test Loss")
        plt.title("Loss (Training vs. Test)")
        plt.xlabel("Epoch"), plt.ylabel("Loss")
        plt.legend(loc="best")
        plt.savefig(f"{graph_dir}/loss.png")
        
        # Plot Training vs. Test Accuracy Graph
        plt.clf()
        plt.plot(np.arange(epoch+1), train_acc_list, label="Training Accuracy")
        plt.plot(np.arange(epoch+1), test_acc_list, label="Test Accuracy")
        plt.title("Accuracy (Training vs. Test)")
        plt.xlabel("Epoch"), plt.ylabel("Accuracy")
        plt.legend(loc="best")
        plt.savefig(f"{graph_dir}/accuracy.png")


########## Execute Code ##########
if __name__ == "__main__" :
    main()