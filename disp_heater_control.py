# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

"""
This test will initialize the display using displayio and draw a solid green
background, a smaller purple rectangle, and some yellow text.
"""
import board
import busio
import digitalio
import terminalio
import displayio
import time

# Starting in CircuitPython 9.x fourwire will be a seperate internal library
# rather than a component of the displayio library
try:
    from fourwire import FourWire
except ImportError:
    from displayio import FourWire
from adafruit_display_text import label
from adafruit_st7789 import ST7789

# Release any resources currently in use for the displays
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

# Make the display context
splash = displayio.Group()
display.root_group = splash

color_bitmap = displayio.Bitmap(240, 240, 1)
color_palette = displayio.Palette(1)
color_palette[0] = 0x000000  # Bright Green

bg_sprite = displayio.TileGrid(color_bitmap, pixel_shader=color_palette, x=0, y=0)
splash.append(bg_sprite)


# Draw a label
text_group = displayio.Group(scale=3, x=10, y=20)
text = "TempA:"
text_area = label.Label(terminalio.FONT, text=text, color=0xFFFF00)
text_group.append(text_area)  # Subgroup for text scaling
splash.append(text_group)

text2_group = displayio.Group(scale=3, x=120, y=20)
text2 = "0"
text2_area = label.Label(terminalio.FONT, text=text2, color=0xFFFF00)
text2_group.append(text2_area)  # Subgroup for text scaling
splash.append(text2_group)

text3_group = displayio.Group(scale=3, x=185, y=20)
text3 = "C"
text3_area = label.Label(terminalio.FONT, text=text3, color=0xFFFF00)
text3_group.append(text3_area)  # Subgroup for text scaling
splash.append(text3_group)

textZ_group = displayio.Group(scale=3, x=10, y=60)
textZ = "TempZ:"
textZ_area = label.Label(terminalio.FONT, text=textZ, color=0x10FF00)
textZ_group.append(textZ_area)  # Subgroup for text scaling
splash.append(textZ_group)

textZ2_group = displayio.Group(scale=3, x=120, y=60)
textZ2 = "180"
textZ2_area = label.Label(terminalio.FONT, text=textZ2, color=0x10FF00)
textZ2_group.append(textZ2_area)  # Subgroup for text scaling
splash.append(textZ2_group)

textZ3_group = displayio.Group(scale=3, x=185, y=60)
textZ3 = "C"
textZ3_area = label.Label(terminalio.FONT, text=textZ3, color=0x10FF00)
textZ3_group.append(textZ3_area)  # Subgroup for text scaling
splash.append(textZ3_group)

textH_group = displayio.Group(scale=3, x=10, y=100)
textH = "HistP:"
textH_area = label.Label(terminalio.FONT, text=textH, color=0x10FF00)
textH_group.append(textH_area)  # Subgroup for text scaling
splash.append(textH_group)

textH2_group = displayio.Group(scale=3, x=120, y=100)
textH2 = "2"
textH2_area = label.Label(terminalio.FONT, text=textH2, color=0x10FF00)
textH2_group.append(textH2_area)  # Subgroup for text scaling
splash.append(textH2_group)

textH3_group = displayio.Group(scale=3, x=185, y=100)
textH3 = "C"
textH3_area = label.Label(terminalio.FONT, text=textH3, color=0x10FF00)
textH3_group.append(textH3_area)  # Subgroup for text scaling
splash.append(textH3_group)

textHM_group = displayio.Group(scale=3, x=10, y=140)
textHM = "HistM:"
textHM_area = label.Label(terminalio.FONT, text=textHM, color=0x10FF00)
textHM_group.append(textHM_area)  # Subgroup for text scaling
splash.append(textHM_group)

textHM2_group = displayio.Group(scale=3, x=120, y=140)
textHM2 = "1"
textHM2_area = label.Label(terminalio.FONT, text=textHM2, color=0x10FF00)
textHM2_group.append(textHM2_area)  # Subgroup for text scaling
splash.append(textHM2_group)

textHM3_group = displayio.Group(scale=3, x=185, y=140)
textHM3 = "C"
textHM3_area = label.Label(terminalio.FONT, text=textHM3, color=0x10FF00)
textHM3_group.append(textHM3_area)  # Subgroup for text scaling
splash.append(textHM3_group)

textG_group = displayio.Group(scale=3, x=10, y=180)
textG = "Heater:"
textG_area = label.Label(terminalio.FONT, text=textG, color=0xFFFFFF)
textG_group.append(textG_area)  # Subgroup for text scaling
splash.append(textG_group)

textG2_group = displayio.Group(scale=3, x=140, y=180)
textG2 = "ON"
textG2_area = label.Label(terminalio.FONT, text=textG2, color=0xFF0000)
textG2_group.append(textG2_area)  # Subgroup for text scaling
splash.append(textG2_group)

textC_group = displayio.Group(scale=3, x=10, y=220)
textC = "Press:"
textC_area = label.Label(terminalio.FONT, text=textC, color=0x0000FF)
textC_group.append(textC_area)  # Subgroup for text scaling
splash.append(textC_group)

textC2_group = displayio.Group(scale=3, x=120, y=220)
textC2 = "5.4"
textC2_area = label.Label(terminalio.FONT, text=textC2, color=0x0000FF)
textC2_group.append(textC2_area)  # Subgroup for text scaling
splash.append(textC2_group)

textC3_group = displayio.Group(scale=3, x=185, y=220)
textC3 = "bar"
textC3_area = label.Label(terminalio.FONT, text=textC3, color=0x0000FF)
textC3_group.append(textC3_area)  # Subgroup for text scaling
splash.append(textC3_group)


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
    text2_area.text = str(tempA)
    textZ2_area.text = str(tempZ)
    textH2_area.text = str(HistP)
    textHM2_area.text = str(HistM)

    if not JoyCenter.value:
        try:
            with open("tempZ.txt", "w") as fp:
                # do the C-to-F conversion here if you would like
                tempZ+=1
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
        print(f"JoyDown pressed. Global value: {HistP}")
        # Debounce delay (optional)
        time.sleep(0.1)

    if not JoyLeft.value:
        # Increase global value
        HistM -= 1
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
        print(f"Button A pressed. Global value: {tempZ}")
        # Debounce delay (optional)
        time.sleep(0.1)
    if not buttonB.value:
        # Increase global value
        tempZ += 1
        print(f"Button B pressed. Global value: {tempZ}")
        # Debounce delay (optional)
        time.sleep(0.1)
    if not buttonX.value:
        # Increase global value
        tempZ -= 1
        print(f"Button X pressed. Global value: {tempZ}")
        # Debounce delay (optional)
        time.sleep(0.1)
    if not buttonY.value:
        # Increase global value
        tempZ -= 10
        print(f"Button Y pressed. Global value: {tempZ}")
        # Debounce delay (optional)
        time.sleep(0.1)
    time.sleep(0.05)
# Tutaj pisz swój kod, młody padawanie ;-)
