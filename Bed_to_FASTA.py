import pybedtools
from pybedtools import BedTool
mouse_bed = pybedtools.BedTool('F5.mm10.enhancers.bed')
for i in range (1, 20, 1):
    mouse_fasta = pybedtools.BedTool('chr{}.fa'.format(i))
    mouse_enhancer_fasta = mouse_bed.sequence(fi=mouse_fasta)
    save_fasta = mouse_enhancer_fasta.save_seqs('chr{}_enhancer.fa'.format(i))

mouse_fasta_x = pybedtools.BedTool('chrX.fa')
mouse_enhancer_x_fasta = mouse_bed.sequence(fi=mouse_fasta)
save_fasta_x = mouse_enhancer_fasta.save_seqs('chrX_enhancer.fa')

mouse_fasta_y = pybedtools.BedTool('chrY.fa')
mouse_enhancer_y_fasta = mouse_bed.sequence(fi=mouse_fasta)
save_fasta_y = mouse_enhancer_fasta.save_seqs('chrY_enhancer.fa')