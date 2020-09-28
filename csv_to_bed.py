#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 12:22:46 2020

@author: Jumana
"""
import pandas as pd

#start off by writing code to turn it into a TSV
result = pd.read_csv("chr1_enhancer_prob.csv", names = ["prob", "sequence", "seq id", "partial length", "whole length"])
start=[]
end=[]

res = []

for seqId in result['seq id']:
    seq_name = seqId[0:4]
    seq_start = (seqId.split(':'))[1].split('-')[0]
    seq_end = seqId.split('-', 1)[1]
    if int(seq_start) not in (pd.DataFrame(start)).values: #returns true if the element is present
        start.append([int(seq_start)])
        if int(seq_end) not in (pd.DataFrame(end)).values:
            end.append([int(seq_end)])
            res.append([seq_name, seq_start, seq_end])
    
df_res = pd.DataFrame(res)

df_res.to_csv('chr1_enhancer_prob.bed', sep = '\t', index = False, header = False)



