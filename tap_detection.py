import time
import board
import busio
import adafruit_lis3dh

# MatrixPortal I2C Setup:
i2c = busio.I2C(board.SCL, board.SDA)
lis3dh = adafruit_lis3dh.LIS3DH_I2C(i2c, address=0x19)

# Set range of accelerometer (can be RANGE_2_G, RANGE_4_G, RANGE_8_G or RANGE_16_G).
lis3dh.range = adafruit_lis3dh.RANGE_16_G

# First parameter is single or double tap (0 to disable taps, 1 for single, 2 for double)
# Secibd parameter is the threshold of the tap (How strong of a tap)
lis3dh.set_tap(1, 10)

#  - 2G = 40-80 threshold
#  - 4G = 20-40 threshold
#  - 8G = 10-20 threshold
#  - 16G = 5-10 threshold

print("Try tapping")
while True:
    if lis3dh.tapped:
        print("Tapped!")
        time.sleep(0.01)
    else:
        pass
