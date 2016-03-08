#!/usr/bin/python3 -i
import threading
import RPi.GPIO as GPIO
import time
lock=threading.Lock()
locktime=0
_timein=0.5
def do_pulse(OUT,timein):
    lock_pulse[OUT].acquire()
    GPIO.setup(OUT,GPIO.OUT)
    GPIO.output(OUT,GPIO.HIGH)
    GPIO.output(OUT,GPIO.LOW)
    time.sleep(timein)
    GPIO.output(OUT,GPIO.HIGH)
    lock_pulse[OUT].release()
    return
def pulse(OUT,timein):
    thread=threading.Thread(target=lambda:do_pulse(OUT,timein))
    thread.start()
    return thread
def callback(IN1,IN2,OUT1,OUT2,timein):
    pulse(OUT1,timein)
    GPIO.remove_event_detect(IN2)
#    GPIO.remove_event_detect(IN1)
    if lock.locked():lock.release()
    GPIO.add_event_detect(IN2,GPIO.RISING,lambda i:listen_second(IN2,IN1,OUT2,OUT1))
#    GPIO.add_event_detect(IN1,GPIO.RISING,lambda i:listen_second(IN1,IN2,OUT1,OUT2))
    return
def listen_second(IN1,IN2,OUT1,OUT2,timein=_timein):
    if not lock.locked():
        lock.acquire()
        global locktime
        locktime=time.time()
    else: return
    GPIO.remove_event_detect(IN2)
    GPIO.setup(IN2,GPIO.IN)
    GPIO.add_event_detect(IN2,GPIO.RISING,lambda i:callback(IN1,IN2,OUT1,OUT2,timein))
    return
def loopcheck(IN1,IN2,timeout):
    while 1:
        if lock.locked() and time.time()-locktime > timeout:
            GPIO.remove_event_detect(in1)
            GPIO.remove_event_detect(in2)
            GPIO.add_event_detect(in1,GPIO.RISING,callbacks1[mode])
            GPIO.add_event_detect(in2,GPIO.RISING,callbacks2[mode])
            if lock.locked():  lock.release()
            
GPIO.setmode(GPIO.BOARD)

mode=0
timeout=2
in1,in2,out1,out2=7,10,16,13
con=11
lock_pulse={out1:threading.Lock(),out2:threading.Lock()}
GPIO.setup(in1,GPIO.IN)
GPIO.setup(in2,GPIO.IN)
GPIO.setup(con,GPIO.IN)
GPIO.setup(out1,GPIO.OUT)
GPIO.setup(out2,GPIO.OUT)
GPIO.output(out1,GPIO.HIGH)
GPIO.output(out2,GPIO.HIGH)
callbacks1=[
        lambda i:listen_second(in1,in2,out1,out2),
        lambda i:listen_second(in1,in2,out2,out1),
        lambda i:pulse(out1,_timein)]
callbacks2=[
        lambda i:listen_second(in2,in1,out2,out1),
        lambda i:listen_second(in2,in1,out1,out2),
        lambda i:pulse(out2,_timein)]
def mode_change(CON):
    if lock.locked(): lock.release()
    global mode
    mode=(mode+1)%3
    GPIO.remove_event_detect(in1)
    GPIO.remove_event_detect(in2)
    GPIO.add_event_detect(in1,GPIO.RISING,callbacks1[mode])
    GPIO.add_event_detect(in2,GPIO.RISING,callbacks2[mode])
    return 
GPIO.add_event_detect(in1,GPIO.RISING,callbacks1[mode])
GPIO.add_event_detect(in2,GPIO.RISING,callbacks2[mode])
GPIO.add_event_detect(con,GPIO.RISING,mode_change)
loopcheck_thread=threading.Thread(target=lambda:loopcheck(in1,in2,timeout))
loopcheck_thread.setDaemon(True)
loopcheck_thread.start()
'''
GPIO.add_event_detect(7,GPIO.RISING,lambda i:listen_second(7,10,8,13))
GPIO.add_event_detect(10,GPIO.RISING,lambda i:listen_second(10,7,13,8))'''
def printlock():
    while 1: print(lock.locked(),lock_pulse[out1].locked(),lock_pulse[out2].locked(),mode,GPIO.input(in1),GPIO.input(in2),GPIO.input(out1),GPIO.input(out2))
