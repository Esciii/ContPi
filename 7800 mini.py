import RPi.GPIO as GPIO
import keyboard
import time

sleep = 0.00166
strb = 20
sclk = 16
d0 = 21

GPIO.setmode(GPIO.BCM)
GPIO.setup(sclk, GPIO.OUT)
#SCLK
GPIO.setup(strb, GPIO.OUT)
#STRB
GPIO.setup(d0, GPIO.IN)
#D0

while True:
    contr = 100000000
    time.sleep(sleep)
    GPIO.output(strb, True)
    time.sleep(sleep)
    GPIO.output(strb, False)
    GPIO.output(sclk, True)
    if GPIO.input(d0):
        contr = (contr + 0)
    else:
        contr = (contr + 1)
        keyboard.send('a')
    time.sleep(sleep)
    GPIO.output(sclk, False)
    time.sleep(sleep)
    GPIO.output(sclk, True)
    if GPIO.input(d0):
        contr = (contr + 0)
    else:
        contr = (contr + 10)
        keyboard.send('s')
    time.sleep(sleep)
    GPIO.output(sclk, False)
    time.sleep(sleep)
    GPIO.output(sclk, True)
    if GPIO.input(d0):
        contr = (contr + 0)
    else:
        contr = (contr + 100)
        keyboard.send('s')
    time.sleep(sleep)
    GPIO.output(sclk, False)
    time.sleep(sleep)
    GPIO.output(sclk, True)
    if GPIO.input(d0):
        contr = (contr + 0)
    else:
        contr = (contr + 1000)
        keyboard.send('w')
    time.sleep(sleep)
    GPIO.output(sclk, False)
    time.sleep(sleep)
    GPIO.output(sclk, True)
    if GPIO.input(d0):
        contr = (contr + 0)
    else:
        contr = (contr + 10000)
        keyboard.send('up')
    time.sleep(sleep)
    GPIO.output(sclk, False)
    time.sleep(sleep)
    GPIO.output(sclk, True)
    if GPIO.input(d0):
        contr = (contr + 0)
    else:
        contr = (contr + 100000)
        keyboard.send('down')
    time.sleep(sleep)
    GPIO.output(sclk, False)
    time.sleep(sleep)
    GPIO.output(sclk, True)
    if GPIO.input(d0):
        contr = (contr + 0)
    else:
        contr = (contr + 1000000)
        keyboard.send('left')
    time.sleep(sleep)
    GPIO.output(sclk, False)
    time.sleep(sleep)
    GPIO.output(sclk, True)
    if GPIO.input(d0):
        contr = (contr + 0)
    else:
        contr = (contr + 10000000)
        keyboard.send('right')
    print(contr)