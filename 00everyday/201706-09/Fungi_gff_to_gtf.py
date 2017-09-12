#!/usr/bin/env python3import re, sys
gff_file = sys.argv[1]
GeneID2locustag_dict = {}locustag2ID_dict = {}GeneID2Genbank_dict = {}ID2Genbank_dict = {}Parent2Genbank_dict = {}ID2Parent_dict = {}Genbank2ID_dict = {}
def NCBIgffParse1(gff_file):    with open(gff_file) as gfffile:        for line in gfffile:            if line.startswith("#"):continue            else:                cols = line.strip().split("\t")                core_item = cols[8].split(";")                if cols[2] == "gene":                   GeneID = re.search(';Dbxref=GeneID:(\w+);', cols[8]).group(1)                   ID = re.search('ID=(\w+);', cols[8]).group(1)                   locus_tag = re.search(';locus_tag=(\w+)', cols[8]).group(1)                   GeneID2locustag_dict[GeneID] = locus_tag                   locustag2ID_dict[locus_tag] = ID                if cols[2] == "mRNA" or cols[2] == "ncRNA" or cols[2] == "rRNA" or cols[2] == "tRNA":                   ID = re.search('ID=(\w+);', cols[8]).group(1)                   Parent = re.search('Parent=(\w+);', cols[8]).group(1)                   ID2Parent_dict[ID] = Parent                if cols[2] == "mRNA" or cols[2] == "ncRNA" or cols[2] == "rRNA":                   ID = re.search('ID=(\w+);', cols[8]).group(1)                   Parent = re.search('Parent=(\w+);', cols[8]).group(1)                   Genbank = re.search('Genbank:([\w\.]+)', cols[8]).group(1)                   ID2Genbank_dict[ID] = Genbank                   Genbank2ID_dict[Genbank] =ID                   Parent2Genbank_dict[Parent] = Genbank                if cols[2] == "exon" or cols[2] == "CDS":
