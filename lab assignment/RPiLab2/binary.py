from gpiozero import LED
import time

led1 = LED(11)
led2 = LED(9)
led3 = LED(10)

while True:
	for i in range (8):
		binary = '{0:b}'.format(i).zfill(3)
		led1.value = int(binary[2])
		led2.value = int(binary[1])
		led3.value = int(binary[0])
		time.sleep(1)
