import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BCM)

GPIO.setup(24, GPIO.OUT)
# GPIO.setwarnings(False)

p = GPIO.PWM(24, 1000)
p.start(0)
try:
    while 1>0:
        n = int(input('Введите желаемый коэффициент заполнения: '))
        if n > 100:
            break
        p.start(n)
        print('Предполагаемое значение напряжения на выходе RC-цепи = ',(n*3.3/100))

        
finally:
    GPIO.output(24, 0)
    
    GPIO.cleanup()