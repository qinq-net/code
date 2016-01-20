#!/usr/bin/python3 -i
import RPi.GPIO as GPIO
import time
import threading
GPIO.setmode(GPIO.BOARD)
#class control:
#    GPIO.setmode(GPIO.BOARD)
#    def change(self,arg):
#        GPIO.remove_event_detect(self.IN)
#        while GPIO.input(self.IN): 1
#        if self.flag11: GPIO.output(self.OUT,GPIO.HIGH)
#        else: GPIO.output(self.OUT,GPIO.LOW)
#        self.flag11 = not self.flag11
#        time.sleep(0.05)
#        return GPIO.add_event_detect(self.IN,GPIO.BOTH,self.change,1000)
#    def __init__(self,IN,OUT):
#        self.IN,self.OUT=IN,OUT
#        GPIO.setup(self.IN,GPIO.IN)
#        GPIO.setup(self.OUT,GPIO.OUT)
#        self.flag11 = False
#        GPIO.output(self.OUT,GPIO.LOW)
#        GPIO.add_event_detect(self.IN,GPIO.BOTH,self.change,1000)
def listen(IN,getstop,timein=0.05,timeout=3):
    while True:
        if getstop(): return
        if GPIO.input(IN):
            time.sleep(timein)
            if GPIO.input(IN):
                starttime=time.time()
                while time.time() - starttime< timeout:
                    if getstop(): return
                    if not GPIO.input(IN): return time.time() - starttime
                while GPIO.input(IN):
                    if getstop(): return
def beam(OUT,timein=0.1):
    GPIO.setup(OUT,GPIO.OUT)
    GPIO.output(OUT,GPIO.LOW)
    time.sleep(timein)
    GPIO.output(OUT,GPIO.HIGH)
    time.sleep(timein)
    GPIO.output(OUT,GPIO.LOW)
class control:
    def __init__(self,IN,OUT,CON,mode=0):
        self.IN = IN
        self.OUT = OUT
        self.CON = CON
        self.mode = mode
        GPIO.setup(self.IN, GPIO.IN)
        GPIO.setup(self.OUT,GPIO.OUT)
        GPIO.setup(self.CON,GPIO.IN)
        self.control=threading.Thread(target=self.control)
        self.control.setDaemon(True)
        self.execute = thread(IN,OUT)
        self.getstop = lambda: False
    def start(self):
        self.control.start()
    def setmode(self, mode):
        self.mode = mode
        self.execute.setmode(self.mode)
    def control(self):
        while True:
            self.setmode(self.mode)
            if self.mode in [1,2,3,4]:
                listen(self.CON, self.getstop)
                if self.mode == 1: self.mode = 2
                elif self.mode == 2: self.mode = 3
                elif self.mode == 3: self.mode = 4
                elif self.mode == 4: self.mode = 1
            else:
                while True: 1
# class thread:
#     def __init__(self,IN,OUT,mode=0):
#         self.IN = IN
#         self.OUT = OUT
#         self.mode = mode
#         self.stopflag=False
#         GPIO.setup(self.IN,GPIO.IN)
#         GPIO.setup(self.OUT,GPIO.OUT)
#         self.flag=bool(GPIO.input(self.OUT))
#         #self.father = threading.Thread(target=self.fatherfunc)
#         #self.father.setDaemon(True)
#         self.thread = threading.Thread(target=self.call)
#         self.thread.setDaemon(True)
#     #def fatherfunc(self):
#     #    self.thread.start()
#     #    while not self.stopflag: 1
#     def start(self):
#         self.stopflag=False
#         self.thread.__init__(target=self.call)
#         self.thread.start()
#     def getstop(self):
#         return self.stopflag
#     def stop(self):
#         self.stopflag=True
#         while self.thread.isAlive(): 1
#         return self.thread.isAlive()
#     def setmode(self,mode):
#         self.stop()
#         self.mode = mode
#         self.start()
#     def call(self):
#         if self.mode == 1:
#             while True:
#                 listen(self.IN,self.getstop)
#                 if self.stopflag: return
#                 if self.flag: GPIO.output(self.OUT,GPIO.HIGH)
#                 else: GPIO.output(self.OUT,GPIO.LOW)
#                 self.flag = not(self.flag)
#                 time.sleep(0.05)
#         elif self.mode == 2:
#             while True:
#                 listen(self.IN,self.getstop)
#                 if self.stopflag: return
#                 time.sleep(2)
#                 if self.flag: GPIO.output(self.OUT,GPIO.HIGH)
#                 else: GPIO.output(self.OUT,GPIO.LOW)
#                 self.flag = not(self.flag)
#                 time.sleep(0.05)
#         elif self.mode == 3:
#             while True:
#                 if self.stopflag: return
#                 if GPIO.input(self.IN): GPIO.output(self.OUT,GPIO.HIGH)
#                 else: GPIO.output(self.OUT,GPIO.LOW)
#         else:
#             while True:
#                 if self.stopflag: return
#                 if GPIO.input(self.IN): GPIO.output(self.OUT,GPIO.LOW)
#                 else: GPIO.output(self.OUT,GPIO.HIGH)
class thread(threading.Thread):
    def __init__(self, IN, OUT, mode=0):
        self.IN = IN
        self.OUT = OUT
        self.mode = mode
        self.stopflag=False
        GPIO.setup(self.IN,GPIO.IN)
        GPIO.setup(self.OUT,GPIO.OUT)
        self.flag=bool(GPIO.input(self.OUT))
        threading.Thread.__init__(self, target=self.target)
        threading.Thread.setDaemon(self, True)
    def target(self):
        if self.mode == 1:
            while True:
                listen(self.IN,self.getstop)
                if self.stopflag: return
                if self.flag: GPIO.output(self.OUT,GPIO.HIGH)
                else: GPIO.output(self.OUT,GPIO.LOW)
                self.flag = not(self.flag)
                time.sleep(0.05)
