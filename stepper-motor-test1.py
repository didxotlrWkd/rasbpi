import RPi.GPIO as GPIO
from time import sleep

EN = 9
# Direction pin from controller
DIR = 11
# Step pin from controller
STEP = 13
# 0/1 used to signify clockwise or counterclockwise.
CW = 1
CCW = 0


# Setup pin layout on PI
GPIO.setmode(GPIO.BOARD)

# Establish Pins in software
GPIO.setup(EN, GPIO.OUT)
GPIO.setup(DIR, GPIO.OUT)
GPIO.setup(STEP, GPIO.OUT)

# Set the first direction you want it to spin
GPIO.output(EN, GPIO.LOW)
GPIO.output(DIR, GPIO.LOW)

try:
    # Run forever.
    while True:
        # Run for 200 steps. This will change based on how you set your controller
        for x in range(200):
            # Set one coil winding to high
            GPIO.output(STEP, GPIO.HIGH)
           

# Once finished clean everything up
except KeyboardInterrupt:
    print("cleanup")
    GPIO.cleanup()
