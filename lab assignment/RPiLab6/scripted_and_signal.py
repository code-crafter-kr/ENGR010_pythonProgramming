
from time import sleep
import time
from gpiozero import CamJamKitRobot
from gpiozero import LED

Led1 = LED(22)
Led2 = LED(23)
robot = CamJamKitRobot()

def moveForward(lps,rps,dur):
	motorforward = (lps,rps)
	robot.value = motorforward
	Led1.off()
	Led2.off()
	time.sleep(dur)

def moveBackward(lps,rps,dur):
	motorbackward = (-lps,-rps)
	robot.value = motorbackward
	Led1.off()
	Led2.off()
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
	Led1.off()
	Led2.on()
	time.sleep(dur)

def lrotate(lps,rps,dur):
	lrotate = (-lps,rps)
	robot.value = lrotate
	Led1.on()
	Led2.off()
	time.sleep(dur)


def stop(lps,rps,dur):
	stop = (lps,rps)
	robot.value = stop
	Led1.off()
	Led2.off()
	sleep(dur)

mf = open('scripted_commands.txt','r')
for line in mf:
	line = line.rstrip()
	lane  = line.split(',')

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
