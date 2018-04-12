#!/usr/bin/env python

import time
import paramiko

USER = 'student'
PASSWORD = 'l0lz'
PORT = 22
HOST = 'localhost'

import paramiko

ssh = paramiko.SSHClient()

ssh.set_missing_host_key_policy(
    paramiko.AutoAddPolicy())

ssh.connect('192.168.1.104', username=USER, password=PASSWORD)

# transport = paramiko.Transport((HOST, PORT))    
# transport.connect(username = USER, password = PASSWORD)    
# 
# def execute_cmd(transport, cmd):
#     channel = transport.open_channel(kind = "session")
#     channel.exec_command(cmd)
# 
#     while not channel.exit_status_ready():
#         time.sleep(1)
#     output = channel.recv(99999)
#     err_output = channel.recv_stderr(99999)
#     return channel.exit_status,output, err_output
# 
# status, output, err = execute_cmd(transport, 'whoami')
# print('status is:', status)
# print('output is:', output.rstrip())
# print('err is:', err)
# print()
# 
# status, output, err = execute_cmd(transport, 'ls -l /Users/{}'.format(USER))
# print('status is:', status)
# print('output is:', output.rstrip())
# print('err is:', err)
# print()
# 
# status, output, err = execute_cmd(
#     transport, 'ls -l /Users/{}'.format('CARDINALBIGGLES')
# )
# 
# print('status is:', status)
# print('output is:', output.rstrip())
# print('err is:', err)
# print()
# 
# transport.close()
