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
import simpleaudio as sa



global rest_t
rest_t = 0.2

def dance(dog):
    if dog.current_pos != "stand":
        stand(dog)
        stand2(dog)
    else:
        pass
    print(Fore.RED +"I <3 QUEEN"+ Style.RESET_ALL)
    wave_obj = sa.WaveObject.from_wave_file("another.wav")
    play_obj = wave_obj.play()
    rest_me = 1.8
    def me_tap(dog,steps=None):
        if steps:
            pass
        else:
            steps = 3
        step = 1
        while step < steps:
            tap_tap(dog, id=1, tim=150, stretch=17, dt=1.3)
            wait(rest_me)
            tap_tap(dog, id=3, tim=150, stretch=17, dt=1.3)
            wait(rest_me)
            step +=1
    me_tap(dog)
    wait(2*rest_me)
    side_side(dog)
    me_tap(dog)
    right_round(dog)
    right_round2(dog)
    side_side(dog)
    scratch_me(dog,stretch=40)
    twerk(dog)
    jackson(dog)
    hop_hop(dog, tim=300)
    walk(dog)
    right_round(dog)
    scratch_me(dog,stretch=40)
    time.sleep(0.5)
    scratch_me2(dog,stretch=40)
    jackson(dog)
    hey_dog(dog,sound=1)
    wait(1)
    me_tap(dog)
    wait(2*rest_me)
    me_tap(dog,1)
    straight(dog)


def dance2(dog):
    scratch_me(dog,stretch=40)
    time.sleep(0.5)
    scratch_me2(dog,stretch=40)
