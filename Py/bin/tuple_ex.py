T=(10,12.5, 'Python', [10,20], ('a', 'b'))

print(T[0])

print(T[1:4])

i = T.index(12.5)

c = T.count('Python')

L= list(T)

L.append(10)

T=tuple(L)

print('T=', T)
