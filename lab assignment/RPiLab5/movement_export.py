#ENGR 010
#Lab 5
#Sehyoun Jang
#sej324


from gpiozero import CamJamKitRobot, DistanceSensor
from time import sleep

sensor = DistanceSensor(echo = 18, trigger = 17, max_distance = 1)
robot = CamJamKitRobot()

with open('distance_data.txt','w') as mf:
	with open('movement_data.txt','w') as mf1:

		def moveForward(lps,rps,dur):
			motorforward = (lps,rps)
			robot.value = motorforward
			mf1.write(f'moveForward,{lps},{rps},{dur}')
			for i in range(dur*10):
				dis = sensor.distance*100
				mf.write(f'{dis},')
				sleep(0.1)

		def moveBackward(lps,rps,dur):
			motorforward = (lps,rps)
			robot.value = motorforward
			mf1.write(f'moveBackward,{lps},{rps},{dur}')
			for i in range(dur*10):
				dis = sensor.distance*100
				mf.write(f'{dis},')
				sleep(0.1)

		def turnleft(lps,rps,dur):
			motorforward = (lps,0)
			robot.value = motorforward
			mf1.write(f'turnleft,{lps},{rps},{dur}')
			for i in range(dur*10):
				dis = sensor.distance*100
				mf.write(f'{dis},')
				sleep(0.1)


		def turnright(lps,rps,dur):
			motorforward = (0,rps)
			robot.value = motorforward
			mf1.write(f'turnright,{lps},{rps},{dur}')
			for i in range(dur*10):
				dis = sensor.distance*100
				mf.write(f'{dis},')
				sleep(0.1)


	
		moveForward(0.25,0.25,2)
		sleep(0.2)
		turnleft(-0.25,0.25,2)
		sleep(0.2)
		moveForward(0.5,0.5,2)
		sleep(0.2)
		turnright(0,-0.25,2)
		sleep(0.2)
		moveForward(0.25,0.25,2)
		sleep(0.2)
		turnright(0.25,-0.25,2)
		sleep(0.2)
		moveBackward(-0.5,-0.5,2)
		sleep(0.2)


