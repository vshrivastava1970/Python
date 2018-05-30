a = 10
b = 0

# try:
#   r1 = a/b
#  print('r1 =', r1)

# except:
#   print('Some error')


try:
    r1 = a / b
    print('r1 =', r1)

except NameError:
    print('Name error')
except ZeroDivisionError:
    print('Zero Division error')
except:
    print('Some error')
finally:
    print('Always execute')

###############
e = 10
f = 0

try:
    r = e / f
except Exception as e:
    print('type exception =', type(e))

##############
g = 10
h = 0
try:
    assert h > 0, 'h is zero'
    print('assert ex')
except AssertionError as ae:
    print('AE Error', ae)
###############
i = 0
j = 0
try:
    if j == 0:
        raise ZeroDivisionError
    print('inside raise i')
    r = i / j
except ZeroDivisionError:
    print('ZDE')


# ############ Custom Exception ##########
class MyExc(Exception):
    def __init__(self, m):
        print('Error Details:', m)

    def viewcompletedetails(self):
        print('Complete details:')

f=0
try:
    if f == 0:
        raise MyExc('f is 0')
except ZeroDivisionError:
    print('ZDE')
except MyExc as a:
    print('MyExe')
    a.viewcompletedetails()