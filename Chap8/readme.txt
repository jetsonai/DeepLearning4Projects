cd

#라이브러리 소스 다운로드
git clone https://github.com/dusty-nv/jetson-inference

cd jetson-inference

git checkout 19ed62150b3e9499bad2ed6be1960dd38002bb7d

git submodule update --init

#라이브러리 빌드(컴파일)
mkdir build

cd build

#cmake 다음의 .. 은 리눅스에서 하위 폴더를 가리킵니다.
cmake ../

make

# 라이브러리의 시스템 설치
sudo make install

sudo ldconfig



-----------------------------------------------------------------------------------
# 만약 pytorch-ssd 폴더가 없으면 다시 받는다. 하지만 6장 실습에서 받아놓았을 것이다.
cd
git clone https://github.com/jetsonai/pytorch-ssd

cd pytorch-ssd

#onnx 파일 보관 폴더 생성
mkdir onnx
-----------------------------------------------------------------------------------

cd pytorch-ssd

cp ~/Downloads/labels.txt ./onnx/

cp ~/Downloads/mb1-ssd-cctv.pth ./onnx/

# pth -> onnx 변환
python3 onnx_export.py --model-dir=./onnx --input=mb1-ssd-cctv.pth --labels=labels.txt

ls ./onnx/ssd-mobilenet.onnx

cp -rf /onnx/ ~/Ai-LearningBot/followingbot

cd ~/Ai-LearningBot/followingbot

detectnet --model=onnx/ssd-mobilenet.onnx --labels=onnx/labels.txt  --input-blob=input_0 --output-cvg=scores --output-bbox=boxes 

python3 my_ssd_detectnet.py --model=onnx/ssd-mobilenet.onnx --labels=onnx/labels.txt  --input-blob=input_0 --output-cvg=scores --output-bbox=boxes




