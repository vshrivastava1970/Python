#Sets
#Unordered
#No index
#No key
#Unique
#Mutable

S = {10,10,'Python', 'Python'}
print(S)
S.add(100)
S.add(100)
print(S)

#Remove

X=S.pop()
#Y=S.remove(10)

L = [10,10,20,30]

S = set(L)
print(S)
L = list(S)
print(L)
