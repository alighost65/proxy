#!/usr/bin/env python
import subprocess

subprocess.run('python socks5.py &', shell=True)
subprocess.run('python pysoxy.py &', shell=True)