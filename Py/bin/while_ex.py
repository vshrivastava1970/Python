a = 10
while a > 0:
    # print("a=", a)
    a -= 1
S = 'Wel come'
i = 0

while i < len(S):
    # print('S=', S[i])
    i += 1
L = [10, 20, 30]
while L:
    X = L.pop()
    print('Removed:', X)

D = {'A': 10, 'B': 20}
while D:
    X = D.popitem()
    print('Removed:', X)

L = [1, 2, 10, 3, 4, 10, 5, 6, 7]

j = 0
while j < len(L):
    if L[j] == 10:
        j = j + 1
        print('Next Element:', L[j])
    j = j + 1

comp = ['Sap', 'Synechron', 'IBM']
k = 0
while k < len(comp):
    if comp[k] == 'Synechron':
        print('Found')
        break
    k += 1
else:
    print('Not Found')

l = 0
while l < len(comp):
    if comp[l] != 'Synechron':
        l = l + 1
        continue
    print('Comp = ', comp[l])
    l = l + 1

# do while

cart = []

while True:
    item = input('Enter Item:')
    cart.append(item)
    choice = input('Do you eant to stop (y/n):')
    if choice.upper() == 'Y':
        print('Your cart: ', cart)
        print('Emptying cart:')
        cart.clear()
        break
