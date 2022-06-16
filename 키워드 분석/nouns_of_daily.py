# Mecab 형태소 분석기
from eunjeon import Mecab

import os, csv
from collections import Counter

import nltk, re
nltk.download('punkt')

mecab = Mecab()
 
path_dir = 'C:/Users/acin/isf/news'
 
file_list = os.listdir(path_dir)

csv_dict = {}

for filename in file_list:
    with open(f'/Users/acin/isf/news/{filename}', 'r', encoding='UTF-8-sig') as f:
        reader = csv.reader(f)
        lst = [line for line in reader]

        csv_dict[filename.split(".")[0]] = []

        for row in lst[1:]:
            temp_dict = {}

            for idx in range(len(lst[0])):
                temp_dict[lst[0][idx]] = row[idx]

            csv_dict[filename.split(".")[0]].append( temp_dict )


# print(csv_dict)
# 명사 top 몇 개 할 지 설정
top = 10

# 한글 불용어 리스트 불러오기 시작
stopwords = []
with open('한글불용어.txt', 'r', encoding='utf8') as f:
    stopwords = f.read().split('\n')
# 한글 불용어 리스트 불러오기 끝


result_list = []

for daily, v in csv_dict.items():
    # print(daily,v)
    # break

    # 일당 기사의 본문을 하나로 합침 시작
    daily_article = ""
    for article in v:
        daily_article += article['Article']
        # 일당 기사의 본문을 하나로 합침 끝

    print(daily_article)
    print("="*100)
    # 불용어 제거 코드 시작
    clean_words = [] 
    for word in nltk.tokenize.word_tokenize(daily_article): 
        if word not in stopwords: #불용어 제거
            clean_words.append(word)
    # 불용어 제거 코드 끝


    # 명사 top 10개 추출 코드 시작
    result = mecab.nouns(" ".join(clean_words))
    count = Counter(result)
    top_nouns = count.most_common(top)
    # 명사 top 10개 추출 코드 끝

    # i[0] → 명사      i[1] → 개수
    print(f"{daily} : { [i[0] for i in top_nouns] }")
    result_list.append(f"{daily},{[i[0] for i in top_nouns]}" )

with open("top_nouns.txt", "w", encoding="utf8") as f:
    for row in result_list:
        f.write(row+"\n")