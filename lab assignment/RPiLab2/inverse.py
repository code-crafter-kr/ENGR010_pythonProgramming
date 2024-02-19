from gpiozero import PWMLED
from gpiozero import LED

import time

led1 = PWMLED(11)
led2 = PWMLED(9)
led3 = PWMLED(10)
runtime = 0
value1 = 0
value2 = 0
value3 = 0

while True:

	if runtime > 30:
		break

	if 0 <= runtime <= 7.5:
		value1 = runtime / 7.5

	elif 7.5 < runtime <= 15:
		value1 = 1 - ((runtime - 7.5) / 7.5)
		value2 = ((runtime - 7.5) / 7.5)

	elif 15 < runtime <= 22.5:
		value2 = 1 - ((runtime - 15) / 7.5)
		value3 = ((runtime - 15) / 7.5)

	elif 22.5 < runtime <= 30:
		value3 = 1 - ((runtime - 22.5) / 7.5)


	if value1 < 0:
		value1 = 0
	if value2 < 0:
		value2 = 0
	if value3 < 0:
		value3 = 0

	led1.value = value1
	led2.value = value2
	led3.value = value3

	runtime += 0.1
	time.sleep(0.1)
	
