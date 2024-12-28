from machine import Pin, Timer
import utime
import random
from gpio_lcd import GpioLcd

activated = [False for i in range(8)]
# Create the LCD object
lcd = GpioLcd(rs_pin=Pin(16),
              enable_pin=Pin(17),
              d4_pin=Pin(18),
              d5_pin=Pin(19),
              d6_pin=Pin(20),
              d7_pin=Pin(21),
              num_lines=2, num_columns=16) 


def get_new_number():
    return random.randint(0,255)

def test_answer(num, bits):
    answer = 0
    for i in range(8):
        if bits[i]:
            answer += 2**i
    print(answer, num)
    if answer == num:
        return True
    else:
        return False
    
def update_task(number, total):
    
    lcd.clear()
    lcd.move_to(0,0)
    line1 = "Dec Number:{0}".format(number)
    lcd.putstr(line1)
    lcd.move_to(0,1)
    line2 = "Your score:{0}".format(total)
    lcd.putstr(line2)
    return cn

lcd.putstr('Hello!')
utime.sleep_ms(2000)
lcd.move_to(0,1)
lcd.putstr("Let's play!")

utime.sleep_ms(2000)#clear screen needs a long delay
score = 0
b_next_task = False
cn = get_new_number()
update_task(cn, score)


while True:
    utime.sleep_ms(20)
    if b_next_task:
        score+=1
        cn = get_new_number()
        update_task(cn, score)
        b_next_task = False
    for i in range(8):
        if Pin(i, Pin.IN, Pin.PULL_DOWN).value():
            if not activated[i]:
                Pin(i+8, Pin.OUT).value(1)
                activated[i]=True
                print(activated)
                utime.sleep_ms(500)
                b_next_task = test_answer(cn, activated[::-1])
                break
            if activated[i]:
                Pin(i+8, Pin.OUT).value(0)
                activated[i]=False
                print(activated)
                utime.sleep_ms(500)
                break

