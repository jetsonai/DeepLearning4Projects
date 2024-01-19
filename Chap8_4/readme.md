* 쿠다 빌드 환경설정이 안 되었다면 반드시 다음의 설정을 하시길 바랍니다.
```
echo "export LD_LIBRARY_PATH=\$LD_LIBRARY_PATH:/usr/local/cuda/lib64" >> ~/.bashrc
```
```
echo "export PATH=\$PATH:/usr/local/cuda/bin" >> ~/.bashrc
```
```
echo "export OPENBLAS_CORETYPE=ARMV8" >> ~/.bashrc
```

## 다크넷 빌드 및 테스트

* 다크넷 소스를 다운받고 빌드합니다.
```
sh ./build_darknet_on_jetson_nano.sh
```
```
cd darknet
```

* 영상 테스트
```
python3 darknet_video.py \
--input blackbox_video.avi \
--weights yolov4-tiny_voc_last.weights \
--config_file yolov4-tiny_voc.cfg \
--data_file vocdata.txt \
--thresh 0.25
```

# 카메라 테스트

소스 수정
```
    if input_path == 0:
        gst_str = ("nvarguscamerasrc ! video/x-raw(memory:NVMM), width=(int)640, height=(int)480, format=(string)NV12, framerate=(fraction)60/1 ! nvvidconv flip-method=0 ! video/x-raw, width=(int)640, height=(int)480, format=(string)BGRx ! videoconvert ! video/x-raw, format=(string)BGR ! appsink")
        input_path = gst_str
```

테스트 실행
```
python3 darknet_video.py \
--input 0 \
--weights yolov4-tiny_voc_last.weights \
--config_file yolov4-tiny_voc.cfg \
--data_file vocdata.txt \
--thresh 0.25
```
