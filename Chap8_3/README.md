
# pytorch-ssd Jetson Nano 실습
## pytorch-ssd 저장소 복사
```
git clone https://github.com/jetsonai/pytorch-ssd
```
## pytorch-ssd 경로 이동
```
cd pytorch-ssd
```
## 사진 파일 추론
```
python3 run_ssd_example.py mb1-ssd ./models/ssd_example/ssd_cctv_sample.pth ./models/ssd_example/labels.txt ./data/drivingcar.jpg
```
## 영상 파일 추론
```
python3 inference_ssd_nano.py ./models/ssd_example/ssd_cctv_sample.pth ./models/ssd_example/labels.txt ./data/run3.mp4
```
## cctv file 추론
```
python3 inference_ssd_nano.py ./models/ssd_example/ssd_cctv_sample.pth ./models/ssd_example/labels.txt ./data/detect_cctv.mp4
```
## cctv camera 추론
```
python3 inference_ssd_nano.py ./models/ssd_example/ssd_cctv_sample.pth ./models/ssd_example/labels.txt
```

## cctv file 추론 & log
```
python3 inference_ssd_nano_log.py ./models/ssd_example/ssd_cctv_sample.pth ./models/ssd_example/labels.txt ./data/detect_cctv.mp4
```
## cctv camera 추론 & log
```
python3 inference_ssd_nano_log.py ./models/ssd_example/ssd_cctv_sample.pth ./models/ssd_example/labels.txt 
