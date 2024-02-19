#Sehyoun Jang
#ENGR 010
#Lab2

from gpiozero import LED
from time import sleep

led1 = LED(10)
led2 = LED(11)
led3 = LED(9)


led1.on()
sleep(1)
led1.off()
led2.on()
sleep(1)
led3.on()
led2.off()
sleep(1)
led3.off()
led1.on()

