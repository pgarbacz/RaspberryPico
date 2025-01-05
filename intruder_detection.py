from machine import Pin, Timer,PWM
import utime
import random
from gpio_lcd import GpioLcd
import time
activated = [False for i in range(8)]
# Create the LCD object
lcd = GpioLcd(rs_pin=Pin(16),
              enable_pin=Pin(17),
              d4_pin=Pin(18),
              d5_pin=Pin(19),
              d6_pin=Pin(20),
              d7_pin=Pin(21),
              num_lines=2, num_columns=16) 
detection = 0



# Initialize PIR sensor on GPIO 0
pir = Pin(0, Pin.IN, Pin.PULL_DOWN)
led = Pin(15, Pin.OUT) # Initialize LED on GPIO 15
buzzer = PWM(Pin(14))# Initialize Buzzer on GPIO 14
buzzer.freq(500)
pir_state = False # Start assuming no motion detected
last_motion_time = 0 # Timestamp of the last motion detected
debounce_time = 3 # Debounce period in seconds

lcd.putstr('Alarm ready!')
utime.sleep_ms(2000)
lcd.move_to(0,1)
lcd.putstr("Detection: {0}".format(detection))

utime.sleep_ms(2000)#clear screen needs a long delay


 # play the middle c for half a second


while True:
    val = pir.value() # Read input value from PIR sensor
    current_time = time.time()

    if val == 1: # Motion detected
        if not pir_state and (current_time - last_motion_time >= debounce_time):
            print(current_time - last_motion_time)
            lcd.move_to(0,1)
            detection+=1
            lcd.putstr("Detection: {0}".format(detection))
            pir_state = True
            led.on() # Turn on LED
            buzzer.duty_u16(500)
            utime.sleep_ms(1000)
            buzzer.duty_u16(0)
            last_motion_time = current_time # Update the last motion timestamp

    elif val == 0:
        if pir_state and (current_time - last_motion_time >= debounce_time):
            pir_state = False
            led.off()
            last_motion_time = current_time # Update the last motion timestamp

            time.sleep(0.1) # Small delay to prevent spamming

    if Pin(7, Pin.IN, Pin.PULL_DOWN).value():
        #Turn OFF alarm
        print("Turn of sound")
    utime.sleep_ms(20)

    

