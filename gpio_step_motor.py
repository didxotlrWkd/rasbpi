import RPi.GPIO as GPIO
import time 

DIR = 12
STP = 16
ENA = 22

GPIO.setmode(GPIO.BOARD)

GPIO.setup(DIR, GPIO.OUT)
GPIO.setup(STP, GPIO.OUT)
GPIO.setup(ENA, GPIO.OUT)

print("GPIO setup")

duration = 1000

GPIO.output(ENA, GPIO.LOW)
print("EN HIGH")
time.sleep(2)

GPIO.output(ENA, GPIO.HIGH)
time.sleep(1)
print("start")

def move_motor(steps, direction, delay=0.0005):
	GPIO.output(DIR, direction)
	
	for _ in range(steps):
		GPIO.output(STP, GPIO.HIGH)
		time.sleep(delay)
		GPIO.output(STP, GPIO.LOW)
		time.sleep(delay)

try:
	move_motor(2000,True)
	time.sleep(1)
	move_motor(2000, False)

except KeyboardInterrupt:
	print("cleanup")
	GPIO.cleanup()

finally:
	GPIO.cleanup()


