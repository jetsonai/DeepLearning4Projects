
# pytorch-ssd Jetson Nano 실습

* 나노에서 실습 시 swap 설정 필수 !!
  
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
```

## 로그 수정 TODO

```
            lv = f"{labels[i]}"
            if lv == '3':
                  # 타임로그, 라벨, 신뢰도를 로그에 남김.
                Data = "[{}] classID: {} conf:{}\n".format(getTimeLog(), labels[i], probs[i])
                print(Data)
                f.write(Data)
```

-----------------------------------------------------------

# Torch2TRT로 onnx 변환

## pytorch-ssd 폴더로 이동

cd pytorch-ssd

## pth -> onnx 변환 (3~5분 정도 시간 소요)

python3 onnx_export.py --model-dir=./onnx

## 완료되면 다음과 같이 변환된 onnx 파일 확인 가능

ls ./onnx/ssd-mobilenet.onnx

## following_test.py 파일을 pytorch-ssd 폴더로 복사

cp ~/AILearningJetbot/FollowingBot/following_test.py ./

following_test.py 의 96line 에 ClassID == 3 으로 변경하고 저장

## 최초 추론 테스트에서는 onnx 파일을 tensorrt 엔진 파일로 변환하는 데 5~10분 정도 소요

python3 following_test.py --model=onnx/ssd-mobilenet.onnx --labels=onnx/labels.txt
--input-blob=input_0 --output-cvg=scores --output-bbox=boxes
