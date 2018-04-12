#!/usr/bin/env python

import paramiko

with paramiko.SSHClient() as ssh:
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    ssh.connect('localhost', username='python', password='l0lz')

