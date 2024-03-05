import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

dac = [8,11,7,1,0,5,12,6]
number = [0]*len(dac)

GPIO.setup([8,11,7,1,0,5,12,6], GPIO.OUT)
number = [1,0,1,1,0,0,1,0]
GPIO.output(dac, number)
time.sleep(1)

number = [0,0,0,0,0,0,1,0] #2
GPIO.output(dac, number)
time.sleep(10)
number = [1,1,1,1,1,1,1,1] #255
GPIO.output(dac, number)
time.sleep(10)
number = [0,1,1,1,1,1,1,1] #127
GPIO.output(dac, number)
time.sleep(10)
number = [0,1,0,0,0,0,0,0] #64
GPIO.output(dac, number)
time.sleep(10)
number = [0,0,1,0,0,0,0,0] #32
GPIO.output(dac, number)
time.sleep(10)
number = [0,0,0,0,0,1,0,1] #5
GPIO.output(dac, number)
time.sleep(10)
number = [0,0,0,0,0,0,0,0] #0
GPIO.output(dac, number)
time.sleep(10)
# number = [1,0,1,1,0,0,1,0] #256
# time.sleep(20)













GPIO.output(dac, 0)
GPIO.cleanup()