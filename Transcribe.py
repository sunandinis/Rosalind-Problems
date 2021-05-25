def transcribe(dna):
    file=open(dna, 'r')
    dna=file.read()
    rna=''
    for nucleotide in dna:
        if nucleotide == 'T':
            rna = rna + 'U'
        else:
            rna = rna + nucleotide
    print(rna)

transcribe('/Users/dhruvarora/Downloads/rosalind_rna (2).txt')
