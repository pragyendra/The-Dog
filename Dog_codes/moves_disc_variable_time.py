from lx16a import *
from math import sin, cos
import math
import numpy as np
import time
import colorama
from colorama import Fore
from colorama import Style
import simpleaudio as sa
import time

global rest_t
rest_t = 0.2

#dog sits
def humble(dog, tim=None):						#time = 1.5 sec (1.7 + 1.5)
	if dog.current_pos =="humble":
		return
	elif dog.current_pos =="straight":
		stand(dog)
	else:
		pass
	if tim:
		pass
	else:
		tim = 1500
	for i in range(len(dog.servo_dir)):
		dog.servo_dir[i].moveTimeWrite(dog.humble[i],tim)
	dog.current_pos = "humble"
	time.sleep((tim/1000) + rest_t)

#complete straight Position
def straight(dog, tim=None):						#time = 2 sec (1.9 + 2 sec)
	if dog.current_pos == "straight":
		return
	elif dog.current_pos == "humble":
		stand(dog)
	else:
		pass
	if tim:
		pass
	else:
		tim = 2000
	for i in range(len(dog.servo_dir)):
		dog.servo_dir[i].moveTimeWrite(dog.straight[i],tim)
	dog.current_pos = "straight"
	time.sleep((tim/1000) + rest_t)

#standing postion #ready to do tasks
def stand(dog, tim=None):
	if tim:
		pass
	else:							#time = 2 sec
		tim = 1500
	for i in range(len(dog.servo_dir)):
		dog.servo_dir[i].moveTimeWrite(dog.stand[i],tim)
	dog.current_pos = "stand"
	time.sleep((tim/1000) + rest_t)

#secondary stand position to make steps (maybe required)
def stand2(dog, tim=None):
	if tim:							#time = 2 sec
		pass
	else:
		tim = 1000
	for i in range(len(dog.servo_dir)):
		dog.servo_dir[i].moveTimeWrite(dog.stand2[i],tim)
	dog.current_pos = "stand2"
	time.sleep((tim/1000) + rest_t)

#handy function to check postions of each motor
def give_pos(dog):
	id = str(input(("motor ids: "))).lower()
	try:
		if id == "all":
			ido = np.arange(1, len(dog.servo_dir)+1, 1)
		elif id == "quit":
			return
		else:
			string ="["+id+ "]"
			ido = eval(string)
		for i in ido:
			print("Position of motor id: ", str(i) , dog.servo_dir[i-1].getPhysicalPos()-dog.straight[i-1])
	except:
		print("Incorrect Entry")
		print("Enter motor ids in the format:","1,2,3")
		give_pos(dog)

def right_round(dog, tim=None,stretch=None):
	if dog.current_pos != "stand2":				#initally go to stand then start walking
		stand2(dog)
	else:
		pass
	t = 0
	dt = 1
	hoho = 0
	if tim:
		pass
	else:
		tim = 100
	if stretch:
		pass
	else:
		stretch=50
	while t < stretch:
		for i in [1,3,5,7]:
			if i == 1:
				phi = 0
				move = 7
			elif i == 5:
				phi = math.pi
				move = 7
			elif i == 3:
				phi = math.pi/2
				move = 7
			elif i == 7:
				phi = (3*math.pi)/2
				move = 7
			else:
				continue
			dog.servo_dir[i].moveTimeWrite(((sin(t + phi))*(-dog.front[i])*move) + dog.stand2[i],tim)
		t += dt
		time.sleep((tim/1000))
	stand2(dog)
	dog.current_pos="stand2"

def right_round2(dog, tim=None,stretch=None):
	if dog.current_pos != "stand2":				#initally go to stand then start walking
		stand2(dog)
	else:
		pass
	t = 0
	dt = 1
	hoho = 0
	if tim:
		pass
	else:
		tim = 100
	if stretch:
		pass
	else:
		stretch=50
	while t < stretch:
		for i in [1,3,5,7]:
			if i == 3:
				phi = 0
				move = 7
			elif i == 7:
				phi = math.pi
				move = 7
			elif i == 1:
				phi = math.pi/2
				move = 7
			elif i == 5:
				phi = (3*math.pi)/2
				move = 7
			else:
				continue
			dog.servo_dir[i].moveTimeWrite(((sin(t + phi))*(-dog.front[i])*move) + dog.stand2[i],tim)
		t += dt
		time.sleep((tim/1000))
	stand2(dog)
	dog.current_pos="stand2"

