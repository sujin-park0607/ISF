# 

도쿄 올림픽 국가별 관련 기사분석과 정서분석을 통해 올림픽 유치 관련 인식 조사 
----------------------------------------------------------------------------

(2021 도쿄 올림픽 관련 국내외 (한.중.미) 인식 조사와 관련하여 데이터 수집 및 데이터 분석)<br>
---

**목차**<br>
---

1. 데이터수집
2. 데이터 전처리
3. 데이터 학습
4. 데이터 분석
5. 결과

**1. 데이터 수집** <br>
---
: 도쿄올림픽 이슈 및 인식을 수집하기 위해 국가별 대표 사이트를 선정하여 웹 크롤러 프로그램 제작

* 기간 : 6/23 ~ 8/21 (총 60일)
* 키워드 : "도쿄올림픽" 
* 사이트 : 네이버
* 수집 데이터 : 1,395,654
* 수집 데이터 필드

   | content | Date |
   |---|---|
   | 내용 | 날짜 |
  
* 수집 결과

   ![image](https://user-images.githubusercontent.com/75667075/176151348-cfc3e12a-35e4-4e5e-8579-7abd12a0077d.png)
   ![image](https://user-images.githubusercontent.com/75667075/176151367-3cf6a5aa-553f-4307-8a61-97871feb4dea.png)


**2.키워드 및 언급량 추출 **<br>
---
: 수집한 기사 데이터셋의 형태소를 분석하여 추출된 단어들에 대한 주요 키워드와 언급량 추출
   Ⅰ. 데이터 전처리 : 형태소 분석을 통하여 명사, 형용사로만 추출 
      * 
      * 
   Ⅱ. 수집된 기사 데이터셋을 활용하여 Top-9 키워드 조사 
   

Ⅰ. nouns_of_daily.py -> 불용어 처리 및 top 10 추출<br>
   <img src= "https://user-images.githubusercontent.com/87688936/169702159-6ddd80be-289b-4828-82d2-95ce2d6c66ae.png" width="200" height="200"><br>
Ⅱ.count_reply.c -> 날짜 별로 3국 각각 댓글 수 합계를 구하여, 어떤 날 제일 댓글이 활발했는지 체크<br>


**3.댓글 데이터 학습**<br>
---
: fastText, Bert 모델을 사용하여 긍.부정 분석

   1. 레이블링
**3. 데이터 그래프화**<br>

Ⅰ. 올림픽 개최 전후 10일간 일별 top1 키워드 빈도수 체크 -> 올림픽 전후 키워드 빈도수 그래프 추출<br>
<img src= "https://user-images.githubusercontent.com/87688936/169703367-45380860-8b6e-499f-8cd7-4c307a1898ad.png" width="300"><br>
Ⅱ. 올림픽 개최 전 후 30일간 top5 키워드에 대한 일별 키워드 빈도수 체크 -> top5 키워드에 대한 일별 키워드 빈도수 체크 그래프 추출<br>
<img src= "https://user-images.githubusercontent.com/87688936/169703385-65e39ad2-b770-491e-96be-6571a5ad3208.png" width="300"><br>
Ⅲ. 올림픽 개최 전 후 30일간 top5 키워드에 대한 주별 키워드 빈도수 체크 -> top5 키워드에 대한 주별 키워드 빈도수 체크 그래프 추출<br>
<img src= "https://user-images.githubusercontent.com/87688936/169703400-f2a2c0ac-a222-4212-bed9-052493423cee.png" width="300"><br>
Ⅳ. 본문 속 단어 빈도수 체크 -> 3국 키워드 wordcloud 추출<br>
<img src= "https://user-images.githubusercontent.com/87688936/169703414-4175ef0d-213f-41d8-9606-8aa1dd7ba2cb.png" width="300"><br>

**4. 감성 분석 (BERT, FASTTEXT)**

Ⅰ. 댓글 데이터 레이블링 



※ 데이터 범위
 7/23일 올림픽 개최일 기준 한달 전/후 6/23~8/21일 <br>
※ 데이터 필드 목록<br>
<img src= "https://user-images.githubusercontent.com/87688936/169702096-172b50d6-1ac5-4df1-a3ff-d134b981f459.png" width="300"><br>
※ 수집 결과 <br>
한국 : 1,395,654개 <br>
