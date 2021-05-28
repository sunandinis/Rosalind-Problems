from Bio import SeqIO
def lcsm():
    file = open('/Users/Downloads/rosalind_lcsm (2).txt', 'r')
    sequences = []
    for record in SeqIO.parse(file, 'fasta'):
        sequences.append(str(record.seq))

    file.close()


    sorted_seq = sorted(sequences, key=len)
    short_seq = sorted_seq[0]
    comp_seq = sorted_seq[1:]
    motif = ''
    for i in range(len(short_seq)):
        for j in range(i, len(short_seq)):
            m = short_seq[i:j + 1]
            found = False
            for sequ in comp_seq:
                if m in sequ:
                    found = True
                else:
                    found = False
                    break
            if found and len(m) > len(motif):
                motif = m
    print(motif)


lcsm()