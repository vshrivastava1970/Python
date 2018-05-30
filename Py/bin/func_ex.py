def add1():
    pass  # if nothing is to execute


def add2():
    X = 10
    Y = 20
    Z = X + Y
    print('add=', Z)


add2()


# print('Z=', Z)

def add3():
    X = 10
    Y = 20
    Z = X + Y
    # return Z
    # return
    # return [X, Y, Z]
    return (X + Y) / 2


def add4(X, Y):
    return X + Y


r3 = add3()
print('add()3=', r3)

r4 = add4(5, 10)
print('add()4=', r4)


def add5(X, Y=10):
    return X + Y


r5 = add5(10)
print('add()5=', r5)

r6 = add5(10, 20)
print('add()6=', r6)

r7 = add5(10, 0)
print('add()7=', r7)


#####################################
def add6(X, Y=10, *Z):
    r = X + Y
    print('add()6 tuple =', r)
    for i in Z:
        r += i
    return r


r8 = add6(10)
print('add()6 r8 =', r8)
r9 = add6(10, 20)
print('add()6 r9 =', r9)
r10 = add6(10, 20, 30, 40)  # Z=(30, 40)
print('add()6 r10 =', r10)


##################################
def add7(*a):
    if len(a) == 0:
        return 'No elements'
    else:
        r = 0
        for i in a:
            r += i
        return r


r11 = add7()
r12 = add7(10)
r13 = add7(10, 20)
print('add()7 =', r11, r12, r13)


#####################################
def add8(X, Y=10, *Z, a, b=20):
    r = X + Y + a + b
    print('tuple=', Z)
    for i in Z:
        r += i
    return r


# keyword argument
r14 = add8(10, 20, 30, 40, a=50, b=60)
print('add8=', r14)


#########################

def add9(*, a, b):
    return a + b


r15 = add9(b=10, a=20)
print('add9=', r15)


############################
def add10(X, Y=10, *Z, a, b, **C):
    r = X + Y + a + b
    print('tuple=', r)
    print('Dict=', C)
    for i in Z:
        r += i
    for j in C.values():
        r += j
    return r


r16 = add10(10, b=10, a=20)
r17 = add10(10, 20, 30, 40, b=10, a=20, c=30, d=40)

print('add10 r16=', r16)
print('add10 r17=', r16)
############################
X = 10
L = [10, 20]


def add11(a, b):
    a = 100
    b.append(30)
    print('ab=', a, b)


r18 = add11(X, L)
print('X & L =', X, L)
###########################

M = 10  # Global scope


# Builtin scope -  also will be available. If we do not define variable, then
# it will do the lookup in builtin scope before to report error

def f1():
    M = 20  # Enclosed scope variable

    def f2():
        # nonloacl M //refer enclosed variable
        # global M // to refer or modifiy global variable
        # global n // it will define new gloable variable
        M = 30  # local scope variable
        print('f2 =', M)

    f2()
    print('f1=', M)


f1()
print('Global=', M)


######################################
def Account():
    count = 0

    def create_acc():
        nonlocal count
        count = count + 1
        print('Your account number is =', count)

    return create_acc


a = Account()  # it return inner create_acc function
a()  # nothing but its calling inner create_acc function
a()  # nothing but its calling inner create_acc function
a()  # nothing but its calling inner create_acc function
