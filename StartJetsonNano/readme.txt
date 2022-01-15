
git clone https://github.com/jetsonai/DeepLearning4Projects

cd DeepLearning4Projects/StartJetsonNano

chmod 777 *.sh

./install_nano_basic.sh

./install-pytorch.sh
   -> It might take more than 40 minutes.
   
./install_torch2trt.sh


No module named 'packaging'

# To Check

python3

import torch
import torchvision

cd installSwapfile

./installSwapfile.sh

sudo reboot
