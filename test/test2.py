#!/usr/bin/python3
import RPi.GPIO as GPIO
import time
GPIO.cleanup()
class SYSTEM:
    GPIO.setmode(GPIO.BOARD)
    def change(self,arg):
        GPIO.remove_event_detect(self.IN)
        print(1)
        while GPIO.input(self.IN): 1
        if self.flag11: GPIO.output(self.OUT,GPIO.HIGH)
        else: GPIO.output(self.OUT,GPIO.LOW)
        self.flag11 = not self.flag11
        time.sleep(0.1)
        return GPIO.add_event_detect(self.IN,GPIO.BOTH,self.change,1000)
    def __init__(self,IN,OUT):
        self.IN,self.OUT=IN,OUT
        GPIO.setup(self.IN,GPIO.IN)
        GPIO.setup(self.OUT,GPIO.OUT)
        self.flag11 = False
        GPIO.output(self.OUT,GPIO.LOW)
        GPIO.add_event_detect(self.IN,GPIO.BOTH,self.change,1000)
system = SYSTEM(12,11)
while True: time.sleep(1)
