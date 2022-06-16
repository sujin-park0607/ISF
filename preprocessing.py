# from nltk.corpus import stopwords 
# from nltk.tokenize import word_tokenize 
import os
import nltk
import csv
import json

csv.field_size_limit(100000000)
stop_words = set(nltk.corpus.stopwords.words('english')) 
stop_words.add('olympics')
stop_words.add('olympic')
stop_words.add('games')
stop_words.add('game')
stop_words.add('tokyo')
stop_words.add('japan')
wordnet =  nltk.stem.WordNetLemmatizer()

def read_news_conents_from_csv(file_path):
    contents = []
    with open(file_path,'r',encoding='utf-8') as f:
        rdr = csv.reader(f)
        for row in rdr:
            contents.append(row[1])

    return contents    


def exclude_stop_words(word_tokens):

    result = []
    if type(word_tokens) == list:    
        
        for w in word_tokens: 
            if w not in stop_words and w.isalnum():
                result.append(w) 
    else:
        raise Exception("Please input \'list\' type")

    return result    


def get_keywords_from_content(contents):
    keywords = []

    for content in contents:
        word_tokens = nltk.tokenize.word_tokenize(content)
        lower_word_tokens = [word.lower() for word in word_tokens]
        word_filtered = exclude_stop_words(lower_word_tokens)
        

        tagged  = nltk.pos_tag(word_filtered)

        for word, tag in tagged:
            if tag.startswith('NN'):
                keywords.append(wordnet.lemmatize(word, 'n'))
    return keywords


if __name__ == "__main__":
    path = 'csv/news'
    file_names = os.listdir(path) #csv/news 폴더의 전체 파일명
    '''
       날짜 0622,0723,0823,0822 list에서 제외
    '''
    file_names.remove('20210622.csv')
    # file_names.remove('20210723.csv')
    file_names.remove('20210822.csv')
    file_names.remove('20210823.csv')


    file_names.sort()

    en_json = {}

    for file_name in file_names:
        
        daily_contents = read_news_conents_from_csv(os.path.join(path,file_name))

        daily_contents_keyword = get_keywords_from_content(daily_contents)
        

        date = file_name.split('.')[0]
        en_json[date] = daily_contents_keyword

        
    with open('en.json', 'w') as outfile:
        json.dump(en_json, outfile)

        
        
        

    
    