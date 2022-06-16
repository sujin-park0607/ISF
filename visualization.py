import json
import os
from wordcloud import WordCloud
from collections import Counter
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rc
import matplotlib.ticker as ticker
from ftfy import fix_text
import bigjson


import argparse

parser = argparse.ArgumentParser()

parser.add_argument('--lang',required=True,help='natural language for analysis')
parser.add_argument('--path',required=True,help='data for analysis')
parser.add_argument('--wordcloud',required=False,default=False,help='draw wordcloud')
parser.add_argument('--bar-graph',required=False,default=False,help='draw bar graph')
parser.add_argument('--daily-line-graph',required=False,default=False,help='draw daily line graph')
parser.add_argument('--weekly-line-graph',required=False,default=False,help='draw weekly line graph')

args = parser.parse_args()

wordcloud_font_path = None

if args.lang == 'ko':
    #matplotlib 한글깨짐 문제 
    rc('font', family='AppleGothic')
    plt.rcParams['axes.unicode_minus'] = False

    #wordcloud 한글깨짐 문제
    wordcloud_font_path = '/Library/Fonts/AppleGothic.ttf'

if args.lang == 'ch':
    #matplotlib 중국어깨짐 문제
    plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']

    #wordcloud 중국어깨짐 문제
    wordcloud_font_path = '/Library/Fonts/Songti.ttc'


def read_json(path,mode,encoding):
    json_data = None
    with open(path,mode=mode,encoding=encoding) as json_file:
        # if mode == "rb":
        # json_data = bigjson.loads(json_file)
        # else:
        json_data = json.loads(json_file.read())
        
    return json_data


def generate_wordcloud(json_data):
    keywords = []
    # stopwords=['개','조','내']
    for key,value in json_data.items():
        keywords.extend(value)

    counter = Counter(keywords)
    tags = counter.most_common(60)
    # tags = [tag[] for tag in tags]
    print(tags)
    # for i,tag in enumerate(tags):
        
    #     if tag[0] in stopwords:
    #         del tags[i]

    wc = WordCloud(background_color="white", max_font_size=60,font_path=wordcloud_font_path)

    cloud = wc.generate_from_frequencies(dict(tags))
    cloud.to_file('wordcloud.jpg')

def get_top_keyword(json_data,date_range=('20210623','20210821'),top=10):
    '''
        날짜 범위에 해당하는 top 키워드 추출
        Args
            json_data: json_data ex){"20210623":[keyword1,keyword2....]}
            date_range: top키워드 추출 날짜범위 ex)20210623 ~ 20210821이면 다음형태로 ('20210623','20210821')
            top: top 몇 키워드 추출할것인지 
        Returns
            키워드와 키워드 빈도수를 빈도수가 많은것순으로 정렬되어 반환
            ex)((keyword1,5),(keyword2, 3))
    '''
    
    #keywords = []
    keywords = []
    json_data_filtered = {}
    for date in pd.date_range(start=date_range[0],end=date_range[1]):

        '''
         json_data에서 날짜 범위에 있는 데이터만 필터링
        '''
        date = str(date.date()).replace('-','')
        if date in json_data:
            json_data_filtered.update({date:json_data[date]})

    for key,value in json_data_filtered.items():
        keywords.extend(value)
    
    # print(keywords)
    
    counter = Counter(keywords)
    
    tags = counter.most_common(top)

    # print("tags: ",tags)

    return tags
    
def list_chunk(lst, n):
    return [lst[i:i+n] for i in range(0, len(lst), n)]
def draw_bar_graph(json_data):
    '''
        올림픽 전후 키워드 각각 10개 추출해서 막대 그래프
        x축이 키워드, y축이 키워드빈도수
    '''
    
    before_date_range = ('20210623','20210722')
    after_date_range = ('20210724','20210821')

    #올림픽 전 top키워드
    before_top10_keywords = get_top_keyword(json_data=json_data,date_range=before_date_range)
    #올림픽 후 top키워드
    after_top10_keywords  = get_top_keyword(json_data=json_data,date_range=after_date_range)

    #x축은 올림픽 전 top10 키워드
    before_x_axis = [tags[0] for tags in before_top10_keywords]
    before_x_axis.append('d-day')
    #y축은 올림픽 전 top10 키워드 빈도수
    before_y_axis = [tags[1] for tags in before_top10_keywords]
    before_y_axis.append(0)

    #x축은 올림픽 후 top10 키워드
    after_x_axis = [tags[0]+' ' for tags in after_top10_keywords]
    after_y_axis = [tags[1] for tags in after_top10_keywords]

    plt.title('올림픽 전후 키워드 빈도수', loc='center')
    plt.xlabel('키워드',labelpad=15)
    plt.ylabel('빈도수',labelpad=15)
    plt.bar(before_x_axis+after_x_axis, before_y_axis+after_y_axis,width=0.7)
    
    # plt.savefig('올림픽전후키워드빈도수.png')
    plt.show()



