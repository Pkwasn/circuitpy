import time
import board
import busio
import adafruit_lis3dh


# MatrixPortal I2C Setup:
i2c = busio.I2C(board.SCL, board.SDA)
lis3dh = adafruit_lis3dh.LIS3DH_I2C(i2c, address=0x19)

# Set range of accelerometer (can be RANGE_2_G, RANGE_4_G, RANGE_8_G or RANGE_16_G).
lis3dh.range = adafruit_lis3dh.RANGE_2_G

while True:
   	# The ".shake" function detects if the accelerometer is being shaken
    if lis3dh.shake(shake_threshold=15):
	# shake_threshold has a minimum value of 10, anything below will always report being shaken
        print("Shaken")
	
	
