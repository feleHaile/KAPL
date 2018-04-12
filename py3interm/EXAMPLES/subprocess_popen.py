#!/usr/bin/env python
import sys
import subprocess as sp
from glob import glob

files = glob('DATA/*')

print(sys.platform)

if sys.platform == 'win32':
    CMD = ['cmd', '/c', 'dir', r'c:\Windows\system32\calc.exe']  # change to clac.exe to see STDERR
else:
    CMD = ['ls', '-l', '/etc/passwd','/etc/wildebeest' ]


# check status and capture STDERR
stdout_filename, stderr_filename = 'proc_stdout.txt', 'proc_stderr.txt'
with open(stdout_filename, 'w') as F_STDOUT:
    with open(stderr_filename, 'w') as F_STDERR:
        try:
            proc = sp.Popen(CMD, stdout=F_STDOUT, stderr=F_STDERR, timeout=60)
        except sp.CalledProcessError as e:
            print("TRY 2: Process failed with return code", e.returncode)
            print("Error message is [[{0}]]".format(err))
        else:
            print("No exceptions were raised.")

        # wait for process to finish and get status code
        status_code = proc.wait()
        
        # now read the files just created above
        with open(stdout_filename) as F_STDOUT:
            with open(stderr_filename) as F_STDERR:
                stderr_text = F_STDERR.read()
                stdout_text = F_STDOUT.read()

print("STATUS:", status_code)
print("CAPTURED STDOUT:\n", stdout_text)
print("CAPTURED STDERR:\n", stderr_text)
