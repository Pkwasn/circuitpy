import time
import board
import busio
import adafruit_lis3dh

# MatrixPortal I2C Setup:
i2c = busio.I2C(board.SCL, board.SDA)
lis3dh = adafruit_lis3dh.LIS3DH_I2C(i2c, address=0x19)

# Set range of accelerometer (can be RANGE_2_G, RANGE_4_G, RANGE_8_G or RANGE_16_G).
lis3dh.range = adafruit_lis3dh.RANGE_2_G

# First parameter is single or double tap (1 for single, 2 for double)
# Secibd parameter is the threshold of the tap (How strong of a tap)
lis3dh.set_tap(2, 60)

while True:
	if lis3dh.tapped:
		print("Tapped!")
		time.sleep(0.1)
