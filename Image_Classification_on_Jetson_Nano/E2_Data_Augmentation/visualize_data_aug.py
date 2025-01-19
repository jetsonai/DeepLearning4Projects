########## Import Library ##########
import random
from os import makedirs

from PIL import ImageFilter

import numpy as np
import matplotlib.pyplot as plt

from torch.utils.data import DataLoader
from torchvision import datasets, transforms



class GaussianBlur(object):
    def __init__(self, p):
        self.p = p

    def __call__(self, img):
        if random.random() < self.p:
            sigma = random.random()*1.9 + 0.1
            return img.filter(ImageFilter.GaussianBlur(sigma))
        else:
            return img


########## Training Code ##########
def main() :
    # Load Dataset
    transform_original = transforms.Compose([transforms.Resize(256), 
                                             transforms.ToTensor()])
    transform_data_aug = transforms.Compose([transforms.Resize(256),
                                             transforms.RandomHorizontalFlip(0.5),
                                             transforms.RandomApply([
                                                 transforms.ColorJitter(brightness=0.4, contrast=0.4, 
                                                                        saturation=0.2, hue=0.1)], p=0.8),
                                             transforms.ToTensor()])
    
    # Download Fashion MNIST Dataset
    dataset_original = datasets.CIFAR10("data/", train=True, transform=transform_original, download=True)
    dataset_data_aug = datasets.CIFAR10("data/", train=True, transform=transform_data_aug, download=True)
    
    # Create DataLoader
    loader_original = DataLoader(dataset_original, batch_size=10, shuffle=False)
    loader_data_aug = DataLoader(dataset_data_aug, batch_size=10, shuffle=False)
    
    # Create Directory
    save_dir = "imgs/data_aug"
    makedirs(save_dir, exist_ok=True)
    
    # Load Dataset
    for data_org, data_aug in zip(loader_original, loader_data_aug) :
        # Load Image
        img_org, img_aug = data_org[0], data_aug[0]
        
        # Convert PyTorch Tensor to Numpy Array
        img_org = img_org.permute(0,2,3,1).cpu().numpy()
        img_aug = img_aug.permute(0,2,3,1).cpu().numpy()
        
        # Stack Results
        img_org = np.hstack(img_org)
        img_aug = np.hstack(img_aug)
        
        # Stack Results
        img_concat = np.vstack([img_org, img_aug])
        
        # Save Results
        plt.imsave(f"{save_dir}/data_augmentation.png", img_concat)
        
        break


########## Execute Code ##########
if __name__ == "__main__" :
    main()