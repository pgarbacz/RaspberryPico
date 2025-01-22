import displayio
import terminalio
from adafruit_display_text import label

class HMI:
    """
    This is used to create and operate of HMI implemented on display with SPI interface

    Attributes:
        width: display width in pixels
        height: display height in pixels

    Methods:
        method1: Description of method1
        method2: Description of method2
    """
    def __init__(self, display, width, height, bgcolor=0x000000 ): 
        self.width = width
        self.height = height
        self._cols = 3
        self._rows = 5
        self.posX=[10, 125, 190]
        self.posY=[20, 60, 100, 140, 180, 220]
        self.splash = displayio.Group()
        display.root_group = self.splash

        color_bitmap = displayio.Bitmap(self.width, self.height, 1)
        color_palette = displayio.Palette(1)
        color_palette[0] = bgcolor

        bg_sprite = displayio.TileGrid(color_bitmap, pixel_shader=color_palette, x=0, y=0)

        dgrid = [[0 for _ in range( self._cols)] for _ in range(self._rows)]
        self.dgrid = dgrid
        self.splash.append(bg_sprite)
        
        

    def add_parameter(self, row, name, value, unit, lcolor=0xFFFFFF):
        



        text_group = displayio.Group(scale=3, x=self.posX[0], y=self.posY[row])
        text_area = label.Label(terminalio.FONT, text=name, color=lcolor)
        text_group.append(text_area)  # Subgroup for text scaling
        self.splash.append(text_group)

        text2_group = displayio.Group(scale=3, x=self.posX[1],y=self.posY[row])
        text2_area = label.Label(terminalio.FONT, text=value, color=lcolor)
        text2_group.append(text2_area)  # Subgroup for text scaling
        self.splash.append(text2_group)

        text3_group = displayio.Group(scale=3, x=self.posX[2], y=self.posY[row])
        text3_area = label.Label(terminalio.FONT, text=unit, color=lcolor)
        text3_group.append(text3_area)  # Subgroup for text scaling
        self.splash.append(text3_group)
        
        return text2_area