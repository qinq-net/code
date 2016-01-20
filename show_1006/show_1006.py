#!/usr/bin/python3
import RPi.GPIO as GPIO
import time
import threading
GPIO.setmode(GPIO.BOARD)
class control:
    GPIO.setmode(GPIO.BOARD)
    def change(self,arg):
        GPIO.remove_event_detect(self.IN)
        while GPIO.input(self.IN): 1
        if self.flag11: GPIO.output(self.OUT,GPIO.HIGH)
        else: GPIO.output(self.OUT,GPIO.LOW)
        self.flag11 = not self.flag11
        time.sleep(0.05)
        return GPIO.add_event_detect(self.IN,GPIO.BOTH,self.change,1000)
    def __init__(self,IN,OUT):
        self.IN,self.OUT=IN,OUT
        GPIO.setup(self.IN,GPIO.IN)
        GPIO.setup(self.OUT,GPIO.OUT)
        self.flag11 = False
        GPIO.output(self.OUT,GPIO.LOW)
        GPIO.add_event_detect(self.IN,GPIO.BOTH,self.change,1000)
class thread:
    flag = False
    def __init__(self,IN,OUT,mode=0):
        self.IN = IN
        self.OUT = OUT
        self.mode = mode
        GPIO.setup(self.IN,GPIO.IN)
        GPIO.setup(self.OUT,GPIO.OUT)
        GPIO.output(self.OUT,GPIO.LOW)
        self.thread = threading.Thread(target=self.call)
        self.thread.setDaemon(True)
        self.thread.start()
    def call(self):
        if self.mode == 0:
            while True:
                if GPIO.input(self.IN):
                    while GPIO.input(self.IN): 1
                    if self.flag: GPIO.output(self.OUT,GPIO.HIGH)
                    else: GPIO.output(self.OUT,GPIO.LOW)
                    self.flag = not(self.flag)
                    time.sleep(0.05)
        elif self.mode == 1:
            while True:
                if GPIO.input(self.IN): GPIO.output(self.OUT,GPIO.LOW)
                else: GPIO.output(self.OUT,GPIO.HIGH)
if __name__ == '__main__':
    main = thread(7,8,0)
    check = thread(7,10,1)
    while True: 1
