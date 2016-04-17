input = open('C:\\Users\\win-7\\Downloads\\rosalind_ini6.txt', 'r')
output = open('C:\\Users\\win-7\\Desktop\\derp.txt','w')

data = input.read()
freq = {}

for word in data.split(' '):
        word = word.rstrip('\n')
        word = word.rstrip('\r')
        freq[word] = freq.get(word,0) + 1

for value in freq:
    output.write(str(value) + ' ' + str(freq[value]) + '\n')

input.close()
output.close()
