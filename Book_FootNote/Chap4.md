# 4장 이미지 분할과 객체 인식
# 각주 모음

## 124 page
  1. 이미지 분할: [Image segmentation](https://en.wikipedia.org/wiki/Image_segmentation)
  2. 의미론적 분할: [Image Semantic Segmentation](https://wiki.tum.de/display/lfdv/Image+Semantic+Segmentation)

## 125 page     
  3. 시내 도로 화면에 대한 이미지 분할 [이미지 분할 예제 결과](https://colab.research.google.com/drive/1q_eCYEzKxixpCKH1YDsLnsvgxl92ORcv?usp=sharing#scrollTo=p097LwAST1v9)
  4. 덴스 예측(dense prediction): 컴퓨터 비전에서 픽셀 단위 밀도 예측은 이미지의 각 픽셀에 대한 레이블을 예측하는 작업입니다.
  [〈Dense Prediction on Sequences with Time-Dilated Convolutions for Speech Recognition〉](https://arxiv.org/pdf/1611.09288.pdf), Tom Sercu, 2016

## 127 page
  5. [재현율(recall)과 정밀도(precision)](https://en.wikipedia.org/wiki/Precision_and_recall)
  6. 정확도와 감도, 그리고 임곗값에 관해 조금 더 살펴보고자 한다면 이 책의 9장에 있는 그림 9.32를 참조합니다.
  7. [mAP](https://en.wikipedia.org/wiki/Evaluation_measures_(information_retrieval)#Mean_average_precision)
  8. [AP](https://en.wikipedia.org/wiki/Evaluation_measures_(information_retrieval)#Average_precision)

## 129 page     
  9. 수용 영역(receptive field): 출력 레이어의 뉴런 하나에 영향을 미치는 입력 뉴런들의 공간 크기입니다
  10. FC를 밀집 계층(dense layer)라고도 합니다. 밀집 계층이란 깊게 연결된 신경망 계층입니다. 즉, 밀집 계층의 각 뉴런은 이전 계층의 모든 뉴런에서
입력을 받습니다.
  11. FC 계층을 모두 Conv 계층으로 대체해 히트맵을 획득 [〈Fully Convolutional Networks for Semantic Segmentation〉](https://arxiv.org/pdf/1411.4038.pdf), Jonathan Long, 2015

## 130 page
  12. 각 특징 맵은 하나의 클래스를 대표하게 됩니다: 이를 히트맵이라고 부릅니다.
  13. 거친 결과 맵(coarse output map): 해상도가 낮은 맵

## 131 page
  14. 업샘플링(up sampling): 이러한 다운샘플링, 업샘플링 과정을 각각 인코더, 디코더라고 부르기도 합니다.
  15. 스킵 구조: 〈Fully Convolutional Networks for Semantic Segmentation〉, Jonathan Long, 2015, 논문의 그림 3, https://arxiv.org/pdf/1411.4038.pdf

## 133 page
  16. FCN 이미지와 라벨, 그리고 추론 후 이미지 분할 결과: 〈Fully Convolutional Networks for Semantic Segmentation〉, Jonathan Long, 2015, 논문의 그림 4, https://arxiv.org/pdf/1411.4038.pdf

## 134 page
  17. 멀티 레이블 이미지 분류(multi-labeled classification): 한 이미지에서 여러 클래스의 객체를 분류합니다.
  18. 바운딩 박스 회귀(bounding box regression): box의 좌푯값을 회귀 모델로 예측합니다
  19. 객체 인식 = 멀티 레이블 이미지 분류 + 바운딩 박스 회귀 : [그림 참조](http://cs231n.stanford.edu/slides/2017/cs231n_2017_lecture11.pdf)

## 136 page
  20. 객체 인식은 산출 결과의 수를 예측하기 어렵다는 문제가 있다.: [그림 참조](http://cs231n.stanford.edu/slides/2017/cs231n_2017_lecture11.pdf)

## 137 page
  21. 슬라이딩 윈도(sliding window): 컴퓨터 비전의 맥락에서 슬라이딩 윈도는 고정된 너비와 높이의 직사각형 영역이 이미지를 가로질러 ‘슬라이드’하면서
객체 인식 등을 수행하는 방법입니다.
  22. HOG(Histogram of oriented gradients): 물체 감지를 위해 컴퓨터 비전 및 이미지 처리에 사용되는 기능 설명자입니다. 이 기술은 이미지의 영역화된
부분에서 그래디언트 방향의 발생 횟수를 계산합니다. https://en.wikipedia.org/wiki/Histogram_of_oriented_gradients
  23. 셀렉티브 서치(selective search): 물체 감지 작업을 위한 영역 제안 알고리즘입니다. https://paperswithcode.com/method/selective-search
  24. Fast R-CNN의 속도 문제: [그림 참조](http://cs231n.stanford.edu/slides/2017/cs231n_2017_lecture11.pdf)

## 138 page
  25. RPN과 Fast R-CNN으로 구성된 Faster R-CNN: 〈Faster R-CNN: Towards Real-Time Object Detection with Region Proposal Networks〉, Shaoqing Ren, Kaiming He, Ross Girshick, Jian Sun, 2015, https://arxiv.org/pdf/1506.01497.pdf 논문의 그림 2.

## 139 page
  26. 앵커 박스: 〈Faster R-CNN: Towards Real-Time Object Detection with Region Proposal Networks〉, Shaoqing Ren, Kaiming He, Ross Girshick, Jian Sun, 2015, https://arxiv.org/pdf/1506.01497.pdf 논문의 그림 3.

## 140 page
  27. Faster R-CNN 테스트 시간: http://cs231n.stanford.edu/slides/2017/cs231n_2017_lecture11.pdf

## 141 page
  28. Fast R-CNN 검출 결과 PASCAL VOC 2007 & PASCAL VOC 2012: 〈Faster R-CNN: Towards Real-Time Object Detection with Region Proposal Networks〉, Shaoqing Ren, Kaiming He, Ross Girshick, Jian Sun, 2015, https://arxiv.org/pdf/1506.01497.pdf 논문의 표 3 참조.

## 142 page
  29. YOLO: 〈You Only Look Once: Unified, Real-Time Object Detection〉, Joseph Redmon, Santosh Divvala, Ross Girshick, Ali Farhadi, 2016, https://pjreddie.com/media/files/papers/yolo.pdf
  30. objectness: [객체가 존재하는 상태(The state of being an object)](https://en.wiktionary.org/wiki/objectness)
  31. YOLO의 모델 이해 : 〈You Only Look Once: Unified, Real-Time Object Detection〉, Joseph Redmon, Santosh Divvala, Ross Girshick, Ali Farhadi, 2016, https://pjreddie.com/media/files/papers/yolo.pdf 그림 2 참조

## 144 page
  32. 1×1 레이어에 대해서는 3.3절에서 다룬 GoogLeNet을 참조하세요.
  33. YOLO의 네트워크 아키텍처: 〈You Only Look Once: Unified, Real-Time Object Detection〉, Joseph Redmon, Santosh Divvala, Ross Girshick, Ali Farhadi, 2016, https://pjreddie.com/media/files/papers/yolo.pdf 그림 3 참조

## 147 page
  34. [객체 인식 모델에서 임곗값의 선택](https://towardsdatascience.com/non-maximum-suppression-nms-93ce178e177c)

## 148 page
  35. YOLO의 Pascal VOC 2007 실시간 추론 성능: 〈You Only Look Once: Unified, Real-Time Object Detection〉, Joseph Redmon, Santosh Divvala, Ross Girshick, Ali Farhadi, 2016, https://pjreddie.com/media/files/papers/yolo.pdf, 논문의 표 1 참조

## 149 page
  36. YOLOv2 논문: [〈YOLO9000: Better, Faster, Stronger〉](Joseph Redmon, Ali Farhadi, 2016, https://arxiv.org/pdf/1612.08242.pdf)
  37. SSD(Single Shot MultiBox Detector): 4.4절 참조
  38. YOLOv2의 Pascal VOC 2007 실시간 추론 성능: 〈YOLO9000: Better, Faster, Stronger〉, Joseph Redmon, Ali Farhadi, 2016,, 논문의 표 3 참조

## 151 page
  39. 수용 영역(receptive field): 수용 영역(receptive field)은 출력 레이어의 뉴런 하나에 영향을 미치는 입력 뉴런들의 공간 크기를 말합니다.
      
## 153 page
  40. YOLOv2는 좋은 IoU 점수로 이어지는 k-평균 클러스터링을 사용 :〈YOLO9000: Better, Faster, Stronger〉, Joseph Redmon, Ali Farhadi, 2016, 논문의 그림 2 참고
  41. 직접 측위 예측(Direct Location Prediction) :〈YOLO9000: Better, Faster, Stronger〉, Joseph Redmon, Ali Farhadi, 2016, 논문의 그림 3 참고
  42. Darknet-19 :〈YOLO9000: Better, Faster, Stronger〉, Joseph Redmon, Ali Farhadi, 2016, 논문의 표 6 참고

## 154 page
  43. 패스스루 레이어(pass-through layer): [참조](https://www.programmersought.com/article/831212120/)

## 155 page
  44. 최종 성능 테이블: 〈YOLO9000: Better, Faster, Stronger〉, Joseph Redmon, Ali Farhadi, 2016, 논문의 표 2 참고

## 156 page
  45. YOLOv3 논문 : [〈YOLOv3: An Incremental Improvement〉](https://arxiv.org/pdf/1804.02767.pdf), Redmon, Ali Farhadi, 2018,  논문의 그림 1
  46. 바운딩 박스: 크기와 위치 정보가 있는 앵커 박스의 의미.
  47. 그림 4.22 바운딩 박스의 위치 정보 참조
  48. 로지스틱 회귀: [independent logistic regression](https://en.wikipedia.org/wiki/Logistic_regression)
      
## 154 page
  43. 패스스루 레이어(pass-through layer): [참조](https://www.programmersought.com/article/831212120/)

## 154 page
  43. 패스스루 레이어(pass-through layer): [참조](https://www.programmersought.com/article/831212120/)

## 154 page
  43. 패스스루 레이어(pass-through layer): [참조](https://www.programmersought.com/article/831212120/)

## 154 page
  43. 패스스루 레이어(pass-through layer): [참조](https://www.programmersought.com/article/831212120/)

## 154 page
  43. 패스스루 레이어(pass-through layer): [참조](https://www.programmersought.com/article/831212120/)




     
