# 실습 방법

cd ~/DeepLearning4Projects/Chap8_5

https://github.com/jetsonai/DeepLearning4Projects/blob/main/AdditionTest/prepare_env_in_jetson.sh

1. 홈 경로의 tensorrtx/yolov5 폴더에서 build 폴더를 생성한 후 yolov5s_voc.wts 파일을 build
폴더 아래로 이동합니다.

cd ~/tensorrtx/yolov5
mkdir build && cd build && cp ~/Downloads/yolov5s_voc.wts .

2. ~/tensorrtx/yolov5/src/config.h의 설정을 훈련한 모델과 추론 설정에 맞게 수정합니다.
⋯
constexpr static int kNumClass = 20;
⋯
constexpr static int kInputH = 480;
constexpr static int kInputW = 480;

3. 빌드를 수행합니다.
cmake ..
make

https://github.com/jetsonai/DeepLearning4Projects/blob/main/AdditionTest/YOLO5_TRT_Test.txt

