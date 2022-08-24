from lx16a import *
from math import sin, cos
import math
import numpy as np
import time
import colorama
from colorama import Fore
from colorama import Style
import time
from moves_disc import *


LX16A.initialize("/dev/ttyUSB0")

#class to create the basic positon and definition of the robot
class imma:
	def __init__(self):
		#notes
		self.current_pos = "hoho"
		self.uplinks = [1,3,5,7]
		self.downlinks = [2,4,6,8]
		#leg 1 - motor 1,2 front(+ve) + back(-ve)
		#leg 2 - motor 3,4 front(-ve) + back(+ve)
		#leg 3 - motor 5,6 front(-ve) + back(+ve)
		#leg 4 - motor 7,8 front(+ve) + back(-ve)
		#motor signs [1, 2,  3,  4,  5,  6, 7, 8]
		self.front = [1, 1, -1, -1, -1, -1, 1, 1]
		#all legs straight
		#hohotraceme  = [1    2    3    4    5    6    7   8  ]
		#self.straight = [108, 107, 156, 157, 157, 136, 89, 105]
		#self.straight = [108, 107, 156, 157, 157, 136, 89, 105]

		#be_humble
		self.humble = [0,0,0,0,0,0,0,0]
		diff = [0, 100, 0, 100, 0, 100, 0, 100]
		for i in range(len(self.humble)):
			self.humble[i] = self.straight[i] + (self.front[i]*diff[i])

		self.stand = [0,0,0,0,0,0,0,0]
		#motor		1	 2    3   4    5    6    7    8
		# diff = [56, -121, -58, 121, -46, -124, 50, -127]
		diff = [-56, 121, -58, 121, -46, 124, -50, 127]
		for i in range(len(self.stand)):
			self.stand[i] = self.straight[i] + (self.front[i]*diff[i])

		# self.stand2 = [72,203,200,54,188,37,55,205]
		self.stand2 = [72,203,192,56,188,39,55,205]

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
			self.ID = 0

		except ServoTimeout as e:
			print(f"Servo {e.ID} is not responding. Exiting...")
			exit()


#create the class of data
dog = imma()

#starting credits
# start()
#booting sequence
# boot_up(dog)
# homing(dog)


#start working from here
user_says = str(input("what to do: "))

#for debugging
while user_says != "quit":
	# try :
	string = user_says + "(" + "dog" + ")"
	# last_pos = hoho_positon(dog)
	exec(string)
	# new_pos = hoho_positon(dog)
	# except:
	# 	print("I'm sorry, I can't do that !")
	# print("- - - - - - - - - - - - - - - - - -")
	user_says = str(input("what to do: "))

shutdown(dog)
print("see ya! Happy Holidays")
