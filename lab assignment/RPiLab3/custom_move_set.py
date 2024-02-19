from gpiozero import CamJamKitRobot
import time

robot = CamJamKitRobot()

def moves(speeds, duration, direction):
	speeds = speeds / 100
	if direction == "forward":
		robot.value=(speeds,speeds)
		#robot.forward(speed = speedt)
    
	elif direction == "backward":
		robot.backward(speed = speeds)
    
	elif direction == "stop":
		robot.stop()
	time.sleep(duration)
	robot.stop()
    
def turns(speeds, duration, direction):
    speeds = speeds / 100
    if direction == "left":
        robot.left(speed=speeds)
    elif direction == "right":
        robot.right(speed=speeds)
    time.sleep(duration)
    robot.stop()

def rotates(speeds, duration, direction):
    speeds = speeds / 100
    if direction == "CW":
        robot.left(speed=speeds)
        robot.right(speed=speeds / 5 * 3)
    elif direction == "CCW":
        robot.left(speed=speeds / 5 * 3)
        robot.right(speed=speeds)
    time.sleep(duration)
    robot.stop()

moves(50, 2, "forward")
turns(100, 0.5, "left")
moves(75, 2, "forward")
rotates(100, 1.5, "CW")
moves(50, 2, "forward")
turns(100, 0.5, "right")
moves(75, 2, "backward")
