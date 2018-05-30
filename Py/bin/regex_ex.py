import re

F = open(r'D:\Training\log\log_sample.txt')

data = F.readlines()
F.close()

import csv

out = open(r'D:\Training\log\report3.csv', 'w', newline='')

writer = csv.writer(out)

for line in data:
    M = re.match('(\d{3}\.\d{1,3}\.[]0-9]{3}\.\d{3}).*(\d{2}/[A-za-z]{3}/\d{4}).*GET\s+/(pics/\w+\.\w+)?.*(http://\w*\.\w*\.\w*).*', line)
    # print(M)
    if M is not None:
        ip = M.group(1)
        dt = M.group(2)
        im = M.group(3)
        ws = M.group(4)
        print(ip, dt, im, ws)
        L=[ip, dt, im, ws]
        writer.writerow(L)
out.close()

F = open(r'D:/Training/log/report3.csv', 'r', newline='')
out = csv.reader(F)
print(list(out))
print(list(out))