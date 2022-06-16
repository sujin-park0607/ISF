import pandas as pd
import glob
import os
input_file = r'csv/comments'
output_file ='csv/total_comments.tsv'

allFile_list = glob.glob(os.path.join(input_file, '2021*'))
print(allFile_list)
allData = []
for file in allFile_list:
    df = pd.read_csv(file)
    df = df.drop(['Unnamed: 0','Name','Recommend','Unrecommend'],axis=1)
    allData.append(df)


dataCombine = pd.concat(allData, axis=0, ignore_index=True)
dataCombine.to_csv(output_file, index = False, encoding='utf-8-sig')