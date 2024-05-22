#!/bin/bash
cp detect_video.py ~/detect_video.py
cd ~
git clone -b yolov5-v7.0 https://github.com/jetsonai/tensorrtx
cp ~/detect_video.py ~/tensorrtx/yolov5/.
wget https://files.pythonhosted.org/packages/5e/3f/5658c38579b41866ba21ee1b5020b8225cec86fe717e4b1c5c972de0a33c/pycuda-2019.1.2.tar.gz
tar xvf pycuda-2019.1.2.tar.gz
cd pycuda-2019.1.2
python3 configure.py --cuda-root=/usr/local/cuda
sudo python3 setup.py install