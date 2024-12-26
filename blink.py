from machine import Pin, Timer
import time
led = Pin(15, Pin.OUT)
led0 = Pin("LED", Pin.OUT)
button = Pin(14, Pin.IN, Pin.PULL_DOWN)
button2 = Pin(13, Pin.IN, Pin.PULL_DOWN)

timer = Timer()
led.value(0)
led0.value(0)
started = False

def blink(timer):
    if started:
        led.toggle()
        led0.toggle()
    
timer.init(freq=4, mode=Timer.PERIODIC, callback=blink)
        
while True:
    if button.value() and not started:
        started = True
        print("START")
    if button2.value() and started:
        started = False
        led.value(0)
        led0.value(0)
        print("STOP")


            