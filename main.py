import paramiko
import time
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(
    paramiko.AutoAddPolicy())
ssh.connect('10.240.230.121', username='monitor', password='ess')
command = 'ls'
(stdin, stdout, stderr) = ssh.exec_command(command)
#stdin.write('ess\n')
time.sleep(1.0)
for line in stdout.readlines():
        print(line, end = '')
ssh.close()