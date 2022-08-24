from lx16a import *
from math import sin, cos
import math
import numpy as np
import time
import colorama
from colorama import Fore
from colorama import Style
import time
import moves_disc

# This dog is a property of Pragyendra and Prince
# if found missing please return to Columbia University
# They were instrumental in making it
# P.S. The 3D Printers in Makerspace are always Busy
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
		self.straight = [108, 107, 156, 157, 157, 136, 89, 105]
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

		self.stand2 = [72,203,200,54,188,37,55,205]

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


#dog sits
def humble(dog):						#time = 1.5 sec (1.7 + 1.5)
	if dog.current_pos =="humble":
		return
	elif dog.current_pos =="straight":
		stand(dog)
		time.sleep(1.7)
	else:
		pass
	tim = 1500
	for i in range(len(dog.servo_dir)):
		dog.servo_dir[i].moveTimeWrite(dog.humble[i],tim)
	dog.current_pos = "humble"

#complete straight Position
def straight(dog):						#time = 2 sec (1.9 + 2 sec)
	if dog.current_pos == "straight":
		return
	elif dog.current_pos == "humble":
		stand(dog)
		time.sleep(1.9)
	else:
		pass
	tim = 2000
	for i in range(len(dog.servo_dir)):
		dog.servo_dir[i].moveTimeWrite(dog.straight[i],tim)
	dog.current_pos = "straight"

#standing postion #ready to do tasks
def stand(dog):							#time = 2 sec
	tim = 1500
	for i in range(len(dog.servo_dir)):
		dog.servo_dir[i].moveTimeWrite(dog.stand[i],tim)
	dog.current_pos = "stand"

#secondary stand position to make steps (maybe required)
def stand2(dog):							#time = 2 sec
	tim = 1000
	for i in range(len(dog.servo_dir)):
		dog.servo_dir[i].moveTimeWrite(dog.stand2[i],tim)
	dog.current_pos = "stand2"

#handy function to check postions of each motor
def give_pos(dog):
	id = str(input(("motor ids: "))).lower()
	# try:
	if id == "all":
		ido = np.arange(1, len(dog.servo_dir)+1, 1)
	elif id == "quit":
		return
	else:
		string ="["+id+ "]"
		ido = eval(string)
	for i in ido:
		print("Position of motor id: ", str(i) , dog.servo_dir[i-1].getPhysicalPos())
	# except:
	# 	print("Incorrect Entry")
	# 	print("Enter motor ids in the format:","1,2,3")
	# 	give_pos(dog)

#def walk
def walk(dog):
	# if dog.current_pos != "stand2":				#initally go to stand then start walking
	# 	stand2(dog)
	# 	time.sleep(2.5)
	# else:
	# 	pass
	t = 0
	dt = 0.05
	hoho = 0
	while t < 50:
		for i in [0]:
			dog.servo_dir[i].moveTimeWrite(((sin(t))*dog.front[i]*20) + dog.stand2[i])
			if sin(t)>=0:
				dog.servo_dir[i+1].moveTimeWrite(((sin(2*t))*(dog.front[i+1])*10) + dog.stand2[i+1])
			elif sin(t)<0:
				if hoho == 0:
					hoho = dog.servo_dir[i+1].getPhysicalPos()
				else:
					pass
				dog.servo_dir[i+1].moveTimeWrite(((sin((t/1.5) + (math.pi/6))*(-dog.front[i+1])*15) + hoho))
			time.sleep(0.05)
		time.sleep(0.05)
		t+= dt


#turns the power on/off to the given motors
def power(dog, off= None):
	if off:
		if off == "off":
			for i in range(len(dog.servo_dir)):
				dog.ID = i + 1
				LX16A.loadOrUnloadWrite(dog,0)
		return
	else:
		pass
	command = ["off", "on"]
	#turn on/off the motor for given id
	def turn (dog, switch):
		input_string = "Enter motor id to turn it "+ command[switch]+": "
		user_says3 = input(input_string)
		try:
			if user_says3.lower() == "all":
				for i in range(len(dog.servo_dir)):
					dog.ID = i+1
					LX16A.loadOrUnloadWrite(dog,switch)
					print("Motor Id", dog.ID, "is now turned", command[switch])
			elif user_says3.lower() == "quit":
				return
			else:
				dog.ID = int(user_says3)
				LX16A.loadOrUnloadWrite(dog,switch)
				print("Motor Id", dog.ID, "is now turned", command[switch])
		except:
			print("Something went wrong")
			print("try again")
			power(dog)

	user_says2 = input("on/Off:").lower()
	if user_says2 == "on":
		switch = 1
		turn(dog, switch)
	elif user_says2 == "off":
		switch = 0
		turn(dog, switch)
	elif user_says2 == "quit":
		return
	else:
		print("Incorrect Entry")
		print("Enter the power switch in the format:", "on", "OR", "off")
		power(dog)

#returns mean comments on wrong input
def nope(dog):
	print("It's you not me!")
	print("You've said Something wrong")
	print("But I will give you one more chance")

