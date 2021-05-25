from Bio import SeqIO
sequences = []
handle = open('/Users/Downloads/rosalind_tran (1).txt', 'r')
for record in SeqIO.parse(handle,'fasta'):
    sequences.append(str(record.seq))

seq1 = sequences[0]
seq2 = sequences[1]

AG = ['A', 'G']
CT = ['C', 'T']

transition_count = 0
transversion_count = 0

for n1, n2 in zip(seq1, seq2):
    if n1 != n2:
        if n1 in AG and n2 in AG:
            transition_count += 1
        elif n1 in CT and n2 in CT:
            transition_count += 1
        else:
            transversion_count += 1
print(transition_count/transversion_count)




