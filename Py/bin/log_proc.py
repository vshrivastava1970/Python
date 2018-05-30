F = open(r'D:\Training\log\log_sample.txt', 'r')

data = F.readlines()
F.close()

F1 = open(r'D:\Training\log\log_sample_report1.txt', 'w')
F2 = open(r'D:\Training\log\log_sample_report1.csv', 'w')
print('IP', 'Date', 'Pics', 'Website', sep='\t', file=F1, flush=True)
print('IP', 'Date', 'Pics', 'Website', sep=',', file=F2, flush=True)
for line in data:
    if line[0].isdigit():
        sp = line.split()
        ip = sp[0]
        # print('IP =', ip)
        dt = sp[3].split(':')
        dt = dt[0]
        dt = dt.split('[')
        dt = dt[1]
        # print('Date =', dt[1])
        if sp[6].startswith('/pics'):
            im = sp[6].split('/')
            im = im[-1]
        else:
            im = 'No Image'
        # print('Image =', im)
        wb = sp[10].split('/')
        wb = wb[2]
        # print('Web Site =', wb)
        print(ip, dt, im, wb, sep='\t', file=F1, flush=True)
        print(ip, dt, im, wb, sep=',', file=F2, flush=True)
F1.close()
F2.close()
