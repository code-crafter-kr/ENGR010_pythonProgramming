#ENGR010
#Lab 6
#Sehyoun Jang
#sej324



from time import sleep
import time
from gpiozero import CamJamKitRobot
from gpiozero import DistanceSensor

sensor = DistanceSensor(echo = 18, trigger = 17, max_distance = 1)
robot = CamJamKitRobot()

def moveForward(lps,rps,dur):
        motorforward = (lps,rps)
        robot.value = motorforward
        time.sleep(dur)
def moveBackward(lps,rps,dur):
	motorbackward = (-lps,-rps)
	robot.value = motorbackward
	time.sleep(dur)

def rturn(lps,rps,dur):
	rturn = (lps,0)
	robot.value =rturn
	time.sleep(dur)
        
def lturn(lps,rps,dur):
	lturn = (0,rps)
	robot.value = lturn
	time.sleep(dur)

def rrotate(lps,rps,dur):
	rrotate = (lps,-rps)
	robot.value = rrotate
	time.sleep(dur)

def lrotate(lps,rps,dur):
	lrotate = (-lps,rps)
	robot.value = lrotate
	time.sleep(dur)


def stop(lps,rps,dur):
	stop = (lps,rps)
	robot.value = stop
	sleep(dur)

mf = open('scripted_commands.txt','r')
for line in mf:
	line = line.rstrip()
	lane  = line.split(',')
	robotdistance = sensor.distance*100
	if robotdistance>10:
		if lane[0] == 'forward':
			moveForward(float(lane[1]),float(lane[2]),float(lane[3]))
		elif lane[0] == 'backward':
			 moveBackward(float(lane[1]),float(lane[2]),float(lane[3]))
		elif lane[0] == 'lrotate':
			lrotate(float(lane[1]),float(lane[2]),float(lane[3]))
		elif lane[0] == 'rrotate':
			rrotate(float(lane[1]),float(lane[2]),float(lane[3]))
		elif lane[0] == 'stop':
			stop(float(lane[1]),float(lane[2]),float(lane[3]))
	
	if robotdistance <= 10:
		moveBackward(1,1,1)
		lrotate(0.5,0.5,0.5)
		moveForward(0.5,0.5,1)
		rrotate(0.5,0.5,0.5)
		moveForward(0.5,0.5,1)
		rrotate(0.5,0.5,0.5)
		moveForward(1,1,1)
		lrotate(0.5,0.5,0.5)
