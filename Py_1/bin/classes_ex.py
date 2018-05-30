# multiple objects asn each object has their individual namespace
# Has inheritance
# Operator overloading

class Account:
    def addname(self, n):
        self.name = n

    def viwname(self):
        return self.name

    B_name = 'ICICI'

    def viewtc():
        return "TC"

    def __init__(self):
        print('Account number logic here')


class Newacc(Account):
    def addaadhar(self, a):
        self.ad = a

    def viewaadhar(self):
        return self.ad

    def viewname(self):
        return 'Hello' + self.name

    def __init__(self):
        print('init in NewAcc')
        Account.__init__(self)


class RBI:
    def viewrules(self):
        return 'RBI Rules'


class Account3(Newacc, RBI):
    def message(self):
        print('Inside Account')


class Bank:
    def viewrules(self):
        return 'Bank Rules'


class Account4(Newacc, RBI, Bank):
    def __init__(self):
        self.bank = Bank()
        super().__init__()

    def __add__(self, other):
        res = 'Hello ' + self.name + ' and ' + other.name
        return res


###############################
a1 = Account()
a2 = Account()
a1.addname('N-1')
a2.addname('N-2')

print(a1.viwname())
print(a2.viwname())
print(Account.B_name)
print(Account.viewtc())

a4 = Account3()
a4.addname('N-4')
print(a4.viewname())
print(a4.viewrules())

a5 = Account4()
a5.addname('N-5')
print(a5.viewname())
print(a5.viewrules())
print(a5.bank.viewrules())

a6 = Account4()
a6.addname('N-6')
r = a5 + a6
print(r)
