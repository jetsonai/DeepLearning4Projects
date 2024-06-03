sudo ./yolov7 -s yolov7-tiny.wts yolov7-tiny.engine t
sudo ./yolov7 -d yolov7-tiny.engine ../images
cd ..
ls
ls build/
cp ~/Downloads/yv7_detect_usb_camera.py .
python3 yv7_detect_usb_camera.py 