def rev_walk(dog, tim=None, stretch=None):
	if dog.current_pos != "stand2":				#initally go to stand then start walking
		stand2(dog)
	else:
		pass
	if stretch:
		pass
	else:
		stretch=50
	t = 0
	dt = 1
	hoho = 0
	if tim:
		pass
	else:
		tim = 100
	while t < stretch:
		for i in [1,3,5,7,0,2,4,6]:
			if i == 1:
				phi = 0
				move = 7
				sign = -1
			elif i == 5:
				phi = math.pi/2
				move = 7
				sign = -1
			elif i == 3:
				phi = math.pi
				move = 7
				sign = -1
			elif i == 7:
				phi = math.pi
				move = 7
				sign = -1
			elif i==0:
				phi = 0
				move = 5
				sign = 1
			elif i==2:
				phi = math.pi
				move = 5
				sign = 1
			elif i==4:
				phi = math.pi/2
				move = 5
				sign = 1
			elif i==6:
				phi = math.pi
				move = 5
				sign = 1
			else:
				continue
			dog.servo_dir[i].moveTimeWrite(((sin(t + phi))*(sign*dog.front[i])*move) + dog.stand2[i],tim)
		t += dt
		time.sleep((tim/1000))
	stand2(dog)

#def walk
def walk(dog, tim=None,stretch=None):
	if dog.current_pos != "stand2":				#initally go to stand then start walking
		stand2(dog)
	else:
		pass
	if stretch:
		pass
	else:
		stretch=50
	t = 0
	dt = 1
	switch = 0
	if tim:
		pass
	else:
		tim = 100
	while t< stretch:
		for i in [0,4]:
			phi = 0
			move = 10
			sign = 1
			dog.servo_dir[i].moveTimeWrite(((sin(t + phi))*(sign*dog.front[i])*move) + dog.stand2[i],tim)
			move = 5
			if sin(t)>=0:
				i+=1
				sign = 1
				dog.servo_dir[i].moveTimeWrite(((sin(2*t + phi))*(sign*dog.front[i])*move) + dog.stand2[i],tim)
			elif sin(t)<0:
				i+=1
				switch = 1
				sign = -1
				dog.servo_dir[i].moveTimeWrite(((sin((2*t) + phi))*(sign*dog.front[i])*move) + dog.stand2[i],100)
			else:
				pass
			if switch == 1:
				for i in [2,6]:
					phi = math.pi
					move = 10
					sign = 1
					dog.servo_dir[i].moveTimeWrite(((sin(t + phi))*(sign*dog.front[i])*move) + dog.stand2[i],100)
					i+=1
					move = 5
					if sin(t)>=0:
						sign = 1
						dog.servo_dir[i].moveTimeWrite(((sin(2*t + phi))*(sign*dog.front[i])*move) + dog.stand2[i],100)
					elif sin(t)<0:
						switch = 1
						sign = -1
						dog.servo_dir[i].moveTimeWrite(((sin((2*t) + phi))*(sign*dog.front[i])*move) + dog.stand2[i],100)


		time.sleep((tim/1000))
		t += dt
	time.sleep((tim/1000))
	stand2(dog)

def tap_tap(dog, id=None, tim=None, stretch=None, dt=None, omega=None):
	if id:
		pass
	else:
		id=int(input("Enter Motor id:"))
		while id not in [2,4]:
			print("Only id 2 and 4 allowed in this motion")
			id=int(input("Enter Motor id:"))
		id = int(id)-1
	if tim:
		pass
	else:
		tim = 200
	if stretch:
		pass
	else:
		stretch = 30
	if dt:
		pass
	else:
		dt = 1
	move = 10
	t=0
	while t < stretch:
		dog.servo_dir[id].moveTimeWrite(((sin(t))*(dog.front[id])*move) + (dog.stand2[id]+(dog.front[id]*(move))),tim)
		time.sleep((tim/1000))
		t+=dt
		pass
	stand2(dog, tim=200)

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
				if pos >=0 :
					pos = dog.front[motor_id-1]*pos
				else:
					pos = -dog.front[motor_id-1]*pos
				pos = pos + dog.straight[motor_id - 1]
			except:
				nope(dog)
		tim = 1500
		dog.servo_dir[motor_id - 1].moveTimeWrite(pos, tim)
		print("The motor", motor_id, "is now at", pos)
	except:
		nope(dog)
	time.sleep((tim/1000)+rest_t)
	dog.current_pos="random"

