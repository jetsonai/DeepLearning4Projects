# 3장 딥러닝 영상분석을 위한 학습 과정 
# 각주 모음

## 72 page
  1. 최적화 솔버(Solver): 최적화 방법, 혹은 솔버라고 부르기도 합니다.

## 73 page     
  2. 극솟값(local minima, 왼쪽)과 안장점(saddle point, 오른쪽) [cs231n Lecture 7 | Training Neural Networks II](https://youtu.be/_JB0AO7QxSA)

## 74 page
  3. [Avoiding Local Minima](https://www.i2tutorials.com/how-can-you-avoid-local-minima-to-achieve-the-minimized-loss-function)

## 75 page     
  4. [모멘텀과 NAG의 차이](https://untitledtblog.tistory.com/149)

## 76 page     
  5. Adagrad: 가중치 W는 수많은 파라미터로 이뤄지는데, 학습을 진행하면서 파라미터의 변화량은 서로 동일하지 않습니다. 이 중 변화량이큰 파라미터는 최적화가
많이 진행됐고 변화량이 적은 파라미터는 최적화가 적게 진행됐다는 의미이기 때문에 변화량에 따라 최적화 속도를 다르게 해준다는 개념입니다.

## 77 page     
  6. [〈Adam: A Method for Stochastic Optimization〉](https://arxiv.org/abs/1412.6980), Diederik P. Kingma, Jimmy Ba, 2014

## 80 page     
  7. 학습률 [cs231n Lecture 6 | Training Neural Networks I](https://youtu.be/wEoyxE0GP2M)
  8. 자비에(Xavier) 초기 코: ≪밑바닥부터 시작하는 딥러닝≫(한빛미디어, 2017), 206쪽
  9. 자비에(Xavier) 초기: 〈Understanding the difficulty of training deep feedforward neural networks〉, Xavier Glorot, Yoshua Bengio, 2010
  10. He 초기화: [〈Delving Deep into Rectifiers: Surpassing Human-Level Performance on ImageNet Classification〉](https://arxiv.org/abs/1502.01852), Kai’ming He, Xiangyu Zhang, Shaoqing
Ren, Jian Sun, 2015

## 81 page     
  11. 배치 정규화(batch normalization) [〈Batch Normalization: Accelerating Deep Network Training by Reducing Internal Covariate Shift〉](https://arxiv.org/abs/1502.03167), Sergey Ioffe, Christian Szegedy, 2015
  12. 데이터의 정규화: ≪파이썬 날코딩으로 알고 짜는 딥러닝 - 프레임워크 없이 단층 퍼셉트론에서 GAN까지≫(한빛미디어, 2019), 336쪽

## 82 page
  13. 데이터 증강: ‘데이터 어그먼테이션(Data Augmentation)’이라고 많이 부릅니다.

## 83 page
  14. [데이터 증강의 예](https://nanonets.com/blog/data-augmentation-how-to-use-deep-learning-when-you-have-limited-data-part-2/)

## 89 page
  15. [Albumentations](https://albumentations.ai/)

## 90 page     
  16. 전이학습 [cs231n Lecture 7 | Training Neural Networks II,](https://youtu.be/_JB0AO7QxSA)
  17. 세 가지 주요 전이학습 시나리오: [Transfer Learning](https://cs231n.github.io/transfer-learning/)
  18. ≪핸즈온 머신러닝≫(한빛미디어, 2018), 306쪽

## 91 page     
  19. LeNet(1998년) [그림 참조](http://vision.stanford.edu/cs598_spring07/papers/Lecun98.pdf) 〈Gradient-Based Learning Applied to Document Recognition〉
  20. , Yann LeCun Leon Bottou Yoshua Bengio and Patrick Haffner, 1998,

## 92 page     
  20. ImageNet 최초로 CNN 기반으로 우승한 AlexNet(2012년) [그림 참조](https://youtu.be/DAOcjicFr1Y) 
  21. [AlexNet](https://en.wikipedia.org/wiki/AlexNet)
  22. ≪텐서플로로 배우는 딥러닝≫(영진닷컴, 2018), 145쪽

## 93 page     
  23. AlexNet의 구성 [〈ImageNet Classification with Deep Convolutional Neural Networks〉](http://
www.cs.toronto.edu/~hinton/absps/imagenet.pdf), Alex Krizhevsky, Ilya Sutskever, Geoffrey E. Hinton, 2012

## 94 page     
  24. AlexNet(2012년) [그림 참조](https://medium.com/@shangethrajaa/alexnet-a-deep-learning-breakthrough-aaddb9ac0078) 

## 95 page     
  25. 딥러닝에 필요한 수조에 달하는 수학 연산을 GPU를 통해 처리 [GPU: 인공지능의 발전을 가속화하는 새로운 컴퓨팅 모델](https://blogs.nvidia.co.kr/2016/02/15/accelerating-ai-artificial-intelligence-gpus/)
  26. ILSVRC의 VGGNet과 GoogLeNet(2014년) [그림 참조](https://youtu.be/DAOcjicFr1Y) 

## 96 page     
  27. 6가지 VGGNet의 구성 [그림 참조](https://arxiv.org/pdf/1409.1556.pdf)
⟨Very Deep Convolutional Networks for Large-Scale Image Recognition⟩, Karen Simonyan & Andrew Zisserman, 2014

## 97 page     
  28. AlexNet과 VGG16, VGG19 : ≪텐서플로로 배우는 딥러닝≫(영진닷컴, 2018), 147쪽
  29. VGGNet 특징: ≪밑바닥부터 시작하는 딥러닝≫(한빛미디어, 2017), 267쪽

## 98 page     
  30. [Review: GoogLeNet](https://medium.com/coinmonks/paper-review-of-googlenet-inception-v1-winner-of-ilsvlc-2014-imageclassification-
c2b3565a64e7)
  31. GoogLeNet의 특징: ≪Going deeper with convolutions≫, Christian Szegedy, Wei Liu, Yangqing Jia, 2014
  32. AGP(Average Global Pooling)는 이 장의 끝에서 설명합니다.

## 100 page     
  33. [〈Network In Network〉](https://arxiv.org/pdf/1312.4400.pdf), Min Lin, Qiang Chen, Shuicheng Yan
  34. 다층 퍼셉트론을 멀티레이어 퍼셉트론(MultiLayer Perceptron, MLP)이라고도 합니다.
  35. 네트워크 레이어가 깊을수록 많은 파라미터를 가지게 됨: [GoogLeNet](https://poddeeplearning.readthedocs.io/ko/latest/CNN/GoogLeNet/)
  36. 그래디언트 소실: [배니싱 그래디언트(Vanishing gradient problem)](https://en.wikipedia.org/wiki/Vanishing_gradient_problem)

## 101 page     
  37. 인셉션 모듈 (a) 초기 버전 (b) 차원 축소 버전: 〈Going deeper with convolutions, Christian Szegedy〉, Wei Liu, Yangqing Jia, 2014
      
## 103 page     
  38. FC 계층과 GAP 계층의 차이 [그림 참조](https://medium.com/coinmonks/paper-review-ofgooglenet-inception-v1-winner-of-ilsvlc-2014-image-classification-c2b3565a64e7) 

## 105 page     
  39. ResNet [〈Deep Residual Learning for Image Recognition〉](https://openaccess.thecvf.com/content_cvpr_2016/papers/He_Deep_Residual_Learning_CVPR_2016_paper.pdf)
, Kaiming He, Xiangyu Zhang, Shaoqing Ren, Jian Sun, 2015
  40. [Introduction to ResNets](https://towardsdatascience.com/introduction-to-resnets-c0a830a288a4)
  41. 학습 및 테스트 오류 : 논문의 그림 1 제목이 “Training error and test error on CIFAR-10 with 20-layer and 56-layer“plain” networks”인데 여기서
error는 손실값의 의미입니다.

## 106 page     
  42. 잔차 블록(Residual Block) : ‘레지듀얼 블록(Residual Block)’이라고도 합니다.
  43. 잔차 학습 블록 [〈Deep Residual Learning for Image Recognition〉](https://openaccess.thecvf.com/content_cvpr_2016/papers/He_Deep_Residual_Learning_CVPR_2016_paper.pdf)
      , Kaiming He, Xiangyu Zhang, Shaoqing Ren, Jian Sun, 2015

## 107 page     
  44. ResNet의 구조(Architecture) :〈Deep Residual Learning for Image Recognition〉, Kaiming He, Xiangyu Zhang, Shaoqing Ren, Jian Sun, 2015,

## 109 page     
  45. 숏컷의 역할을 알아보는 테스트 : 〈Deep Residual Learning for Image Recognition〉, Kaiming He, Xiangyu Zhang, Shaoqing Ren, Jian Sun, 2015,

## 110 page     
  46. ILSVRC의 ResNet(2015년) [그림 참조](https://youtu.be/DAOcjicFr1Y)









