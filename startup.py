#!/usr/bin/python3 -i
# Python Startup Script
import sys
import readline
import rlcompleter
import atexit
import os
# Tab Completion
readline.parse_and_bind('tab: complete')
# History File
__history_file=os.path.join(os.environ['HOME'], '.python3history')
try:
    readline.read_history_file(__history_file)
except IOError:
    pass
atexit.register(readline.write_history_file, __history_file)
del os, __history_file, readline, rlcompleter