#moves the robot by a given angle and direction
def move_by(dog, id_m=None, dir_m=None, pos_m=None, tim=None):
    if id_m:
        if dir_m == "front":
            sign = 1
        elif dir_m == "back":
            sign = -1
        if tim:
            pass
        else:
            tim = 1500
        pos = dog.servo_dir[id_m - 1].getPhysicalPos() + (dog.front[id_m - 1]*sign*pos_m)
        dog.servo_dir[id_m - 1].moveTimeWrite(pos, tim)
    else:
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
    dog.current_pos="random"

def move_multi(dog):
	enter_ids = str(input("Enter motor ids: ")).lower()
	string = "[" + enter_ids + "]"
	ids = eval(string)
	pos= []
	for i in ids:
		string = "Enter the position for" + str(i) +" : "
		enter_pos = int(input(string))
		enter_pos = dog.front[i-1]*enter_pos
		enter_pos += dog.straight[i-1]
		pos.append(enter_pos)
	for i in range(len(ids)):
		tim = 300
		dog.servo_dir[ids[i]-1].moveTimeWrite(pos[i], tim)
	time.sleep((tim/1000)+rest_t)
	dog.current_pos="random"

def move_multi_by(dog):
	enter_ids = str(input("Enter motor ids: ")).lower()
	string = "[" + enter_ids + "]"
	ids = eval(string)
	pos= []
	for i in ids:
		string = "Enter the position for" + str(i) +" : "
		enter_pos = int(input(string))
		enter_pos = dog.front[i-1]*enter_pos
		enter_pos += dog.servo_dir[i-1].getPhysicalPos()
		pos.append(enter_pos)
	for i in range(len(ids)):
		tim = 300
		dog.servo_dir[ids[i]-1].moveTimeWrite(pos[i], tim)
	time.sleep((tim/1000)+rest_t)
	dog.current_pos="random"

def scratch_me(dog, tim=None,stretch=None):
    if dog.current_pos == "scratch_me":
        return
    elif dog.current_pos != "stand2":
        stand2(dog)
    else:
        pass
    if stretch:
        pass
    else:
        stretch=20
    if tim:
        pass
    else:
        tim= 180
    move_by(dog, 3, "front", 120, tim=3000)
    time.sleep(3.1)
    t = 0
    dt = 0.8
    pos = dog.servo_dir[3].getPhysicalPos()
    move = 30
    while t<stretch:
        dog.servo_dir[3].moveTimeWrite(((sin(t))*dog.front[3]*move) + pos, tim)
        time.sleep(0.05)
        t += dt
    dog.current_pos = "scratch_me"
    stand2(dog)
    return

def scratch_me2(dog, tim=None,stretch=None):
    if dog.current_pos == "scratch_me":
        return
    elif dog.current_pos != "stand2":
        stand2(dog)
    else:
        pass
    if stretch:
        pass
    else:
        stretch=20
    if tim:
        pass
    else:
        tim= 180
    move_by(dog, 1, "front", 120, tim=3000)
    time.sleep(3.1)
    t = 0
    dt = 0.8
    pos = dog.servo_dir[1].getPhysicalPos()
    move = 30
    while t<stretch:
        dog.servo_dir[1].moveTimeWrite(((sin(t))*dog.front[1]*move) + pos, tim)
        time.sleep(0.05)
        t += dt
    dog.current_pos = "scratch_me"
    stand2(dog)
    return

