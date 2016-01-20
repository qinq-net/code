#!/usr/bin/python3
import RPi.GPIO as GPIO
GPIO.cleanup()
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.OUT)
GPIO.setup(12,GPIO.IN)
while True:
#     GPIO.output(11,GPIO.HIGH)
#     GPIO.wait_for_edge(12,GPIO.RISING)
#     GPIO.output(11,GPIO.LOW)
#     GPIO.wait_for_edge(12,GPIO.FALLING)
    if GPIO.input(12): GPIO.output(11,GPIO.LOW)
    else: GPIO.output(11,GPIO.HIGH)
