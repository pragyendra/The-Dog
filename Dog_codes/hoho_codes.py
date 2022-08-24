from lx16a import *
from math import sin, cos
import numpy as np
import time

# This is the port that the controller board is connected to
# This will be different for different computers
# On Windows, try the ports COM1, COM2, COM3, etc...
# On Raspbian, try each port in /dev/
LX16A.initialize("/dev/ttyUSB0")

# There should two servos connected, with IDs 1 and 2
# If one isn't connected, an exception is thrown

class imma:
	def __init__(self):
		#notes
		#leg 1 - motor 1,2 front(+ve) + back(-ve)
		#leg 2 - motor 3,4 front(-ve) + back(+ve)
		#leg 3 - motor 5,6 front(-ve) + back(+ve)
		#leg 4 - motor 7,8 front(+ve) + back(-ve)

		#all legs straight
		self.straight = [108, 107, 156, 157, 157, 136, 89, 105]
		#be_humble
		self.humble = [0,0,0,0,0,0,0,0]
		self.humble[0] = self.straight[0] + 0
		self.humble[1] = self.straight[1] + 100
		self.humble[2] = self.straight[2] + 0
		self.humble[3] = self.straight[3] - 100
		self.humble[4] = self.straight[4] + 0
		self.humble[5] = self.straight[5] - 100
		self.humble[6] = self.straight[6] + 0
		self.humble[7] = self.straight[7] + 100

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

			self.servo_dir = [servo1, servo2, servo3, servo4, servo5, servo6, servo7, servo8]

		except ServoTimeout as e:
			print(f"Servo {e.ID} is not responding. Exiting...")
			exit()

def humble(dog):
	tim = 5000
	for i in range(len(dog.servo_dir)):
		dog.servo_dir[i].moveTimeWaitWrite(dog.humble[i],tim)
	for servo in dog.servo_dir:
		servo.moveStart()

def straight(dog):
	tim = 5000
	for i in range(len(dog.servo_dir)):
		dog.servo_dir[i].moveTimeWaitWrite(dog.straight[i],tim)
	for servo in dog.servo_dir:
		servo.moveStart()

dog = imma()

user_says = str(input("what to do: "))
string = user_says + "(" + "dog" + ")"
exec(string)
