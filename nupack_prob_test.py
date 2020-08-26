from calc_prob import prob
import pandas as pd
from Bio import SeqIO
import csv
import time

list_final = []

t0 = time.perf_counter()

for seq_record in SeqIO.parse("chr1_enhancer.fa", "fasta"):
    overall_seq = str(seq_record.seq.upper())
    i = 0
    #print(overall_seq)
    while(((i * 17)+17) < len(overall_seq)):
        specific_seq = overall_seq[i*17 : (i *17) + 17] #getting 17 letters at a time
        seq_id = seq_record.id
        #print(specific_seq)
        if(len(specific_seq) > 2):
            print(specific_seq)
            sequence_len_dots = (len(specific_seq))
            structure = "."*sequence_len_dots 
            #print(structure)
            #print(specific_seq)
            result = prob(specific_seq, structure, 37, 0, 0.157, 'dna1998')
            #result = 0
            print(result)
            list_final.append([result, specific_seq, seq_id, len(specific_seq), len(overall_seq)])
            i = i + 1

with open("chr1_enhancer_prob.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(list_final)


t1 = time.perf_counter()
print(t1-t0, "seconds process time")
