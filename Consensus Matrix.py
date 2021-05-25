def consensus_profile():
    file = open('./consensus.txt', 'r')
    output = []
    while True:
        line = file.readline()
        if line.__contains__('>'):
            pass
        elif line == '':
            break
        else:
            output.append(line.rstrip())

    collength = len(output[0])
    col = 0
    consensus_seq = ''
    k = []
    A = []
    C = []
    G = []
    T = []
    while col < collength:
        for string in output:
            k.append(string[col])
        a_count = k.count('A')
        t_count = k.count('T')
        g_count = k.count('G')
        c_count = k.count('C')
        A.append(a_count)
        C.append(t_count)
        G.append(g_count)
        T.append(t_count)
        maximum = max(a_count, t_count, g_count, c_count)
        if maximum == a_count:
            consensus_seq += 'A'
        elif maximum == t_count:
            consensus_seq += 'T'
        elif maximum == g_count:
            consensus_seq += 'G'
        else:
            consensus_seq += 'C'
        col += 1
        k = []
    print(consensus_seq)
    print('A:' + str(A))
    print('C:' + str(C))
    print('G:' + str(G))
    print('T:' + str(T))



consensus_profile()





