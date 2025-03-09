# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT
import MAX31865_heater_control_circuitpython as heater
import board
import busio
import digitalio
import displayio
import time
from hmi import HMI

# Starting in CircuitPython 9.x fourwire will be a seperate internal library
# rather than a component of the displayio library
try:
    from fourwire import FourWire
except ImportError:
    from displayio import FourWire
from adafruit_display_text import label
from adafruit_st7789 import ST7789

displayio.release_displays()

tft_dc = board.GP8
tft_cs = board.GP9
spi_clk = board.GP10
spi_mosi = board.GP11
tft_rst = board.GP12
backlight = board.GP13
spi = busio.SPI(spi_clk, spi_mosi)

display_bus = FourWire(spi, command=tft_dc, chip_select=tft_cs, reset=tft_rst)

display = ST7789(
    display_bus,
    rotation=270,
    width=240,
    height=240,
    rowstart=80,
    backlight_pin=backlight,
)

hmi = HMI(display, 240, 240)

tempA_value = hmi.add_parameter(0, "TempA:", "0", "C", 0xFFFF00)
tempZ_value = hmi.add_parameter(1, "TempZ:", "180", "C", 0x10FF00)
histP_value = hmi.add_parameter(2, "HistP:", "2", "C", 0x10FF00)
histM_value = hmi.add_parameter(3, "HistM:", "1", "C", 0xFFFFFF)
relay_value = hmi.add_parameter(4, "Relay:", "ON", "", 0xFF0000)
press_value = hmi.add_parameter(5, "Press:", "5.4", "bar", 0x0000FF)

print("Go")
buttonA = digitalio.DigitalInOut(board.GP15)
buttonA.direction = digitalio.Direction.INPUT
buttonA.pull = digitalio.Pull.UP
buttonB = digitalio.DigitalInOut(board.GP17)
buttonB.direction = digitalio.Direction.INPUT
buttonB.pull = digitalio.Pull.UP
buttonX = digitalio.DigitalInOut(board.GP19)
buttonX.direction = digitalio.Direction.INPUT
buttonX.pull = digitalio.Pull.UP
buttonY = digitalio.DigitalInOut(board.GP21)
buttonY.direction = digitalio.Direction.INPUT
buttonY.pull = digitalio.Pull.UP

JoyUp = digitalio.DigitalInOut(board.GP2)
JoyUp.direction = digitalio.Direction.INPUT
JoyUp.pull = digitalio.Pull.UP

JoyDown = digitalio.DigitalInOut(board.GP18)
JoyDown.direction = digitalio.Direction.INPUT
JoyDown.pull = digitalio.Pull.UP

JoyLeft = digitalio.DigitalInOut(board.GP16)
JoyLeft.direction = digitalio.Direction.INPUT
JoyLeft.pull = digitalio.Pull.UP

JoyRight = digitalio.DigitalInOut(board.GP20)
JoyRight.direction = digitalio.Direction.INPUT
JoyRight.pull = digitalio.Pull.UP

JoyCenter = digitalio.DigitalInOut(board.GP3)
JoyCenter.direction = digitalio.Direction.INPUT
JoyCenter.pull = digitalio.Pull.UP

led = digitalio.DigitalInOut(board.LED)
# For QT Py M0:
# led = digitalio.DigitalInOut(board.SCK)
led.switch_to_output()
tempZ = int(200)  # default value
tempMax = 300

try:
    with open("tempZ.txt", "r") as fp:
        
        line = fp.readline()
        #print(line)
        tempR = line[:3]
        if tempR.isdigit():  # Check if the string consists of only digits
            tempZ = int(tempR.strip())
            print(tempZ)
            
        else:
            print("Invalid input: String contains non-numeric characters.")
        led.value = not led.value
        time.sleep(1)
except OSError as e:  # Typically when the filesystem isn't writeable...
    delay = 0.5  # ...blink the LED every half second.
    print(e)
    if e.args[0] == 28:  # If the file system is full...
        delay = 0.25  # ...blink the LED faster!
        print(e.args[0])
        # while True:
        # led.value = not led.value
        time.sleep(delay)


HistM = 2
HistP = 1
tempA = 25
while True:
    tempA_value.text = str(tempA)
    tempZ_value.text = str(tempZ)
    histP_value.text = str(HistP)
    histM_value.text = str(HistM)
    
    heater.control(tempA, tempZ, HistM, HistP)

    if not JoyCenter.value:
        try:
            with open("tempZ.txt", "w") as fp:
                # do the C-to-F conversion here if you would like
                print(tempZ)
                fp.write("{0}".format(tempZ))
                fp.flush()
                led.value = not led.value
                time.sleep(1)
        except OSError as e:  # Typically when the filesystem isn't writeable...
            delay = 0.5  # ...blink the LED every half second.
            print(f"OSError")
            if e.args[0] == 28:  # If the file system is full...
                delay = 0.25  # ...blink the LED faster!
        print(f"JoyCenter pressed. Settings Updated")
        # Debounce delay (optional)
        time.sleep(0.1)

    if not JoyUp.value:
        # Increase global value
        HistP += 1
        print(f"JoyUp pressed. Global value: {HistP}")
        # Debounce delay (optional)
        time.sleep(0.1)
    if not JoyDown.value:
        # Increase global value
        HistP -= 1
        if HistP<0:
            HistP=0
        print(f"JoyDown pressed. Global value: {HistP}")
        # Debounce delay (optional)
        time.sleep(0.1)

    if not JoyLeft.value:
        # Increase global value
        HistM -= 1
        if HistM<0:
            HistM=0
        print(f"JoyLeft pressed. Global value: {HistM}")
        # Debounce delay (optional)
        time.sleep(0.1)

    if not JoyRight.value:
        # Increase global value
        HistM += 1
        print(f"JoyLeft pressed. Global value: {HistM}")
        # Debounce delay (optional)
        time.sleep(0.1)
    if not buttonA.value:
        # Increase global value
        tempZ += 10
        if tempZ>tempMax:
            tempZ=tempMax
        print(f"Button A pressed. Global value: {tempZ}")
        # Debounce delay (optional)
        time.sleep(0.1)
    if not buttonB.value:
        # Increase global value
        tempZ += 1
        if tempZ>tempMax:
            tempZ=tempMax
        print(f"Button B pressed. Global value: {tempZ}")
        # Debounce delay (optional)
        time.sleep(0.1)
    if not buttonX.value:
        # Increase global value
        tempZ -= 1
        if tempZ<=0:
            tempZ=0
        print(f"Button X pressed. Global value: {tempZ}")
        # Debounce delay (optional)
        time.sleep(0.1)
    if not buttonY.value:
        # Increase global value
        tempZ -= 10
        if tempZ<=0:
            tempZ=0
        print(f"Button Y pressed. Global value: {tempZ}")
        # Debounce delay (optional)
        time.sleep(0.1)
    time.sleep(0.05)
# Tutaj pisz swój kod, młody padawanie ;-)
