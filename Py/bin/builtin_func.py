L = [1, 2, 3, 4]


def squares(M):
    r = []
    for i in M:
        r.append(i * i)
    return r


out = squares(L)

for j in out:
    print('j =', j)


###############
# Generator
def squares1(M):
    r = []
    for i in M:
        yield i * i
        # Its not storing data/item in memory, instead use a generated object to store items and return reference
    return r


out = squares1(L)
# out = list(out)
for k in out:
    print('squares1 k =', k)

for l in out:
    print('squares1 l =', l)


###############
# Decorators

def mydecorators(f):
    def new_func(a, b):
        print('Add Result')
        f(a, b)
        print('End & Return')

    return new_func

@mydecorators   # used to assign decorator function for add(a, b)
def add(a, b):
    print(a+b)

add(10, 20)