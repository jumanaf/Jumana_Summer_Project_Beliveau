#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 10:58:35 2020

@author: Jumana
"""
from calc_prob import prob
import random
import csv

#creating random seed as control for statistical tests

#create 54, 634 random samples total, each 17 nt long, run 100 times (then 1000 times)
list_final = []
with open('chr1.fa', 'r') as file:
    chr1 = file.read().replace('\n', '')
for i in range(90, 100, 1):
    for j in range(0, 54634, 1):
        #take random seed from chr1
        st = random.randint(0, len(chr1))
        #take end 17 nt from there
        end = st + 17
        #calculate prob
        while ("N" in chr1[st:end] or ">chr1" in chr1[st:end] or "n" in chr1[st:end]):
            st = random.randint(0, len(chr1))
            end = st + 17
        specific_seq = chr1[st:end]
        structure = "."*17
        print(specific_seq)
        result = prob(specific_seq, structure, 37, 0, 0.157, 'dna1998')
        list_final.append([result, specific_seq, st, end, len(specific_seq)])
        
        
    with open("chr1_seed_{}.csv".format(i), "w", newline="") as f:
       writer = csv.writer(f)
       writer.writerows(list_final)
