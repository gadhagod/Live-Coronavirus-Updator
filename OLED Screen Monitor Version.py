#thanks so adafruit for base code
import host
import time
import requests

import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

import subprocess

RST = None
DC = 23
SPI_PORT = 0
SPI_DEVICE = 0

disp = Adafruit_SSD1306.SSD1306_128_32(rst=RST)
disp.begin()
disp.clear()
disp.display()

width = disp.width
height = disp.height
image = Image.new('1', (width, height))
draw = ImageDraw.Draw(image)
draw.rectangle((0,0,width,height), outline=0, fill=0)

padding = -2
top = padding
bottom = height-padding
x = 0

font = ImageFont.load_default()

while True:
    draw.rectangle((0,0,width,height), outline=0, fill=0)

    deaths1 = "Deaths: " + str(deaths())
    cases1 = "Cases: " + str(cases())
    recoveries1 = "Recovered: " + str(recoveries())

    draw.text((x, top), deaths1,  font=font, fill=255)
    draw.text((x, top+10), cases1, font=font, fill=255)
    draw.text((x, top+20), recoveries1,  font=font, fill=255)

    disp.image(image)
    disp.display()
    time.sleep(.1)