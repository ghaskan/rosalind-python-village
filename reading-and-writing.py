f = open('', 'r') # input location
g = open('','w') # output location

data = f.read()

lines = data.splitlines()

c = 0

for i in lines:
    if c % 2 != 0:
        print(i)
        g.write(str(i) + '\n')
    c += 1

f.close()
g.close()
