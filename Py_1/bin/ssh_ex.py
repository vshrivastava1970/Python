import paramiko

# SSH
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)
ssh.connect(hostname='test.rebex.net', username='demo', password='password', port=22)
stdin, stdout, stderr = ssh.exec_command('ls -l')
out = stdout.readlines()
print(out)
# stdin.write()

# FTP

ftp = ssh.open_sftp()
ftp.get('readme.txt', 'dest_readme.txt')
ftp.put('dest_readme.txt', '/tmp')