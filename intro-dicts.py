input = open('', 'r') # input location
output = open('','w') # output location

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
