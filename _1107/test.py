#!/usr/bin/python3 -i
import time
from RPi.GPIO import *
setmode(BOARD)
def beam(out,timein=0.1):
    setup(out,OUT)
    output(out,LOW)
    time.sleep(timein)
    output(out,HIGH)
    time.sleep(timein)
    output(out,LOW)

