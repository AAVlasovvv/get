import RPi.GPIO as gpio

from time import sleep
gpio.setmode(gpio.BCM)
dac = [8,11,7,1,0,5,12,6]
leds = [9,10,22,27,17,4,3,2]
comp = 14
troyka = 13
gpio.setup(dac, gpio.OUT)
gpio.setup(leds, gpio.OUT)
gpio.setup(troyka, gpio.OUT, initial=gpio.HIGH)
gpio.setup(comp, gpio.IN)
def perev(a):
    return [int (elem) for elem in bin(a)[2:].zfill(8)]

def adc():
    k = 0
    for i in range(7, -1, -1):
        k += 2**i
        daccc = []
        daccc = perev(k)
        gpio.output(dac, daccc)
        sleep(0.001)
        compv = gpio.input(comp)
        if compv == gpio.HIGH:
            k -= 2**i
    return k

def volume(n):
    n = int(round(n/32,0))
    number = [0]*8
    for i in range(n):
        number[i]=1
    return number

try:
    while True:
        i = adc()
        
        # if i != 0:
        if i != None:
                    gpio.output(leds, volume(i))
                    print(i, '{:.2f}'.format(3.3*i/256))
        else: 
                    i = 255
                    gpio.output(leds, 3.3)
                    print(i, '{:.2f}'.format(3.3*i/256))

# except TypeError:
#     i = 256
#     print(i, '{:.2f}'.format(3.3*i/256))

finally:
    gpio.output(dac, 0)
    gpio.output(leds, 0)
    gpio.cleanup()