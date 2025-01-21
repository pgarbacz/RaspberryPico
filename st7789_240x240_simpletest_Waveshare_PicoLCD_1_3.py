# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

"""
This test will initialize the display using displayio and draw a solid green
background, a smaller purple rectangle, and some yellow text.
"""
import board
import busio
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
text_group = displayio.Group(scale=4, x=10, y=20)
text = "Akt. Temp. - "
text_area = label.Label(terminalio.FONT, text=text, color=0xFFFF00)
text_group.append(text_area)  # Subgroup for text scaling
splash.append(text_group)

text2_group = displayio.Group(scale=4, x=180, y=20)
text2 = "_"
text2_area = label.Label(terminalio.FONT, text=text2, color=0xFFFF00)
text_group.append(text_area)  # Subgroup for text scaling
splash.append(text_group)
count=0
while True:
    count+=1
    time.sleep(1)
    text2_area.text = str(count)
    pass
