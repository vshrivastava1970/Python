c=10

if(c>0 and c<100):
    print('In range')

S='Python'

if 'th'in S:
    print('th found')

if S == 'Python':
    print('String are equal')


L1 = [10, 20, 'Python']

L2=L1

if 10 in L1:
    print('10 found')

if 'th' in L1[2]:
    print('th found')


if L1 == L2:
    print('Objects are equals')

D = {'A':10, 'B':20}

if 'A' in D:
    print('A - found')

if 'A' in D.keys():
    print('Key A - found')
if 10 in D.values():
    print('Value 10 found')
