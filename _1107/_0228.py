#!/usr/bin/python3 -i
import threading
import RPi.GPIO as GPIO
import time
lock=threading.Lock()
lock2=threading.Lock()
def pulse(OUT,timein):
    GPIO.setup(OUT,GPIO.OUT)
    GPIO.output(OUT,GPIO.LOW)
    time.sleep(timein)
    GPIO.output(OUT,GPIO.HIGH)
    return
def callback(IN1,IN2,OUT1,OUT2,timein):
    pulse(OUT1,timein)
    GPIO.remove_event_detect(IN2)
    GPIO.remove_event_detect(IN1)
    if lock.locked():lock.release()
    GPIO.add_event_detect(IN2,GPIO.RISING,lambda i:listen_second(IN2,IN1,OUT2,OUT1))
    GPIO.add_event_detect(IN1,GPIO.RISING,lambda i:listen_second(IN1,IN2,OUT1,OUT2))
    return
def listen_second(IN1,IN2,OUT1,OUT2,timein=0.75):
    if not lock.locked(): lock.acquire()
    else: return
    GPIO.remove_event_detect(IN2)
    GPIO.setup(IN2,GPIO.IN)
    GPIO.add_event_detect(IN2,GPIO.RISING,lambda i:callback(IN1,IN2,OUT1,OUT2,timein))
    return
GPIO.setmode(GPIO.BOARD)

mode=0
in1,in2,out1,out2=7,10,8,13
con=11
GPIO.setup(in1,GPIO.IN)
GPIO.setup(in2,GPIO.IN)
GPIO.setup(con,GPIO.IN)
callbacks1=[
        lambda i:listen_second(in1,in2,out1,out2),
        lambda i:listen_second(in1,in2,out2,out1),
        lambda i:pulse(out1,0.75)]
callbacks2=[
        lambda i:listen_second(in2,in1,out2,out1),
        lambda i:listen_second(in2,in1,out1,out2),
        lambda i:pulse(out2,0.75)]
def mode_change(CON):
    lock.acquire()
    global mode
    mode=(mode+1)%3
    GPIO.remove_event_detect(in1)
    GPIO.remove_event_detect(in2)
    GPIO.add_event_detect(in1,GPIO.RISING,callbacks1[mode])
    GPIO.add_event_detect(in2,GPIO.RISING,callbacks2[mode])
    return lock.release()
GPIO.add_event_detect(in1,GPIO.RISING,callbacks1[mode])
GPIO.add_event_detect(in2,GPIO.RISING,callbacks2[mode])
GPIO.add_event_detect(con,GPIO.RISING,mode_change)

'''
GPIO.add_event_detect(7,GPIO.RISING,lambda i:listen_second(7,10,8,13))
GPIO.add_event_detect(10,GPIO.RISING,lambda i:listen_second(10,7,13,8))'''
