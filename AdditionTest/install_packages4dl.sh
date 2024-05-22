#!/bin/bash

sudo apt-get update

sudo apt-get install libpython3-dev -y

sudo apt install python-dev python3-dev python-pip python3-pip python-numpy python3-numpy \
  python3-matplotlib python3-venv -y

sudo -H pip install -U jetson-stats

echo "export LD_LIBRARY_PATH=\$LD_LIBRARY_PATH:/usr/local/cuda/lib64" >> ~/.bashrc
echo "export PATH=\$PATH:/usr/local/cuda/bin" >> ~/.bashrc
echo "export OPENBLAS_CORETYPE=ARMV8" >> ~/.bashrc

sudo -H pip3 install --upgrade --ignore-installed pip setuptools

sudo apt install libcanberra-gtk-module libcanberra-gtk3-module -y

wget https://nvidia.box.com/shared/static/fjtbno0vpo676a25cgvuqc1wty0fkkg6.whl -O torch-1.10.0-cp36-cp36m-linux_aarch64.whl
sudo apt-get install python3-pip libopenblas-base libopenmpi-dev -y


pip3 install pillow

python3 -m pip install Cython 
python3 -m pip install wheel
python3 -m pip install numpy
python3 -m pip install torch-1.10.0-cp36-cp36m-linux_aarch64.whl


sudo apt-get install libjpeg-dev zlib1g-dev libpython3-dev libavcodec-dev libavformat-dev libswscale-dev -y
git clone --branch v0.11.1 https://github.com/pytorch/vision torchvision
cd torchvision
export BUILD_VERSION=0.11.1
sudo python3 setup.py install --user
cd ../  # attempting to load torchvision from build dir will result in import error

python3 -m pip install tqdm thop seaborn ipython psutil pyyaml

