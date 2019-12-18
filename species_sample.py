#!/usr/bin/python3

# Takes in stdout from unzipped maf sequences and outputs all sequences with homologs in all of the specified genomes below

import sys

genomes = ['mm9','bosTau4','canFam2','loxAfr3','macEug1','monDom5','ornAna1','galGal3','taeGut1','anoCar1','xenTro2','danRer6','tetNig2','fr2','gasAcu1','oryLat2']
conserved = []
sequences = sys.stdin.readlines()
total = ''.join(sequences)
indvs = total.split('s hg')[1:]
for i in indvs:
    t = 0
    for s in genomes:
        if s in i:
            t += 1
        else:
            break
    if t == len(genomes):
        conserved.append('s hg' + i)
        print(''.join(conserved))