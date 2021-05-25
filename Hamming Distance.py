def hamming_distance():
    file=open('/Users/dhruvarora/Downloads/rosalind_hamm (1).txt', 'r')
    fastafile = [line.rstrip('\n') for line in file.readlines()]
    s = fastafile[0]
    t = fastafile[1]
    hamming_count = 0
    for nucleotide in range(0,len(s)):
      if s[nucleotide] != t[nucleotide]:
          hamming_count = hamming_count + 1
    print(hamming_count)

hamming_distance()
