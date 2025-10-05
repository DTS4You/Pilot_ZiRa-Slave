# Example showing use of HSV colors
import time
from libs.neopixel import Neopixel

numpix = 60
strip = Neopixel(numpix, 0, 2, "GRB")

hue = 0
while(True):
    color = strip.colorHSV(hue, 255, 150)
    strip.fill(color)
    strip.show()
    
    hue += 150