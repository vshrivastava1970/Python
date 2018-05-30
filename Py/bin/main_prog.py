# import mymodule
import mymodule as m

'''
//We can import lib from file also. Scope will be only for that file
import sys
sys.path.append(r'D:\training\lib')
'''

# print(mymodule.msg)

# r1 = mymodule.add(10, 20)
# print('r1=', r1)

print(m.msg)

r1 = m.add(10, 20)
print('r1=', r1)

from mymodule import msg, add

print(msg, add(10, 20))

from mymodule import msg as M

print('M=', M)

from mymodule import *

# msg = 'Hello'
print(msg, add(10, 20), M)

############################# package demo ####

import cloud.net.mymodule

print('cloud pkg:', cloud.net.mymodule.msg)

import cloud.net.mymodule as m

print('cloud m pkg:', m.msg)

from cloud.net.mymodule import msg

print('cloud msg pkg:', msg)

from cloud.net.mymodule import *

print('cloud msg pkg:=', msg)