#        elif self.mode == 2:
#             while True:
#                 listen(self.IN,self.getstop)
#                 if self.stopflag: return
#                 time.sleep(2)
#                 if self.flag: GPIO.output(self.OUT,GPIO.HIGH)
#                 else: GPIO.output(self.OUT,GPIO.LOW)
#                 self.flag = not(self.flag)
#                 time.sleep(0.05)
        elif self.mode == 3:
            while True:
                if self.stopflag: return
                if GPIO.input(self.IN): GPIO.output(self.OUT,GPIO.HIGH)
                else: GPIO.output(self.OUT,GPIO.LOW)
        elif self.mode in [2,4]:
            while True:
                GPIO.output(self.OUT,GPIO.HIGH)
                self.flag=True
                listen(self.IN,self.getstop,timein=0.2)
                if self.stopflag: return
                else:
                    if self.mode == 2: time.sleep(2)
                    GPIO.output(self.OUT,GPIO.LOW)
                    self.flag=False
                    time.sleep(1)
        else:
            while True:
                if self.stopflag: return
                if GPIO.input(self.IN): GPIO.output(self.OUT,GPIO.LOW)
                else: GPIO.output(self.OUT,GPIO.HIGH)
        GPIO.setup(self.OUT,GPIO.OUT)
        self.flag=bool(GPIO.input(self.OUT))
#     def start(self):
#         self.stopflag=False
#         self.thread.__init__(target=self.call)
#         self.thread.start()
#     def getstop(self):
#         return self.stopflag
#     def stop(self):
#         self.stopflag=True
#         while self.thread.isAlive(): 1
#         return self.thread.isAlive()
#     def setmode(self,mode):
#         self.stop()
#         self.mode = mode
#         self.start()
    def start(self):
        self.stopflag=False
        threading.Thread.__init__(self, target=self.target)
        self.setDaemon(True)
        threading.Thread.start(self)
    def getstop(self):
        return self.stopflag
    def stop(self):
        self.stopflag=True
        while threading.Thread.isAlive(self): 1
        return threading.Thread.isAlive(self)
    def setmode(self,mode):
        self.stop()
        self.mode=mode
        self.start()
##class FatherThread(threading.Thread):
#    def __init__(self, IN, OUT, thread_num=0, timeout=1.0):
#        super(FatherThread, self).__init__()
#        self.thread_num = thread_num
#        self.stopped = False
#        self.timeout = timeout
#    def run(self):
#        def call():
#            if self.mode == 1:
#                while True:
#                    listen(self.IN) 
#                    if self.flag: GPIO.output(self.OUT,GPIO.HIGH)
#                    else: GPIO.output(self.OUT,GPIO.LOW)
#                    self.flag = not(self.flag)
#                    time.sleep(0.05)
#            elif self.mode == 2:
#                while True:
#                    listen(self.IN)
#                    time.sleep(2)
#                    if self.flag: GPIO.output(self.OUT,GPIO.HIGH)
#                    else: GPIO.output(self.OUT,GPIO.LOW)
#                    self.flag = not(self.flag)
#                    time.sleep(0.05)
#            elif self.mode == 3:
#                while True:
#                    if GPIO.input(self.IN): GPIO.output(self.OUT,GPIO.HIGH)
#                    else: GPIO.output(self.OUT,GPIO.LOW)
#            else:
#                while True:
#                    if GPIO.input(self.IN): GPIO.output(self.OUT,GPIO.LOW)
#                    else: GPIO.output(self.OUT,GPIO.HIGH)
#        subthread=threading.Thread(target=call,args=())
#        subthread.setDaemon(True)
#        subthread.start()
#        while not self.stopped:
#            subthread.join(self.t
if __name__ == '__main__':
    a=control(7,8,10,1)
    a.start()
   # while True: 1
