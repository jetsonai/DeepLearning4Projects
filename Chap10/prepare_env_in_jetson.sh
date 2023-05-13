#!/bin/bash
cd ~
git clone -b v7.0 https://github.com/jetsonai/yolov5
git clone -b yolov5-v7.0 https://github.com/jetsonai/tensorrtx
python3 -m pip install --upgrade pip
python3 -m pip install tqdm thop seaborn