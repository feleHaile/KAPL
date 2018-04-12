#!/usr/bin/env python
from subprocess import run, check_output, CalledProcessError, PIPE
from glob import glob
import shlex

# "ls -l DATA/*"         NOT WINDOWS

# r"cmd / dir DATA\*"     WINDOWS

cmd = 'ls -l'
filespec = 'DATA/*.txt'

fake_command = 'abc def "some thing" xyz "other thing"'

cmd_words = shlex.split(cmd)
files = glob(filespec)
print(files)

full_cmd = cmd_words + files

print(full_cmd)

proc = run(full_cmd, stdout=PIPE, stderr=PIPE)

print(proc.returncode)
print(proc.stdout.decode())
print(proc.stderr.decode())

print('-' * 60)

try:
    output = check_output(full_cmd)
except CalledProcessError as err:
    print(err.returncode)
    print(err)
else:
    print("OUTPUT:", output)
