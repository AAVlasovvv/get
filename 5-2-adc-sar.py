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