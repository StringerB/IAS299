#!/usr/bin/python3
import subprocess

host = "10.235.30."
max_host = 255

def ping(host):
    for item in  range(1, max_host):
        proc = subprocess.Popen('ping -c 1 ' + host + str(item), 
                shell=True, stdout=subprocess.PIPE)
        proc.wait(timeout=1)
        r = proc.communicate(timeout=1)
        print(r)

ping(host)
