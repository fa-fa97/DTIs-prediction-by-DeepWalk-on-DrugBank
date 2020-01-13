#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon May  6 23:30:40 2019

@author: fatemehf
"""

import pandas as pd 
import random

db=pd.read_csv(r'~/Desktop/d/protein_df.csv')   
drugDB=db[['drugbank_id','uniprot_id']]


drugDB['drug_id'] = drugDB.groupby(['drugbank_id']).ngroup()
drugDB['target_id'] = drugDB.groupby(['uniprot_id']).ngroup()


###Convert dataset to edgelist and adjaency matrix 

data = pd.read_csv('~/Desktop/d/drugbank_unique.csv')

edj_data = data[['drug_id', 'target_id']]

drug_num = len(edj_data['drug_id'].unique())

edj_data['target_id'] += drug_num


num_edj=len(edj_data)
adj =edj_data.groupby('drug_id')['target_id'].apply(list)

adj.to_csv('~/Desktop/d/drug_adj.csv',sep=',')

### first implementation       

while(True):
    a=[random.randint(0,7722),random.randint(7722,12648)]
    b=True
    for i in range(len(edj_data)):
        if(list(edj_data.iloc[i])==a):
            b=False
            break
    if(b):
        edj_data=edj_data.append(pd.DataFrame([a],columns=['drug_id','target_id']))
        print(len(edj_data),"lenght is")        
    if len(edj_data)>=num_edj+3000:
        break
edj_data.to_csv('~/Desktop/d/drug_edj_negetive_positive.csv',sep=',')

### second implementation 

neg_and_pos_edj = pd.read_csv(r'Desktop/d/drug_edj_negetive_positive.csv')
num_edj_neg=len(neg_and_pos_edj)
while(True):
    a=[random.randint(0,7722),random.randint(7722,12648)]
    b=True
    for i in range(len(neg_and_pos_edj)):
        if(list(neg_and_pos_edj.iloc[i])==a):
            b=False
            break
    if(b):
        neg_and_pos_edj= neg_and_pos_edj.append(pd.DataFrame([a],columns=['drug_id','target_id']))
        print("lenght is:",len(neg_and_pos_edj))        
    if len(neg_and_pos_edj)>=num_edj_neg+3000:
        break

neg_and_pos_edj.to_csv('drug_edj_negetive_positive.csv',sep=',',index=False)

### add label column to datafram

data = pd.read_csv(r'~/Desktop/d/drug_edj_negetive_positive.csv')
data['label'] = 1
for i , row in data.iterrows():
    if i > 26391 :
        data.iloc[i]['label'] = -1

data.to_csv(r'~/Desktop/d/drug_edj_negetive_positive.csv',sep=',',index=False)



