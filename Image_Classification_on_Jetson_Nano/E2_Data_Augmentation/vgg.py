########## Import Library ##########
import torch
from torch import nn
import torch.nn.functional as F

from torchsummary import summary


########## Conv-ReLU-Block Implementation ##########
class ConvBlock(nn.Module) :
    def __init__(self, in_channels, out_channels, num_layers) :
        super().__init__()
        # Create Convolutional Layer Instance
        
        if num_layers == 2 :
            self.conv_block = nn.Sequential(nn.Conv2d(in_channels, out_channels, kernel_size=3, stride=1, padding=1),
                                            nn.ReLU(inplace=True),
                                            nn.Conv2d(out_channels, out_channels, kernel_size=3, stride=1, padding=1),
                                            nn.ReLU(inplace=True))
        elif num_layers == 3 :
            self.conv_block = nn.Sequential(nn.Conv2d(in_channels, out_channels, kernel_size=3, stride=1, padding=1),
                                            nn.ReLU(inplace=True),
                                            nn.Conv2d(out_channels, out_channels, kernel_size=3, stride=1, padding=1),
                                            nn.ReLU(inplace=True),
                                            nn.Conv2d(out_channels, out_channels, kernel_size=3, stride=1, padding=1),
                                            nn.ReLU(inplace=True))
    
    def forward(self, x) :
        return self.conv_block(x)


########## Conv-BN-ReLU-Block Implementation ##########
class ConvBlockwithBN(nn.Module) :
    def __init__(self, in_channels, out_channels, num_layers) :
        super().__init__()
        # Create Convolutional Layer Instance
        
        if num_layers == 2 :
            self.conv_block = nn.Sequential(nn.Conv2d(in_channels, out_channels, kernel_size=3, stride=1, padding=1, bias=False),
                                            nn.BatchNorm2d(out_channels),
                                            nn.ReLU(inplace=True),
                                            nn.Conv2d(out_channels, out_channels, kernel_size=3, stride=1, padding=1, bias=False),
                                            nn.BatchNorm2d(out_channels),
                                            nn.ReLU(inplace=True))
        elif num_layers == 3 :
            self.conv_block = nn.Sequential(nn.Conv2d(in_channels, out_channels, kernel_size=3, stride=1, padding=1, bias=False),
                                            nn.BatchNorm2d(out_channels),
                                            nn.ReLU(inplace=True),
                                            nn.Conv2d(out_channels, out_channels, kernel_size=3, stride=1, padding=1, bias=False),
                                            nn.BatchNorm2d(out_channels),
                                            nn.ReLU(inplace=True),
                                            nn.Conv2d(out_channels, out_channels, kernel_size=3, stride=1, padding=1, bias=False),
                                            nn.BatchNorm2d(out_channels),
                                            nn.ReLU(inplace=True))
    
    def forward(self, x) :
        return self.conv_block(x)

    
########## Linear-ReLU-Block Implementation ##########
class LinearBlock(nn.Module) :
    def __init__(self, in_channels, num_classes) :
        super().__init__()
        # Create Linear Layer Instance
        
        self.linear_block = nn.Sequential(nn.Linear(in_channels, in_channels),
                                          nn.ReLU(inplace=True),
                                          nn.Linear(in_channels, in_channels),
                                          nn.ReLU(inplace=True),
                                          nn.Linear(in_channels, num_classes),
                                          nn.Softmax(dim=-1)) 
    
    def forward(self, x) :
        return self.linear_block(x)
    

########## Linear-Dropout-ReLU-Block Implementation ##########
class LinearBlockwithDropout(nn.Module) :
    def __init__(self, in_channels, num_classes, p) :
        super().__init__()
        # Create Linear Layer Instance
        
        self.linear_block = nn.Sequential(nn.Linear(in_channels, in_channels),
                                          nn.Dropout(p),
                                          nn.ReLU(inplace=True),
                                          nn.Linear(in_channels, in_channels),
                                          nn.Dropout(p),
                                          nn.ReLU(inplace=True),
                                          nn.Linear(in_channels, num_classes),
                                          nn.Softmax(dim=-1)) 
    
    def forward(self, x) :
        return self.linear_block(x)


