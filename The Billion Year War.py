def reverse_palindrome():
    file = open('/Users/dhruvarora/Downloads/rosalind_revp (4).txt', 'r')
    next(file)
    seq = file.read()
    seq=seq.replace('\n','')
    count = 4
    while count <= 12:
        for i in range(0, len(seq)):
            j = i + count
            substring = seq[i:j]
            if len(substring) == count:
                rev_substring = rev(substring)
                complement_substring = complement(rev_substring)
                if substring == complement_substring:
                    print(i + 1, count)
        count += 1


def rev(substring):
    arr = []
    for i in range(len(substring) - 1, -1, -1):
        arr.append(substring[i])
    return ''.join(arr)


def complement(string):
    arr = []
    for nucleotide in string:
        if nucleotide == 'A':
            arr.append('T')
        elif nucleotide == 'T':
            arr.append('A')
        elif nucleotide == 'G':
            arr.append('C')
        else:
            arr.append('G')
    return ''.join(arr)


reverse_palindrome()