from Bio import SeqIO
import re
def gene_discontigous():
    handle = open('/Downloads/rosalind_splc (4).txt', 'r')
    seq = []
    for record in SeqIO.parse(handle, 'fasta'):
        seq.append(str(record.seq))                         # Extracts DNA sequences

    seqLength = len(seq)
    DNA = seq[0]                                            # Store main DNA string

    for intron in seq[1:seqLength]:                         # Iterating over all intron sequences and excluded
        DNA = DNA.replace(intron, '')                       # Replace intron with nothing and collect in DNA

    map = {
        'TTT': 'F', 'CTT': 'L', 'ATT': 'I', 'GTT': 'V',
        'TTC': 'F', 'CTC': 'L', 'ATC': 'I', 'GTC': 'V',
        'TTA': 'L', 'CTA': 'L', 'ATA': 'I', 'GTA': 'V',
        'TTG': 'L', 'CTG': 'L', 'ATG': 'M', 'GTG': 'V',
        'TCT': 'S', 'CCT': 'P', 'ACT': 'T', 'GCT': 'A',
        'TCC': 'S', 'CCC': 'P', 'ACC': 'T', 'GCC': 'A',
        'TCA': 'S', 'CCA': 'P', 'ACA': 'T', 'GCA': 'A',
        'TCG': 'S', 'CCG': 'P', 'ACG': 'T', 'GCG': 'A',
        'TAT': 'Y', 'CAT': 'H', 'AAT': 'N', 'GAT': 'D',
        'TAC': 'Y', 'CAC': 'H', 'AAC': 'N', 'GAC': 'D',
        'TAA': 'Stop', 'CAA': 'Q', 'AAA': 'K', 'GAA': 'E',
        'TAG': 'Stop', 'CAG': 'Q', 'AAG': 'K', 'GAG': 'E',
        'TGT': 'C', 'CGT': 'R', 'AGT': 'S', 'GGT': 'G',
        'TGC': 'C', 'CGC': 'R', 'AGC': 'S', 'GGC': 'G',
        'TGA': 'Stop', 'CGA': 'R', 'AGA': 'R', 'GGA': 'G',
        'TGG': 'W', 'CGG': 'R', 'AGG': 'R', 'GGG': 'G'
    }
    final = ''
    for i in range(0, len(DNA), 3):
        codon = DNA[i:i+3]
        final = final + map.get(codon)
    print(final)


gene_discontigous()

