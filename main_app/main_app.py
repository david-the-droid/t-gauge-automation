"""Basic PWM demo"""

from time import sleep
from gpiozero import PWMOutputDevice

pwm1 = PWMOutputDevice(27, frequency=137)  # GPIO 27
pwm2 = PWMOutputDevice(22, frequency=137)  # GPIO 22

try:
    pwm1.value = 0
    pwm2.value = 0.3

    while True:
        sleep(1)

except KeyboardInterrupt:
    print("\nProgram interrupted by user. Stopping train...")
    pwm1.off()
    pwm2.off()
