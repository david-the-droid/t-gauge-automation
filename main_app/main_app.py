# empty python file

from gpiozero import PWMOutputDevice
from time import sleep

# pwm controller

# GPIO 27 (13): AIN2
# GPIO 22 (15): AIN1

# GPIO18, f=40Hz
pwm1 = PWMOutputDevice(pin=27, frequency=140)
pwm2 = PWMOutputDevice(pin=22, frequency=140)

# duty cycle 50%
try: 
	pwm1.value = 0
	pwm2.value = 0.5
except keyBoardInterrupt:
	pwm.off()
	print("PWM stopped")
	

while True:
	sleep(1)
