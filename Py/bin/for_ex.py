'''
S = 'Python'
for a in S:
    print('a =', a)

b=100

L=[10,20,30]

for b in L:
    print('b=', b)
    print('type=', type(b))

print('Now b =', b)
'''
D = {'A': 10, 'B':20}
'''
for c in D:
    print('C=', c)
    print('Value=', D[c])

for d in D.keys():
    print('d=', d)

for e in D.values():
    print('e=', e)


for i in D.items():
    print('i=', i)

for k, v in D.items():
    print('k=', k)
    print('v=', v)
    if v == 10:
        print('Key for 10 is =', k)
'''
L1 = [10,20,30]
L2 = ['a', 'b']

for i,j,k,l in zip(L1, L2,L1, L2):
    print(i,j,k,l)
    
comp=['Sap','Synechron','IBM']

for c in comp:
    if(c == 'Synechron'):
        print('Synechron found')
        break
else:
    print('Not found')
    

n=range(10)
list(n)
n=range(1, 10)
list(n)
n=range(1,10,2)
list(n)

for i in range(1,10,2):
    print('i=',i)

for i in range(0,len(comp)):
    print('comp=',comp[i])





    
