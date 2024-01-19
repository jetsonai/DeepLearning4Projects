# pytorch-ssd 폴더로 이동
```
cd pytorch-ssd
```
mkdir onnx

# pth -> onnx 변환 (3~5분 정도 시간 소요)
```
cp models/ssd_example/* ./onnx
```
python3 onnx_export.py --model-dir=./onnx --input=ssd_cctv_sample.pth

# 완료되면 다음과 같이 변환된 onnx 파일 확인 가능
```
ls ./onnx/ssd-mobilenet.onnx

------------------------------------------------

# following_test.py 파일을 pytorch-ssd 폴더로 복사

```
cp ~/AILearningJetbot/FollowingBot/detectnet_test.py ./

# 최초 추론 테스트에서는 nonx 파일을 tensorrt 엔진 파일로 변환하는 데 ~5~10분 정도 소요

```
python3 detectnet_test.py --model=onnx/ssd-mobilenet.onnx --labels=onnx/labels.txt --input-blob=input_0 --output-cvg=scores --output-bbox=boxes
```
