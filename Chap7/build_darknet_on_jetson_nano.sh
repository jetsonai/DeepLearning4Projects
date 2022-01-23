#!/bin/bash
git clone https://github.com/jetsonai/darknet.git
cp Makefile_Nano darknet/Makefile
cd darknet && make -j $(nproc)
wget https://github.com/AlexeyAB/darknet/releases/download/darknet_yolo_v4_pre/yolov4-tiny.weights
./darknet detect cfg/yolov4-tiny.cfg yolov4-tiny.weights data/dog.jpg
cd ../
mv vocnames.txt darknet/
mv vocdata.txt darknet/
mv yolov4-tiny_voc.cfg darknet/
mv yolov4-tiny_voc_last.weights darknet/
mv darknet_video.py darknet/
mv challenge.mp4 darknet/