########## VGG-16-Like Model Implementation ##########
class VGG16(nn.Module) :
    def __init__(self, img_channels, width, num_classes) :
        super().__init__()
        
        # Create Convolutional Layer Instance
        self.conv_block_1 = ConvBlock(img_channels, width, num_layers=2)
        self.conv_block_2 = ConvBlock(width, width*2, num_layers=2)
        self.conv_block_3 = ConvBlock(width*2, width*4, num_layers=3)
        self.conv_block_4 = ConvBlock(width*4, width*4, num_layers=3)
        self.conv_block_5 = ConvBlock(width*4, width*4, num_layers=3)
        
        # Create Classifier Layer Instance
        self.classifier = LinearBlock(width*4, num_classes)
    
    def forward(self, x) :
        x = self.conv_block_1(x) # H x W
        x = F.max_pool2d(x, 2, 2)
        
        x = self.conv_block_2(x) # H/2 x W/2
        x = F.max_pool2d(x, 2, 2)
        
        x = self.conv_block_3(x) # H/4 x W/4
        x = F.max_pool2d(x, 2, 2)
        
        x = self.conv_block_4(x) # H/8 x W/8
        x = F.max_pool2d(x, 2, 2)
        
        x = self.conv_block_5(x) # H/16 x W/16
        x = F.max_pool2d(x, 2, 2)
        
        x = F.adaptive_avg_pool2d(x, 1).flatten(start_dim=1)
        x = self.classifier(x)
        
        return x


########## VGG-16-BN-Like Model Implementation ##########
class VGG16withBN(nn.Module) :
    def __init__(self, img_channels, width, num_classes, p) :
        super().__init__()
        
        # Create Convolutional Layer Instance
        self.conv_block_1 = ConvBlockwithBN(img_channels, width, num_layers=2)
        self.conv_block_2 = ConvBlockwithBN(width, width*2, num_layers=2)
        self.conv_block_3 = ConvBlockwithBN(width*2, width*4, num_layers=3)
        self.conv_block_4 = ConvBlockwithBN(width*4, width*4, num_layers=3)
        self.conv_block_5 = ConvBlockwithBN(width*4, width*4, num_layers=3)
        
        # Create Classifier Layer Instance
        self.classifier = LinearBlockwithDropout(width*4, num_classes, p)
    
    def forward(self, x) :
        x = self.conv_block_1(x) # H x W
        x = F.max_pool2d(x, 2, 2)
        
        x = self.conv_block_2(x) # H/2 x W/2
        x = F.max_pool2d(x, 2, 2)
        
        x = self.conv_block_3(x) # H/4 x W/4
        x = F.max_pool2d(x, 2, 2)
        
        x = self.conv_block_4(x) # H/8 x W/8
        x = F.max_pool2d(x, 2, 2)
        
        x = self.conv_block_5(x) # H/16 x W/16
        x = F.max_pool2d(x, 2, 2)
        
        x = F.adaptive_avg_pool2d(x, 1).flatten(start_dim=1)
        x = self.classifier(x)
        
        return x
    

########## Check Model Implementation ##########
if __name__ == "__main__" :
    # Check Device
    device = "cuda" if torch.cuda.is_available() else "cpu"
    print(f"Current Device : {device}")

    # Set Model Parameter
    img_channels, width, num_classes, p = 1, 16, 10, 0.25
    
    # Create Model Instance
    model = VGG16(img_channels, width, num_classes).to(device)
    model_bn = VGG16withBN(img_channels, width, num_classes, p).to(device)
    
    # Summarize Model
    img_size = 32
    summary(model, (img_channels, img_size, img_size))
    summary(model_bn, (img_channels, img_size, img_size))