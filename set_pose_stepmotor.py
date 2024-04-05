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

current_position = 0

def move_motor(steps, direction, delay=0.0005):
	GPIO.output(DIR, direction)
	
	for _ in range(steps):
		GPIO.output(STP, GPIO.HIGH)
		time.sleep(delay)
		GPIO.output(STP, GPIO.LOW)
		time.sleep(delay)

def set_pose(target_position):
	global current_position

	steps = target_position - current_position
	direction = GPIO.HIGH if steps > 0 else GPIO.LOW
	steps = abs(steps)
	print("moving step : ", steps)
	GPIO.output(DIR, direction)

	for _ in range(steps):
		GPIO.output(STP, GPIO.HIGH)
		time.sleep(0.0005)
		GPIO.output(STP, GPIO.LOW)
		time.sleep(0.0005)

	current_position = target_position

try:
	current_position = 0

	target_positions = [2000, -2000 , 4000 ,-3500]

	for pos in target_positions:
		set_pose(pos)
		time.sleep(1)

except KeyboardInterrupt:
	print("cleanup")
	GPIO.cleanup()

finally:
	GPIO.cleanup()


