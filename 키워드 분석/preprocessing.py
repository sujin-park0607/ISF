from eunjeon import Mecab
import os, csv
from collections import Counter
import nltk, re
import json
import io

from nltk.data import load

mecab = Mecab()


def create_csv_dict(path):
    '''
        Returns
            csv_dict
                {
                    'date':[content1,content2,content3]，
                    'date':[content1,content2,content3]，
                }
    '''
    csv_dict = {}

    with open(path, 'r', encoding='UTF-8-sig') as f:
        reader = csv.reader(f)

        for row in reader:
            '''
             row
                [제목,날짜,내용]
            '''

            if ''.join(row) == '': #['','',''] 값없는 행이면
                continue 
            
            title, date, content = row
            #2021.06.22. 오후 11:24 to 20210622
            date_splited = date.split(' ')[0].replace('.','')
            print(f'process {date_splited}')
            if date_splited in csv_dict:
                csv_dict[date_splited].append(content)
            else:
                csv_dict[date_splited]=[content]
            

    return csv_dict

def load_stop_words(stop_words=[]):

    _stop_words =[]
    with open('한글불용어.txt', 'r', encoding='utf8') as f:
        _stop_words = f.read().split('\n')

    _stop_words.extend(stop_words)
    return _stop_words

def word_tokenization(csv_dict,stop_words=[]):
    '''
        Args
            csv_dict: {
                'date': [content1,content2]
            }
            stop_words: 불용어 리스트

        Returns
            {
                date: ['keyword1','keyword2'],
                date: ['keyword1','keyword2']
            }
    '''
    tokenized_words_dict = {}
    for date, contents in csv_dict.items():
        content = ' '.join(contents)
        tokenized_words = []

        print(f'tokenize {date}')
        for word in nltk.tokenize.word_tokenize(content):
            if word not in stop_words and word.isalnum(): #불용어 제거
                
                tokenized_words.append(word)

        tokenized_words_dict.update({date:tokenized_words})
        
        
    return tokenized_words_dict


if __name__ == "__main__":
    json_data = {}
    csv_dict = create_csv_dict('total_news.tsv')
    stop_words = load_stop_words()
    # print(stop_words)
    tokenized_words_dict = word_tokenization(csv_dict,stop_words)

    for date,keywords in tokenized_words_dict.items():
        print(f'Noun extraction {date}')
        results = mecab.nouns(" ".join(keywords))
        clean_words = []
        for word in results: 
            if word not in stop_words: #불용어 제거
                clean_words.append(word)
        json_data.update({date:clean_words})        
        
        
    with open('ko_b.json', 'wb') as f:
        f.write(json.dumps(json_data).encode("utf-8"))
        # json.dump(json_data,f)
    with open('ko.json','w',encoding="utf-8") as f:
        f.write(json.dumps(json_data,ensure_ascii=False))
