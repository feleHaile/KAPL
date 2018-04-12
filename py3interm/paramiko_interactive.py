#!/usr/bin/env python

import paramiko

with paramiko.SSHClient() as ssh:
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    ssh.connect('localhost', username='python', password='l0lz')

    stdin, stdout, stderr  = ssh.exec_command('bc')

    stdin.write("17 + 25\n")
    result = stdout.readline()
    print("Result is:", result)

    stdin.write("scale = 3\n")
    stdin.write("738.32/191.3902\n")
    result = stdout.readline()
    print("Result is:", result)

    stdin.write("quit\n")

