import torch
from torchvision import models
import torch.nn as nn
import torch.nn.functional as F

class MobileNet(nn.Module):
    def __init__(self, num_classes, pretrained=True):
        super().__init__()
        self.network = models.mobilenet_v2(pretrained=pretrained)
        num_ftrs = self.network.classifier[1].in_features 
        self.network.classifier[1] = nn.Linear(num_ftrs, num_classes)
        self.classifier = nn.Sequential(nn.Softmax(dim=-1)) 

    def forward(self, x):
        x = self.network(x)  
        x = self.classifier(x) 
        return x