import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

leds = [2, 3,4,17,27,22,10,9]


GPIO.setup([2, 3,4,17,27,22,10,9], GPIO.OUT)

for j in range (3):
    for i in range (len(leds)):
        GPIO.output(leds[i], 1)
        time.sleep(0.2)
        GPIO.output(leds[i], 0)
        
GPIO.output([2, 3,4,17,27,22,10,9], 0)
GPIO.cleanup()

# GPIO.setup(21, GPIO.OUT)
# GPIO.setup(24, GPIO.IN)

# while True:
#     GPIO.output(21, GPIO.input(24))