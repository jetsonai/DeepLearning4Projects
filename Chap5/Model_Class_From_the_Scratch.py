import torch
import torch.nn as nn
import torch.nn.functional as F

class PyTorch_Custom_Model_Class(nn.Module):
    def __init__(self):
        super().__init__()
        pass
    
    def forward(self, x):
        return x

class MODEL_From_Scratch(nn.Module):
    def __init__(self, num_classes):
        super().__init__()
        self.classifier = nn.Sequential(
            nn.Conv2d(3, 32, kernel_size = 3, stride = 2, padding = 1)
            , nn.BatchNorm2d(32)
            , nn.ReLU()
            , nn.Conv2d(32, 64, kernel_size = 3, stride = 2, padding = 1)
            , nn.BatchNorm2d(64)
            , nn.ReLU()
            , nn.Conv2d(64, 128, kernel_size = 3, stride = 2, padding = 1)
            , nn.BatchNorm2d(128)
            , nn.ReLU()
            , nn.AdaptiveAvgPool2d(1)
            , nn.Flatten()
            , nn.Linear(128, 512)
            , nn.ReLU()
            , nn.Dropout()
            , nn.Linear(512, 64)
            , nn.ReLU()
            , nn.Dropout()
            , nn.Linear(64, num_classes)
            , nn.Softmax(dim=-1)
        )
    def forward(self, x):
        return self.classifier(x)