#move the given motor to given positon
def move_to(dog):
	try:
		motor_id = input("Enter Motor id: ")
		if motor_id == "quit":
			return
		else:
			try:
				motor_id = int(motor_id)
			except:
				nope(dog)
		pos = input("Final Positon: ")
		if pos == "quit":
			return
		else:
			try:
				pos = int(pos)
			except:
				nope(dog)
		tim = 1500
		dog.servo_dir[motor_id - 1].moveTimeWrite(pos, tim)
		print("The motor", motor_id, "is now at", pos)
	except:
		nope(dog)

#moves the robot by a given angle and direction
def move_by(dog):
	try:
		motor_id = input("Enter Motor id: ")
		if motor_id == "quit":
			return
		else:
			try:
				motor_id = int(motor_id)
			except:
				nope(dog)
		side = input("Direction: ")
		if side == "quit":
			return
		else:
			if side == "front":
				sign = 1
			elif side == "back":
				sign = -1
			else:
				nope(dog)
				move_by(dog)
		pos = input("Position: ")
		if pos == "quit":
			return
		else:
			try:
				pos = int(pos)
			except:
				nope(dog)
		tim = 1500
		pos = dog.servo_dir[motor_id - 1].getPhysicalPos() + (dog.front[motor_id - 1]*sign*pos)
		dog.servo_dir[motor_id - 1].moveTimeWrite(pos, tim)
		print("The motor", motor_id, "is now at", pos)
	except:
		nope(dog)


def move_multi(dog):
	enter_ids = str(input("Enter motor ids: ")).lower()
	string = "[" + enter_ids + "]"
	ids = eval(string)
	pos= []
	for i in ids:
		string = "Enter the position for" + str(i) +": "
		enter_pos = int(input(string))
		pos.append(enter_pos)
	for i in range(len(ids)):
		tim = 1500
		dog.servo_dir[ids[i]-1].moveTimeWrite(pos[i], tim)

def hey_dog(dog):



def twerk(dog):
	stand(dog)
	time.sleep(1.1)
	step = 0
	up = 0
	while step < 10:
		if up == 0:
			for i in [0,1,2,3]:
				dog.servo_dir[i].moveTimeWrite(dog.stand[i],200)
			for i in [4,5,6,7]:
				dog.servo_dir[i].moveTimeWrite(dog.stand2[i],200)
			up = 1
			time.sleep(0.6)
		else:
			for i in [0,1,2,3]:
				dog.servo_dir[i].moveTimeWrite(dog.stand[i],200)
			for i in [4,5,6,7]:
				dog.servo_dir[i].moveTimeWrite(dog.stand[i],200)
			up = 0
			time.sleep(0.6)
		step +=1

#boot up
def boot_up(dog):
	print("Booting up...")
	for i in range(len(dog.servo_dir)):
		servo = dog.servo_dir[i]
		id = servo.IDRead() -1
		max_volt = servo.vInLimitRead()
		volt = servo.vInRead()
		max_temp = servo.tempMaxLimitRead()
		temp = servo.tempRead()
		if i == id:
			if max_volt[0]<=volt<=max_volt[1]:
				if temp<=max_temp:
					print(Fore.GREEN + "Servo id",i+1,"is healthy"+ Style.RESET_ALL)
				else:
					print(Fore.RED + "Servo id",i+1,"is above maximum legal temperature"+ Style.RESET_ALL)
			else:
				print(Fore.RED + "Servo id",i+1,"is outside legal voltage limits"+ Style.RESET_ALL)
		else:
			print(Fore.RED + "Servo id",i+1,"is misidentified"+ Style.RESET_ALL)
		wait(2)
	print(Fore.GREEN + "- - - - - - - - - - - - - - - - - -" + Style.RESET_ALL)

def homing(dog):
	print(Fore.BLUE + "Initiating Homing Sequence . . ."+ Style.RESET_ALL)
	wait(2)
	humble(dog)
	stand(dog)
	print(Fore.BLUE + "DONE" + Style.RESET_ALL)
	print(Fore.BLUE + "- - - - - - - - - - - - - - - - - -" + Style.RESET_ALL)

def shutdown(dog):
	print(Fore.BLUE + "Initiating shutdown sequence . . .")
	humble(dog)
	time.sleep(3.2)
	power(dog, "off")
	wait(2)

def undo(dog):
	array_position(dog, last_pos)
def redo(dog):
	array_position(dog, new_pos)

def array_position(dog, array):
	for i in range(len(dog.servo_dir)):
		dog.servo_dir[i].moveTimeWrite(array[i], 1000)

#create the class of data
dog = imma()

def wait(end):
	start = time.time()
	while time.time() - start < end:
		continue

def start():
	print("This  property belongs to Pragyendra and Prince")
	wait(4)
	print("if found missing please return to Columbia University")
	wait(4)
	print("They were instrumental in building it")
	wait(4)
	print("P.S. The 3D Printers in Makerspace are always Busy")
	wait(6)
	print("Lets start")
	print("- - - - - - - - - - - - - - - - - -")


#starting credits
# start()
#booting sequence
# boot_up(dog)
# homing(dog)

# global last_pos
# global new_pos
# last_pos = hoho_position(dog)
# new_pos = hoho_position(dog)


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
