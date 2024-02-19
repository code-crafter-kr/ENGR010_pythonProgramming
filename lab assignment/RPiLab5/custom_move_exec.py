#ENGR 010
#Lab 5
#Sehyoun Jang
#sej324

from time import sleep
import time
from gpiozero import CamJamKitRobot

robot = CamJamKitRobot()

def move_Forward(lps,rps,dur):
	motorforward = (lps,rps)
	robot.value = motorforward
	time.sleep(dur)

def move_Backward(lps,rps,dur):
	motorbackward = (-lps,-rps)
	robot.value = motorbackward
	time.sleep(dur)

def r_turn(lps,rps,dur):
	rturn = (lps,0)
	robot.value =rturn
	time.sleep(dur)
        
def l_turn(lps,rps,dur):
	lturn = (0,rps)
	robot.value = lturn
	time.sleep(dur)

def r_rotate(lps,rps,dur):
	rrotate = (lps,-rps)
	robot.value = rrotate
	time.sleep(dur)

def l_rotate(lps,rps,dur):
	lrotate = (-lps,rps)
	robot.value = lrotate
	time.sleep(dur)


def stop(lps,rps,dur):
	stop = (lps,rps)
	robot.value = stop
	sleep(dur)

reading = open('move_commands.txt','r')

for line in reading:
	line = line.rstrip()
	order  = line.split(',')

	if order[0] == 'forward':
		move_Forward(float(order[1]),float(order[2]),float(order[3]))
	elif order[0] == 'backward':
		 move_Backward(float(order[1]),float(order[2]),float(order[3]))
	elif order[0] == 'lrotate':
		l_rotate(float(order[1]),float(order[2]),float(order[3]))
	elif order[0] == 'rrotate':
		r_rotate(float(order[1]),float(order[2]),float(order[3]))
	elif order[0] == 'stop':
		stop(float(order[1]),float(order[2]),float(order[3]))
