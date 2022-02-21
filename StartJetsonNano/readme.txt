
git clone https://github.com/jetsonai/DeepLearning4Projects

cd DeepLearning4Projects/StartJetsonNano

chmod 777 *.sh

./install_nano_basic.sh

./install-pytorch.sh
   -> It might take more than 40 minutes.
   
./install_torch2trt.sh


# To Check

python3

import torch
import torchvision

cd installSwapfile

chmod 777 *.sh
./installSwapfile.sh

sudo reboot




sudo sh -c 'echo 50 > /sys/devices/pwm-fan/target_pwm'

