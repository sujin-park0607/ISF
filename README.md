# ISF_국제스포츠 정보 현안 분석

도쿄 올림픽 국가별 관련 기사분석과 정서분석을 통해 올림픽 유치 관련 인식 조사 
---

(2021 도쿄 올림픽 관련 국내외 (한.중.미) 인식 조사와 관련하여 데이터 수집 및 데이터 분석)<br>
**1. 데이터 수집**<br>
*국가별 대표 사이트 데이터 수집<br>
*데이터 범위는 7/23 올림픽 개최 기준으로 한달 전후인 6/23~8/21 까지 총 60일 도쿄올림픽 키워드 댓글 데이터 수집<br>
*한국 1,395,654 / 중국 50,165/ 미국 19,822 개의 댓글 데이터 수집<br>

 .  | 한국 | 중국 | 미국
---
사이트 | 네이버 뉴스 | sina | 뉴욕타임즈 |
데이터 | 1,395,654 | 50,165 | 19,822|

한국 - 네이버 뉴스<br>
중국 - sina<br>
미국 - 뉴욕 타임즈<br>

**2.데이터 전처리**<br>
* 불용어 처리 및 본문 속 단어 빈도수 체크<br>

Ⅰ. nouns_of_daily.py -> 불용어 처리 및 top 10 추출<br>
   <img src= "https://user-images.githubusercontent.com/87688936/169702159-6ddd80be-289b-4828-82d2-95ce2d6c66ae.png" width="200" height="200"><br>
Ⅱ.count_reply.c -> 날짜 별로 3국 각각 댓글 수 합계를 구하여, 어떤 날 제일 댓글이 활발했는지 체크<br>

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
