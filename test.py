from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 

# example = "Family is not an important thing. It's everything."
# stop_words = set(stopwords.words('english')) 

# word_tokens = word_tokenize(example)

# result = []
# for w in word_tokens: 
#     if w not in stop_words: 
#         result.append(w) 

# print(word_tokens) 
# print(result) 


'''
pos_tag : 품사태깅
'''

# from nltk import pos_tag
# from nltk import RegexpParser
# text ="learn php from guru99 make and hello study easy".split()
# print("After Split:",text)
# tokens_tag = pos_tag(text)
# print("After Token:",tokens_tag)
# patterns= """mychunk:{<JJ.?>?<NN.?>?}"""
# chunker = RegexpParser(patterns)
# print("After Regex:",chunker)
# output = chunker.parse(tokens_tag)
# print("After Chunking",output)


# from nltk.stem import WordNetLemmatizer,PorterStemmer

# st1 = WordNetLemmatizer()
# str2 = PorterStemmer()

# words=['times','olympic','peoples','years']
# print([st1.lemmatize(w, 'n') for w in words])
# print([str2.stem(w) for w in words])

import matplotlib.pyplot as plt
import numpy as np

# x = np.arange(3)
# years = ['2018', '2019', '2020']
# values = [100, 400, 900]

# plt.bar(x, values)
# plt.xticks(x, years)
# plt.show()

# # 한 주의 요일(0: 일, 1: 월 ~ 6: 토)
# days = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
# # 내가 사용한 돈(천원)
# money_spent = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
# # 친구가 사용한 돈(천원)
# money_spent_2 = [11, 14, 15, 15, 22, 21, 12]
# # 내가 사용한 돈을 그래프로 그립니다
# plt.plot(days, money_spent)
# # 같은 그림에 친구가 사용한 돈도 그래프로 그립니다
# # plt.plot(days, money_spent_2)
# # 화면에 그래프를 보여줍니다
# plt.show()

import argparse


parser = argparse.ArgumentParser()

parser.add_argument('--folder',required=True)
args = parser.parse_args()
