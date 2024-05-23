# 8.5장의 예제를 나노보다 고 사양 젯슨 보드에서 테스트 가능한 스크립트입니다.

# 본 페이지는 1 번 Jetpack 버전 4.6, 2번 Jetpack 버전 5.0.2 로 구성되어 있습니다.

# 1번 Jetpack 버전 4.6  

Jetson TX2, Tetson AGX Xavier Jetpack 4.6 버전이 설치된 상태에서 테스트를 시작합니다.(4.6.x)

본 레파지토리를 다운받은 후

cp DeepLearning4Projects/AdditionTest/*.sh ~

sh install_basic.sh

(20~30분 소요)
(만약 matplot 설치 중 에러나면서 종료되면 install_basic_no_matplot.sh 으로 다시 설치해주세요)

sh install_pytorch_1.10.0.sh

(한시간 쯤 소요)

sh prepare_env_in_jetson.sh

(30~40분 쯤 소요)

이후에는 YOLO5_TRT_Test.txt 를 보면서 따라해보세요.

# 2번 Jetpack 버전 5.0.2

Tetson AGX Xavier Jetpack 5.0.2 버전이 설치된 상태에서 테스트를 시작합니다.

본 레파지토리를 다운받은 후

cp DeepLearning4Projects/AdditionTest/*.sh ~

sh install_basic.sh

(20~30분 소요)
(만약 matplot 설치 중 에러나면서 종료되면 install_basic_no_matplot.sh 으로 다시 설치해주세요)

sh install_pytorch_1.11_p38.sh

(한시간 쯤 소요)

sh prepare_env_in_jetson_jp5.sh

(30~40분 쯤 소요)

이후에는 YOLO5_TRT_Test.txt 를 보면서 따라해보세요.
(이 버전은 engine 파일 생성 시간이 4버전 대와 비교하여 5~10배정도 길게 소요됩니다만 생성 후 실행 시간은 문제 없습니다)

안되는 부분 있으면 말씀해주세요 !!
