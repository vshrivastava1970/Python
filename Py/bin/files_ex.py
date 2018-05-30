from builtins import print

F = open(r'D:\Training\log\report1.txt', 'w')
# always new file

X = 10
Y = 'Python \n'

# write content into a file
X = str(X) + '\n'
F.write(X)
F.write(Y)
F.flush()
# F.close()

L = [X, Y]
F.writelines(L)
F.flush()
F.close()

F = open(r'D:\Training\log\report1.txt', 'r')
r1 = F.read()
#print('r1=', r1)

F.seek(0)

r2 = F.read()
#print('r2 =', r2)

F.seek(0)

r3 = F.readline()
while r3 != '':
    print('r3 =', r3)
    r3 = F.readline()

F.seek(0)
r4 = F.readlines()
print('r4 =', r4)