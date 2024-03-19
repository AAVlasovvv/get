import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BCM)

dac = [8,11,7,1,0,5,12,6]
GPIO.setup(dac, GPIO.OUT)
def binary(n):
    n = format(n, 'b')
    return n
def volt(n):
    u = n/256*3.3
    print('Предполагаемое напряжение на ЦАП =', u, 'В')
try:
    while 1>0:
        n = (input("Введите число от 0 до 255: "))
        if n == 'q':
            break
        try:
            n = float(n)
        except ValueError:
            print('Вы ввели не число')
            break
        if float(n)%1 != 0:
            print('Вы ввели не целое число')
            break
        if float(n) < 0:
            print('Вы ввели отрицательное число')
            break
        if float(n) > 255:
            print('Вы значение превышающее возможности 8-разрядного ЦАП')
            break
        n = int(n)
        volt(n)
        n = binary(n)
        number = [int(i) for i in str(n)]
        for j in range(8-len(number)):
            number = [0] + number

        GPIO.output(dac, number)
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()