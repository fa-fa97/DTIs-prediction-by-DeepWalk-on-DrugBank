#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu May 16 18:15:03 2019

@author: fatemehf
"""

import pandas as pd


data = pd.read_csv(r'~/Desktop/d/drug_edj_negetive_positive.csv')


column = ['F'+str(i) for i in range(1,65)]

column.insert(0,'node_id')

embedding=pd.read_csv(r'~/Desktop/d/drug_target_embedding.csv',names=column,dtype='a')

for i in range(1,65):
    embedding['F'+str(i)] = embedding['F'+str(i)].apply(lambda x : float(x))
    
    
embedding['node_id'] = embedding['node_id'].apply(lambda x : float(x))

cols = ['F'+str(i) for i in range(1,65)]    
cols.insert(0,'drug_id')
cols.insert(1,'target_id')
cols.insert(2,'label')
dataset_add =  pd.DataFrame(columns=cols,data=None) 



for i,row in data.iterrows():
    label=row['label']
    target_vector = embedding.loc[embedding['node_id'] == row['target_id']]
    target_vector = target_vector.reset_index(drop=True)
    drug_vector = embedding.loc[embedding['node_id'] == row['drug_id']]
    drug_vector = drug_vector.reset_index(drop=True)
    
    dataset_vector = drug_vector.add(target_vector)
    
    dataset_vector= dataset_vector.drop(columns = ['node_id'])
    dataset_vector['label'] = label
    dataset_vector['drug_id'] = drug_vector['node_id']
    dataset_vector['target_id'] = target_vector['node_id']
    
    print(i)
    
    dataset_add= dataset_add.append(dataset_vector,ignore_index=True)

dataset_add.to_csv('~/Desktop/d/dataset_add.csv',index=False)  
    
    
    
    
    
    
    
    
