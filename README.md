# 

도쿄 올림픽 기사분석과 정서분석을 통해 올림픽 유치 관련 인식 조사 
-----
(2021 도쿄 올림픽 관련  인식 조사와 관련하여 데이터 수집 및 데이터 분석)<br>


**목차**<br>
---

1. 데이터수집
2. 키워드 및 언급량 추출
3. 댓글 데이터 긍.부정 감성분석
4. 프로젝트 결과




**1. 데이터 수집** <br>
---
: 도쿄올림픽 이슈 및 인식을 수집하기 위해 국가별 대표 사이트를 선정하여 웹 크롤러 프로그램 제작

* 기간 : 6/23 ~ 8/21 (총 60일)
* 키워드 : "도쿄올림픽" 
* 사이트 : 네이버
* 수집 데이터 : 1,395,654
* 수집 데이터 필드 : 내용, 
* 수집 결과

<img width="50%" src="https://user-images.githubusercontent.com/75667075/176170797-47d850f8-c152-42e5-b1e7-62c541823f07.png"/>     <img width="50%" src="https://user-images.githubusercontent.com/75667075/176170898-7cc18e6b-15f4-41ac-8059-6ac45a2a6949.png"/>

   
   
   
   
2.키워드 및 언급량 추출 <br>
---
: 수집한 기사 데이터셋의 형태소를 분석하여 추출된 단어들에 대한 주요 키워드와 언급량 추출


   2-1. 데이터 전처리
      * 형태소 분석 후 형용사, 명사만 추출 
      * 한국어 형태소 분석기 Mecab 사용
  2-2. 결과
      * 키워드 조사
      
|키워드|언급량|
|---|---|
|선수|83653|
|경기|54737|
|한국|53742|
|대표|47786|
|팀|41019|
|여자|38386|
|대회|31099|
|금메달|29450|
|남자|29105|
<br>
      
      
* 결과 그래프

<img width="50%" src="https://user-images.githubusercontent.com/75667075/176162644-0e1b994a-9513-4b6c-a727-d5f3d3eb03f3.png"/><img width="50%" src="https://user-images.githubusercontent.com/75667075/176164420-32d4973a-5ff8-4847-9201-03c36842f103.png"/>

      
      
      
      
3.댓글 데이터 긍.부정 감성분석<br>
---
: Accuary: 87.6%

   
   3-1 레이블링
   : 긍정 1, 부정 0 으로 분류하여 전체 약 130만개의 데이터 중 5만개의 데이터 레이블링 작업 진행
   <img width="500" src="https://user-images.githubusercontent.com/75667075/176162925-9767f74a-320a-410a-b467-b54486b0c92c.png"/>

   
   3-2 딥러닝을 이용한 학습
   :fastText, Bert를 활용하여 모델 형성
   
   <img width="200" src="https://user-images.githubusercontent.com/75667075/176170456-a6a76f0b-572e-48d4-9fba-fc6b7ce1bf56.png"/><img width="200" src="https://user-images.githubusercontent.com/75667075/176170701-df290ba7-1720-42f6-9756-9f6a61b8bf48.png"/>

   3-3 결과
   
   [상단- 긍정, 하단- 부정]
   <p align="left"><img width="80%" src="https://user-images.githubusercontent.com/75667075/176164592-b6427b08-f89f-4332-96eb-e5346ad04070.png"/>

   [긍정, 부정이 가장 높은 Top-5 핵심 키워드 추출]
   <p align="left"><img width="80%" src="https://user-images.githubusercontent.com/75667075/176164675-e9625f9c-e685-4f82-af4f-4aade7fca9f0.png"/>
   
   *긍정
   |날짜| 키워드| 
   |---|---|
   |7/29 | 선수, 한국, 경기, 여자|
   |7/31 | 선수, 한국, 경기, 여자|
   |8/3 | 선수,한국, 여자, 경기|
   |8/5 | 선수, 한국, 경기, 대표|
   |8/7 | 선수, 여자, 안산, 양궁|
   
   *부정
   
   |날짜| 키워드|
   |---|---|
   |7/10 | 선수, 경기, 대표, 팀| 
   |7/11 | 회담, 정상, 정부, 대통령|
   |7/14 |  코로나, 서울, 확진, 대통령|
   |7/18 | 코로나, 대통령, 정부, 선수|
   |7/22 | 대통령, 코로나, 선수, 정부|
   
   
   
   
**4. 프로젝트 결과**<br>
---
: [ISF] 2021 데이터로 본 국제스포츠 결과물

<p align="center"><img width="65%" src="https://user-images.githubusercontent.com/75667075/176165452-68656a22-b4be-4927-8a88-ca51279783bc.png"/>

