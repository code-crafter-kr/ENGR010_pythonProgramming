#ENGR 010
#Lab 4
#Sehyoun Jang
#04/07/2023

from gpiozero import LED, DistanceSensor
from time import sleep

led = LED(1)
sensor = DistanceSensor(echo = 17, trigger = 18, max_distance = 1)

sensor.when_in_range = led.on
sensor.when_out_of_range = led.off

while True:
	if ((sensor.distance*100) >= 10) and  ((sensor.distance*100) <= 20):
		print("Distance:%s"%(sensor.distance*100))
	sleep(0.5)
