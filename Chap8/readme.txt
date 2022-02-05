cd

#라이브러리 소스 다운로드
git clone https://github.com/dusty-nv/jetson-inference

cd jetson-inference

git checkout 19ed62150b3e9499bad2ed6be1960dd38002bb7d

git submodule update –init

#라이브러리 빌드(컴파일)
mkdir build

cd build

#cmake 다음의 .. 은 리눅스에서 하위 폴더를 가리킵니다.
cmake ../

make

# 라이브러리의 시스템 설치
sudo make install

sudo ldconfig

cd
!git clone https://github.com/jetsonai/pytorch-ssd

cd pytorch-ssd

#onnx 파일 보관 폴더 생성
mkdir onnx

cp ~/Downloads/labels.txt ./onnx/

cp ~/Downloads/mb1-ssd-cctv.pth ./onnx/

# pth -> onnx 변환

python3 onnx_export.py --model-dir=./onnx 
