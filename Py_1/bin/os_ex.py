# import system command

import os

out = os.listdir()
print('out =', out)

rSuccessStatus0 = os.system('dir')
print('rSuccessStatus0  =', rSuccessStatus0)

rFailedStatus1 = os.system('dirxy')
print('rFailedStatus1 =', rFailedStatus1)

# x,y,z = os.walk
# main[Sub][f1,f2]

path = input('Enter Path:')
for main, sub, files in os.walk(path):
    for f in files:
        if f.endswith('.py'):
            f = main + '\\' + f
            print('file =', f)
