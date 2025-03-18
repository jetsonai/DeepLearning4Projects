# YOLOv5 실습 방법

## wts 파일 만들기

Colab 에서 Convert_YOLOv5_For_tensorrtx.ipynb 파일을 이용하여 yolov5s_voc.wts 을 생성시켜줍니다.

%cd
git clone https://github.com/ultralytics/yolov5

## Jetson Nano 에서 실행

### 환경 세팅 (제공된 이미지에는 세팅되어 있으니 스킵해주세요)

cd ~/DeepLearning4Projects/Chap8_5

다음의 스크립트를 실행하고

wget https://raw.githubusercontent.com/jetsonai/DeepLearning4Projects/main/AdditionTest/prepare_env_in_jetson.sh

1. 홈 경로의 tensorrtx/yolov5 폴더에서 build 폴더를 생성한 후 yolov5s_voc.wts 파일을 build
폴더 아래로 이동합니다.

cd ~/tensorrtx/yolov5

mkdir build && cd build 

2. ~/tensorrtx/yolov5/src/config.h의 설정을 훈련한 모델과 추론 설정에 맞게 수정합니다.
⋯
constexpr static int kNumClass = 20;
⋯
constexpr static int kInputH = 480;
constexpr static int kInputW = 480;

3. 빌드를 수행합니다.
   
cmake ..

make

## 터미널을 열고 다음과 같이 실행합니다.

cd ~/tensorrtx/yolov5/build

cp ~/Downloads/yolov5s_voc.wts .

cd ~/tensorrtx/yolov5/

cp ~/DeepLearning4Projects/Chap8_5/detect_video.py . 

python3 detect_video.py


# YOLOv8 실습 방법 ( > Jetpack 4.6.1 )

## Start Docker Container

DOCKER_ULTRA_NANO_RESTART

DOCKER_ULTRA_NANO_ATTACH

## Check Exercise python files

## Execute Test

python3 yolov8test.py 

## Convert TRT

yolo export model=yolov8n.pt format=engine device="dla:0" half=True : X

--> yolo export model=yolov8n.pt format=engine half=True

## Execute TRT Test

python3 yolov8trt_test.py





