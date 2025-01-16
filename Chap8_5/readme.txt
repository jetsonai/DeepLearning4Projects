cd ~/DeepLearning4Projects/Chap8_5

!git clone -b v7.0 https://github.com/jetsonai/yolov5
!pip install -r yolov5/requirements.txt

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

4. yolov5s_voc를 TensorRT 엔진 파일로 변환합니다.
./yolov5_det -s yolov5s_voc.wts yolov5s_voc.engine s

5. 변환한 엔진 파일을 확인하기 위해 TensorRT로 추론을 수행합니다.
./yolov5_det -d yolov5s_voc.engine ../images

TensorRT를 활용해 추론 실행 코드
DeepLearning4Projects/Chap8_5/detect_video.py

python3 detect_video.py
