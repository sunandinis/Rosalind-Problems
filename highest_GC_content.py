def highest_GC_content():
    file = open('/Users/dhruvarora/Downloads/rosalind_gc.txt', 'r')
    fastafile = [line.rstrip('\n') for line in file.readlines()]
    fastalabel = ''
    fastDict = {}
    for line in fastafile:
      if '>' in line:
          fastalabel=line
          fastDict[fastalabel] = ''
      else:
          fastDict[fastalabel] += line
    ResultDict = dict(fastDict)

    maximum = float('-inf')
    protien = ''

    for key,value in ResultDict.items():
        val = ((value.count('C') + value.count('G'))/ len(value) * 100)
        ResultDict[key] = val
        if val > maximum:
            maximum = val
            protien = key.lstrip(">")



    print(protien + '\n' + str(maximum))






highest_GC_content()