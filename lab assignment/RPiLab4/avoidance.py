#ENGR 010
#Lab 4
#Sehyoun Jang
#04/07/2023
import time
from gpiozero import CamJamKitRobot
from gpiozero import LED, DistanceSensor
from time import sleep

led = LED(1)
sensor = DistanceSensor(echo = 17, trigger = 18, max_distance = 1)

sensor.when_in_range = led.on
sensor.when_out_of_range = led.off



robot = CamJamKitRobot()

def move_forward(lps,rps,duration):
	motor_forward = (lps,rps)
	robot.value = motor_forward
	time.sleep(duration)

def move_backward(lps,rps,duration):
	motor_backward = (-lps,-rps)
	robot.value = motor_backward
	time.sleep(duration)

def right_turn(lps,rps,duration):
	rturn = (lps,0)
	robot.value =rturn
	time.sleep(duration)
        
def left_turn(lps,rps,duration):
	lturn = (0,rps)
	robot.value = lturn
	time.sleep(duration)

def right_rotate(lps,rps,duration):
	right_rotate = (lps,-rps)
	robot.value = right_rotate
	time.sleep(duration)

def left_rotate(lps,rps,duration):
	left_rotate = (-lps,rps)
	robot.value = left_rotate
	time.sleep(duration)

def operation():
	print('Moves backward at full speed for 1 seconds')
	move_backward(1,1,1)
	print('Rotates CCW 90°')
	left_turn(0.5,0.5,0.8)
	print('Moves forward at half of full speed for 1 seconds')
	move_forward(0.5,0.5,1)
	print('Rotates CW 90°')
	right_turn(0.5,0.5,0.8)
	print('Moves forward at half of full speed for 1 seconds')
	move_forward(0.5,0.5,1)
	print('Rotates CW 90°')
	right_turn(0.5,0.5,0.8)
	print('Moves forward at half of full speed for 1 seconds')
	move_forward(0.5,0.5,1)
	print('Rotates CCW 90°')
	left_turn(0.5,0.5,0.8)

def sw(distance):
	robot_distance = sensor.distance*100
	if distance >= robot_distance:
		return True
	else:
		return False

while True:
	distance = sensor.distance * 100
	print("Distance:", distance)
	sleep(0.5)
	if sw(10):
		operation()
	
	
