from lx16a import *
from math import sin, cos
import time

# This is the port that the controller board is connected to
# This will be different for different computers
# On Windows, try the ports COM1, COM2, COM3, etc...
# On Raspbian, try each port in /dev/
LX16A.initialize("/dev/ttyUSB0")

# There should two servos connected, with IDs 1 and 2
# If one isn't connected, an exception is thrown
try:
	#leg 1
	servo1 = LX16A(1)
	servo2 = LX16A(2)
	#leg 2
	servo3 = LX16A(3)
	servo4 = LX16A(4)
	#leg 3
	servo5 = LX16A(5)
	servo6 = LX16A(6)
	#leg 4
	servo7 = LX16A(7)
	servo8 = LX16A(8)

except ServoTimeout as e:
	print(f"Servo {e.ID} is not responding. Exiting...")
	exit()

t = 0

while True:
	# Two sine waves out of phase
	# The servos can rotate between 0 and 240 degrees,
	# So we adjust the waves to be in that range
	servo1.moveTimeWrite(sin(t) * 50 + 120)
	servo2.moveTimeWrite(cos(t) * 50 + 120)
	time.sleep(0.05)

	t += 0.05
