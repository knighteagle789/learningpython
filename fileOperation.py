f = open ('myfile.txt','a')

for line in f:
    print (line, end = '')

f.write('\nThis sentence will be appended.')
f.write('\nPython is Fun!')

f.close()