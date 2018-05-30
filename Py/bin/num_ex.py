# Numbers

a = 10 #int
b = 12.5 #float
c = 0b1010 #bin
d = 0x123 #hex
e = 0o12 #oct
# Dynamically Typed
print('Hello')
print(a,b,c,d,e)
#Immutable
'''
if we override with new value of a = 100, then
python will create new object with value 100 and assign new reference to
a
'''
a=100
f=a
a=200
print (f,a)
a= a+f
g = 'WEL COME'

print(len(g))

#print(g[0:6:1])
#print(g[0:6:2])
#print(g[::3])
print(g[::-1])
print(g[1])
r1=g.startswith('WE')
r2=g.endswith('COME')
r3=g.istitle()
r4=g.title()
r5=g.isupper()
r6=g.upper()
r7=g.islower()
r8=g.lower()
print(r1,r2,r3,r4,r5,r6,r7,r8)
rr1 = g.split('E')
print(rr1)

L1 = [10, 20]
L2 = ['a', 'b']
#L3 = L1 +L2
print(L1+L2)
L4 = [10,20,['a','b']]

L5 = L4.copy()

L4[0] = 100
#print(L4,L5)
L4.append('C')
print(L4,L5)









