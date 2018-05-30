L = ['Python', 5, ['Pune', 'Blr']]

D = {'course':'Python', 'dur':5, 'Loc':['Pune', 'Blr']}

E = dict(course='Python', dur=5, Loc=['Pune', 'Blr'])
# To access element

print(D['course'])
print(D['Loc'][1])

#add & update

D['course'] = ['Java','Python']

#Remove

X=D.pop('dur')
Y=D.popitem()

del D

D = E.copy()
E.clear()
print(D)
#D.clear()
#print(D)

K =D.keys()
V =D.values()
I =D.items()
print(K)
print(V)
print(I)
