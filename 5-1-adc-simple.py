import RPi.GPIO as gpio

from time import sleep
gpio.setmode(gpio.BCM)
dac = [8,11,7,1,0,5,12,6]
comp = 14
troyka = 13
gpio.setup(dac, gpio.OUT)
gpio.setup(troyka, gpio.OUT, initial=gpio.HIGH)
gpio.setup(comp, gpio.IN)
def perev(a):
    return [int (elem) for elem in bin(a)[2:].zfill(8)]

def adc():
    for i in range(256):
        daccc = []
        daccc = perev(i)
        gpio.output(dac, daccc)
        compv = gpio.input(comp)
        sleep(0.001)
        if compv == gpio.HIGH:
            return i
          

try:
    while True:
        i = adc()
        
        if i != 0:
            if i != None:
                    
                    print(i, '{:.2f}'.format(3.3*i/256))
            else: 
                    i = 255
                    print(i, '{:.2f}'.format(3.3*i/256))

# except TypeError:
#     i = 256
#     print(i, '{:.2f}'.format(3.3*i/256))

finally:
    gpio.output(dac, 0)
    gpio.cleanup()