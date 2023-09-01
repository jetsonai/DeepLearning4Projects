#!/bin/bash
sudo apt install libblas-dev liblapack-dev libatlas-base-deb gfortran
python3 -m pip install --upgrade pip
python3 -m pip install cython==0.29.15
python3 -m pip install numpy==1.18.5
python3 -m pip install scipy==1.4.1
python3 -m pip install seaborn==0.11.0
python3 -m pip install pandas==1.1.4
cp weights/yolov5s_voc.pt ~/yolov5s_voc.pt
cp detect_video.py ~/detect_video.py
cd ~
git clone -b v7.0 https://github.com/jetsonai/yolov5
git clone -b yolov5-v7.0 https://github.com/jetsonai/tensorrtx
python3 -m pip install tqdm thop ipython psutil 
cp ~/tensorrtx/yolov5/gen_wts.py ~/yolov5/.
cp ~/yolov5s_voc.pt ~/yolov5/.
cp ~/detect_video.py ~/tensorrtx/yolov5/.
wget https://files.pythonhosted.org/packages/5e/3f/5658c38579b41866ba21ee1b5020b8225cec86fe717e4b1c5c972de0a33c/pycuda-2019.1.2.tar.gz
tar xvf pycuda-2019.1.2.tar.gz
cd pycuda-2019.1.2
python3 configure.py --cuda-root=/usr/local/cuda
sudo python3 setup.py install