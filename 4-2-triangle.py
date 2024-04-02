import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BCM)
dac = [8,11,7,1,0,5,12,6]
GPIO.setup(dac, GPIO.OUT)
def dec2bin(n):
    n = format(n, 'b')
    return n

t = float(input('Введите желаемый период треугольного сигнала: '))

try:
    while 1>0:
        n = 0
        while n <= 255:
            b = dec2bin(n)
            number = [int(i) for i in str(b)]
            for j in range(8-len(number)):
                number = [0] + number

            GPIO.output(dac, number)
            n += 1
            time.sleep(t/512)
        n -= 1
        while n>0:
            b = dec2bin(n)
            number = [int(i) for i in str(b)]
            for j in range(8-len(number)):
                number = [0] + number

            GPIO.output(dac, number)
            n -= 1
            time.sleep(t/512)
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()