def draw_daily_line_graph(json_data):
    '''
    ['game', 'time', 'olympic', 'year', 'team']
    '''

    all_top5_keywords = [ keyword[0] for keyword in get_top_keyword(json_data=json_data, top=5)]
    
    
    date_range = ('20210623','20210821')
    x_axis = list(range(-30,30))
    y_axis = [[],[],[],[],[]]
    for date in pd.date_range(start=date_range[0],end=date_range[1]):

        date = str(date.date()).replace('-','')
        keywords = get_top_keyword(json_data=json_data,date_range=(date,date),top=10000000)
        keyword_filtered = [tag for tag in keywords if tag[0] in all_top5_keywords]

        # print(keyword_filtered)
        # x_axis.append(date[4:])
        # keyword_filtered_dict = dict(keyword_filtered)
        
        # print(f"{date}s:",keyword_filtered)
        rank_table = {keyword:0 for keyword in all_top5_keywords}
        

        for rank,tag in enumerate(keyword_filtered):
            if tag[0] in rank_table:
                rank_table[tag[0]] = tag[1]

        # print(f"{date}:",rank_table)
        for i in range(5):
            y_axis[i].append(rank_table[all_top5_keywords[i]])
        
    for i in range(len(y_axis)):
        print(f"y{i}: ",y_axis[i])
    
    #5개 선 그래프 그리기
    for i in range(5):
        print('hello')
        plt.plot(x_axis, y_axis[i])
    
    # plt.ylim([0,1])
    plt.legend(all_top5_keywords,loc=(1.0,0.5))
    plt.title('TOP5 키워드에대한 일별키워드 빈도수', loc='center')
    # plt.savefig('올림픽전후키워드빈도수.png')
    # plt.savefig('top5_일별키워드_빈도수.png')
    plt.show()
    

    

def draw_weekly_line_graph(json_data):
    all_top5_keywords = [ keyword[0] for keyword in get_top_keyword(json_data=json_data, top=5)]
    list_chunked = list_chunk(list(json_data.keys()),7)
    x_axis = []
    y_axis = [[],[],[],[],[]]

    for i in range(1,10):
        x_axis.append(f'{i}주')


    
    for date_list in list_chunked:
        # print("date: ",date_list)
        # print(date_list[0],date_list[-1])
        # print("="*100)
        keywords = get_top_keyword(json_data=json_data,top=10000000,date_range=(date_list[0],date_list[-1]))
        frequency_dict = {keyword:0 for keyword in all_top5_keywords}
        for keyword in keywords:
            if keyword[0] in frequency_dict:
                frequency_dict[keyword[0]] = keyword[1]
        for i,top_keyword in enumerate(all_top5_keywords):
            y_axis[i].append(frequency_dict[top_keyword])
        


    for i in range(5):
        # print('&'*100)
        # print(f'{i}: ',y_axis[i])
        plt.plot(x_axis, y_axis[i])
    
    # plt.ylim([0,1])
    plt.title('TOP5 키워드에대한 주별키워드 빈도수', loc='center')
    plt.legend(all_top5_keywords,loc=(1.0,0.5))
    # plt.savefig('top5_주별키워드_빈도수.png')
    plt.show()

    
if __name__ == '__main__':

    json_data = read_json(args.path,mode='r',encoding='utf-8')
    if args.wordcloud:
        generate_wordcloud(json_data)
    
    if args.bar_graph:
        draw_bar_graph(json_data)

    if args.daily_line_graph:
        draw_daily_line_graph(json_data)

    if args.weekly_line_graph:
        draw_weekly_line_graph(json_data)

    