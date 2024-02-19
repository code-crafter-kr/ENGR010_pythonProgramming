from gpiozero import CamJamKitRobot
import time

robot = CamJamKitRobot()

def moves(speeds, duration, direction):
    speeds = speeds / 100
    if direction == "forward":
        robot.forward(speeds)
    
    elif direction == "backward":
        robot.backward(speeds)
    
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


moves(100, 4, "backward")
