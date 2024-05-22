8.5장의 예제를 TX2나 Xavier 에 Jetpack 4.6 버전이 설치된 상태에서 테스트 가능한 스크립트입니다.

본 레파지토리를 다운받은 후

cp DeepLearning4Projects/AdditionTest/*.sh ~

cp DeepLearning4Projects/AdditionTest/yolov5s_voc.wts ~/Downloads

sh install_packages4dl.sh

(한시간 반쯤 소요)

sh prepare_env_in_jetson.sh

(40분 쯤 소요)

이후에는 YOLO5_TRT_Test.txt 를 보면서 따라해보세요.

안되는 부분 있으면 말씀해주세요 !!
