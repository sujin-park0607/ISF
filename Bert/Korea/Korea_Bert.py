from transformers import BertTokenizer, BertForSequenceClassification
from torch.utils.data import DataLoader
from transformers import AdamW
import pandas as pd
import os
import torch
import torch.nn as nn
from torch.nn import CrossEntropyLoss
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix, roc_auc_score, classification_report
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
from tqdm import tqdm
import json
from collections import OrderedDict
from datetime import datetime
import logging
logging.basicConfig(level=logging.INFO, format='%(message)s')

# huggingface，wordpiece
tokenizer = BertTokenizer.from_pretrained("kykim/bert-kor-base")

### Read Data
def read_data(file):
    texts = []
    labels = []
    data = pd.read_excel(file, engine='openpyxl')
    for row in data.itertuples():
        label = getattr(row, 'label')
        review = str(getattr(row, 'review'))[1:-1]
        texts.append(review)
        labels.append(label)
    assert len(texts) == len(labels)
    return texts, labels

texts, labels = read_data('Ko.xlsx')
###  traindata, testdata
train_texts, val_texts, train_labels, val_labels = train_test_split(
    texts, labels, test_size=0.2, random_state=43, stratify=labels)

###  Max length
max_len = max([len(item) for item in train_texts])
print(max_len)

max_len = max([len(item) for item in val_texts])
print(max_len)

### mapping
label2id = OrderedDict({item: idx for idx, item in enumerate(set(train_labels + val_labels))})
id2label = OrderedDict({v: k for k, v in label2id.items()})

# 
train_encodings = tokenizer(train_texts,
                            truncation=True,
                            padding=True,
                            max_length=128)
val_encodings = tokenizer(val_texts,
                          truncation=True,
                          padding=True,
                          max_length=128)


# PyTorch Dataset  Create Dataset
class CuDataset(torch.utils.data.Dataset):
    def __init__(self, encodings, labels):
        self.encodings = encodings
        self.labels = labels

    def __getitem__(self, idx):
        idx = int(idx)
        item = {
            key: torch.tensor(val[idx])
            for key, val in self.encodings.items()
        }
        item['labels'] = torch.tensor(label2id[self.labels[idx]])
        return item

    def __len__(self):
        return len(self.labels)

train_dataset = CuDataset(train_encodings, train_labels)
val_dataset = CuDataset(val_encodings, val_labels)

#  Create Dataloader
batch_size = 64
train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
eval_loader = DataLoader(val_dataset, batch_size=batch_size, shuffle=False)

device = torch.device('cuda:0') if torch.cuda.is_available() else torch.device(
    'cpu')  # Use GPU
model = BertForSequenceClassification.from_pretrained(
    "kykim/bert-kor-base", num_labels=len(label2id)) #Initial state: random ,Adjusting parameters to learn
model.to(device)
model.train()

### 计算Accuracy，Precision，Recall，F1 score，confusion_matrix，classification_report
def compute_metrics(labels, preds):
    accuracy = accuracy_score(labels, preds)
    precision = precision_score(labels, preds)
    recall = recall_score(labels, preds)
    f1 = f1_score(labels, preds)
    print(f'accuracy: {accuracy}\n')
    print(f'precision: {precision}\n')
    print(f'recall: {recall}\n')
    print(f'f1: {f1}\n')
    print(confusion_matrix(labels, preds))
    print(classification_report(labels, preds))
    return f1

###eval_model
@torch.no_grad()
def eval_model(model, eval_loader):
    model.eval()
    labels = []
    preds = []
    for idx, batch in enumerate(eval_loader):
        input_ids = batch['input_ids'].to(device)
        attention_mask = batch['attention_mask'].to(device)
        labels.extend(batch['labels'].numpy())
        outputs = model(input_ids,attention_mask=attention_mask)  # All probabilities
        preds.extend(torch.argmax(outputs[0], dim=-1).cpu().numpy()) 
    f1 = compute_metrics(labels, preds)
    model.train()
    return f1

###Train models
optim = AdamW(model.parameters(), lr=1e-5)  # Optimization
step = 0
best_f1 = 0
epoch = 10
for epoch in range(epoch):
    for idx, batch in tqdm(enumerate(train_loader),
                           total=len(train_texts) // batch_size):
        optim.zero_grad()
        input_ids = batch['input_ids'].to(device)
        labels = batch['labels'].to(device)
        attention_mask = batch['attention_mask'].to(device)
        outputs = model(input_ids=input_ids, labels=labels, attention_mask=attention_mask)
        loss = outputs[0]  # 计算Loss
        logging.info(
            f'Epoch-{epoch}, Step-{step}, Loss: {loss.cpu().detach().numpy()}')
        step += 1
        loss.backward()
        optim.step()

    print(f'Epoch {epoch}, start evaluating.')
    f1 = eval_model(model, eval_loader)  # evaluation Model
    if f1 > best_f1:
        print(f'best_f1: {f1}')
        model.save_pretrained('model_best')  
        tokenizer.save_pretrained('model_best')
        best_f1 = f1
### Predict
def predict(model, tokenizer, text):
    encoding = tokenizer(text,
                         return_tensors="pt",
                         max_length=128,
                         truncation=True,
                         padding=True)
    encoding = {k:v.to(device) for  k,v in encoding.items()}
    outputs = model(**encoding)
    #pred = id2label[torch.argmax(outputs[0], dim=-1).numpy()[0]]
    pred = id2label[torch.argmax(outputs[0], dim=-1).cpu().detach().numpy()[0]]
    return pred

tokenizer = BertTokenizer.from_pretrained("model_best")
model = BertForSequenceClassification.from_pretrained(
    "model_best", num_labels=len(label2id))
model.to(device)    

import numpy as np
result_dict = {}
for root, dirs, files in os.walk('test', topdown=True):
    for name in files:
        all_preds = []
        print(f'process file: {name}')
        try:
            with open(os.path.join(root, name), 'r', encoding='utf8') as f:
                lines = f.readlines()
        except:
            with open(os.path.join(root, name), 'r', encoding='gb18030') as f:
                lines = f.readlines()
        for idx, line in enumerate(lines):
            line = line.strip()
            if not line:
                continue
            text = line
            pred=predict(model,tokenizer,line)
            all_preds.append(pred)
        base_name_date = '-'.join([os.path.basename(name)[4:6], os.path.basename(name)[6:8]])
        result_dict[datetime.strptime(base_name_date, "%m-%d")] = [
            sum(all_preds), len(all_preds)]
result_dict = sorted(result_dict.items(), key=lambda x: x[0])
np.save('result_dict_XKo.npy', result_dict)