
import os
import json

import argparse


parser = argparse.ArgumentParser()

parser.add_argument('--folder',required=True,help="Change the file in the folder name to a json object")
parser.add_argument('--output',required=True,help="Created json file name")
args = parser.parse_args()


path = args.folder
json_data = {}
for file_names in os.listdir(path):
    with open(os.path.join(path,file_names),encoding='utf-8') as f:
        day = file_names.split(".")[1]
        if len(day) == 1:
            day ='0'+day

        name = f'20210{file_names.split(".")[0]}{day}'
        lines=[ line.replace('\n','').strip() for line in f.readlines()]
        json_data.update({name:lines})


#print(json_data)
with open(args.output,'w',encoding='utf-8') as f:
   f.write(json.dumps(json_data,ensure_ascii=False))