def jackson(dog, tim=None, steps=None):
    step = 0
    if dog.current_pos != "straight":
        straight(dog)
    else:
        pass
    if tim:
        pass
    else:
        tim = 1500
    if steps:
        pass
    else:
        steps = 10
    while step <steps:
        if step % 2 == 0:
            for i in [0,2,4,6]:
                move_by(dog, i+1, "back", 22)
            for i in [1,3,5,7]:
                move_by(dog, i+1, "front", 49)
            time.sleep(1.5)
            step +=1
        else:
            for i in range(len(dog.servo_dir)):
                dog.servo_dir[i].moveTimeWrite(dog.straight[i],tim)
            time.sleep((tim/1000)+rest_t)
            step +=1
    stand2(dog)
    dog.current_pos = "stand2"

def hop_hop(dog,tim=None, steps=None):
	if tim:
		pass
	else:
		tim = 500
	if steps:
		pass
	else:
		steps=10
	step = 0
	while step <steps:
	    if step % 2 == 0:
	        stand2(dog, tim)
	        step += 1
	    else:
	        stand(dog, tim)
	        step +=1
	stand2(dog)
	dog.current_pos = "stand2"

def side_side(dog, tim=None, steps=None):
    if dog.current_pos != "stand":
        stand(dog)
    else:
        pass
    if steps:
        pass
    else:
        steps=30
    step = 0
    if tim:
        pass
    else:
        tim = 500
    while step <steps:
        if step % 2 == 0:
            for i in [0,1,6,7]:
                dog.servo_dir[i].moveTimeWrite(dog.stand2[i],tim)
            for i in  [2,3,4,5]:
                dog.servo_dir[i].moveTimeWrite(dog.stand[i],tim)
        else:
            for i in [0,1,6,7]:
                dog.servo_dir[i].moveTimeWrite(dog.stand[i],tim)
            for i in  [2,3,4,5]:
                dog.servo_dir[i].moveTimeWrite(dog.stand2[i],tim)
        step += 1
        time.sleep((tim/1000))
    stand2(dog)
    dog.current_pos = "stand"

def hey_dog(dog,sound=None):
    if dog.current_pos == "hey_dog":
        return
    elif dog.current_pos != "stand2":
        stand2(dog)
    else:
        pass
    if sound:
        pass
    else:
        wave_obj = sa.WaveObject.from_wave_file("hey_dog.wav")
        play_obj = wave_obj.play()
    move_by(dog, 3, "front", 80)
    move_by(dog, 4, "back", 35)
    time.sleep(3)
    move_by(dog, 4, "front", 35)
    move_by(dog, 3, "back", 80)
    return

def twerk(dog, tim=None, steps=None):
	stand(dog)
	step = 0
	up = 0
	if tim:
		pass
	else:
		tim = 200
	if steps:
		pass
	else:
		steps=10
	while step < steps:
		if up == 0:
			for i in [0,1,2,3]:
				dog.servo_dir[i].moveTimeWrite(dog.stand[i],tim)
			for i in [4,5,6,7]:
				dog.servo_dir[i].moveTimeWrite(dog.stand2[i],tim)
			up = 1
		else:
			for i in [0,1,2,3]:
				dog.servo_dir[i].moveTimeWrite(dog.stand[i],tim)
			for i in [4,5,6,7]:
				dog.servo_dir[i].moveTimeWrite(dog.stand[i],tim)
			up = 0
		time.sleep((tim/1000)+rest_t)
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

#input the time to wait in sec
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

def end_credits():
	print(Fore.BLUE + "Made By:"Style.RESET_ALL)
	wait(3)
	print(Fore.BLUE + "Pragyendra Bagediya"+ Style.RESET_ALL)
	wait(3)
	print(Fore.BLUE + "Prince Bharma"+ Style.RESET_ALL)
	wait(3)
	print(Fore.BLUE + "")
	print(Fore.BLUE + "Special credits to:"+ Style.RESET_ALL)
	wait(3)
	print(Fore.BLUE + "Prof. Hod Lipson"+ Style.RESET_ALL)
	wait(3)
	print(Fore.BLUE + "TA Xincheng Zhao:"+ Style.RESET_ALL)
	wait(3)
	print("")
	print(Fore.BLUE + "P.S. The 3D Printers in Makerspace are always Busy"+ Style.RESET_ALL)
	wait(6)
	print(Fore.Green + "See Ya, Bye"+ Style.RESET_ALL)
	print(Fore.BLUE + "- - - - - - - - - - - - - - - - - -"+ Style.RESET_ALL)
