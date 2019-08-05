gencode =   {'AUA':'I', 'AUC':'I', 'AUU':'I', 'AUG':'M',
    'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACU':'T',
    'AAC':'N', 'AAU':'N', 'AAA':'K', 'AAG':'K',
    'AGC':'S', 'AGU':'S', 'AGA':'R', 'AGG':'R',
    'CUA':'L', 'CUC':'L', 'CUG':'L', 'CUU':'L',
    'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCU':'P',
    'CAC':'H', 'CAU':'H', 'CAA':'Q', 'CAG':'Q',
    'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGU':'R',
    'GUA':'V', 'GUC':'V', 'GUG':'V', 'GUU':'V',
    'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCU':'A',
    'GAC':'D', 'GAU':'D', 'GAA':'E', 'GAG':'E',
    'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGU':'G',
    'UCA':'S', 'UCC':'S', 'UCG':'S', 'UCU':'S',
    'UUC':'F', 'UUU':'F', 'UUA':'L', 'UUG':'L',
    'UAC':'Y', 'UAU':'Y', 'UAA':'_', 'UAG':'_',
    'UGC':'C', 'UGU':'C', 'UGA':'_', 'UGG':'W'}

file = input('insert dna file name/path to dna file ')
print('file name: ' + file)

dna_file = open(file).read().rstrip('\n').upper()

dna_comp = dna_file.replace('A','u')
dna_comp1 = dna_comp.replace('T','a')
dna_comp2 = dna_comp1.replace('G','c')
dna_comp3 = dna_comp2.replace('C','g')
rna_seq = dna_comp3.upper()

last_codon_start = len(rna_seq) - 2

protein = ''

for start in range(0,last_codon_start,3):
    codon = rna_seq[start:start+3]
    amino_acid = gencode.get(codon,'X')
    protein += amino_acid

rna_file = open(file + '_rna.txt','w')
rna_file.write(rna_seq)
rna_file.close()

protein_file = open(file + '_protein.txt','w')
protein_file.write(protein)
protein_file.close()
