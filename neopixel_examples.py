import time
import board
from rainbowio import colorwheel
import neopixel

#Initialize board NeoPixel
NEOPIXEL = neopixel.NeoPixel(board.NEOPIXEL, 1, brightness=0.04, auto_write=True)

# Colors, can be anything in between these values
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

# Rainbow LED
# If the NeoPixel brightness is too low, it cannot transition between colors, just 
# flashes RGB instead of everything in between
i = 0
while True:
    i = (i + 1) % 256 # run from 0 to 255
    NEOPIXEL.fill(colorwheel(i))
    time.sleep(0.01)

# auto_write = false
while True:
	NEOPIXEL.fill(RED)
	NEOPIXEL.show()	# Updates NeoPixel, auto_write calls this function automaticlaly once a color is set
	time.sleep(0.01)
