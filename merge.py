import os
import json
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--path',required=True,help='Folder names of files for merging')
parser.add_argument('--output',required=True,help='Output file name')

args = parser.parse_args()

json_datas = {}

path = args.path
for file_name in os.listdir(path):
    with open(os.path.join(path,file_name)) as f:
        json_data = json.loads(f.read())
        json_datas.update({
            file_name.split('.')[0]: json_data
        })

with open(args.output,'w',encoding="utf-8") as f:
    f.write(json.dumps(json_datas,ensure_ascii=False,indent='\t'))