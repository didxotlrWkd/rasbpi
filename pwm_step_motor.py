import RPi.GPIO as GPIO
import time

STP = 33
DIR = 12
EN = 22

GPIO.setmode(GPIO.BOARD)

GPIO.setup(DIR, GPIO.OUT)
GPIO.setup(EN, GPIO.OUT)
GPIO.setup(STP , GPIO.OUT)

pwm = GPIO.PWM(STP , 1000)

pwm.start(0)

try: 
	while True:
		GPIO.output(DIR, GPIO.LOW)
		for i in range(1000):
			pwm.ChangeDutyCycle(1000)
			time.sleep(0.1)

		GPIO.output(DIR, GPIO.HIGH)
		for i in range(1000):
			pwm.ChangeDutyCycle(1000)
			time.sleep(0.1)
except:
	pwm.stop()
	GPIO.cleanup()
