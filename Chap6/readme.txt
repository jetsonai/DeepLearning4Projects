cd

!git clone https://github.com/jetsonai/pytorch-ssd

cd pytorch-ssd

#onnx 파일 보관 폴더 생성
mkdir onnx

cp ~/Downloads/labels.txt ./onnx/

cp ~/Downloads/mb1-ssd-cctv.pth ./onnx/

# 사진 파일 추론
python3 run_ssd_example.py mb1-ssd onnx/mb1-ssd-cctv.pth ./onnx/labels.txt ./data/drivingcar.jpg

## opencv + ssd 실습

# 영상 파일 추론
python3 my_ssd_opencv.py mb1-ssd onnx/mb1-ssd-cctv.pth ./onnx/labels.txt ./data/run3.mp4

# USB 카메라 추론
python3 my_ssd_opencv.py mb1-ssd onnx/mb1-ssd-cctv.pth ./onnx/labels.txt

## 로깅 추가

# 영상 파일 추론
python3 my_ssd_opencv_cctv.py mb1-ssd onnx/mb1-ssd-cctv.pth ./onnx/labels.txt ./data/detect_cctv.mp4

# USB 카메라 추론
python3 my_ssd_opencv_cctv.py mb1-ssd onnx/mb1-ssd-cctv.pth ./onnx/labels.txt
