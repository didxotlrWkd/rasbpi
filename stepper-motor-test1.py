import RPi.GPIO as GPIO
from time import sleep

EN = 22
# Direction pin from controller
DIR = 27
# Step pin from controller
STEP = 17
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
GPIO.output(EN, GPIO.HIGH)
GPIO.output(DIR, GPIO.HIGH)

try:
    # Run forever.
    while True:
        print("start")
        """Change Direction: Changing direction requires time to switch. The
        time is dictated by the stepper motor and controller. """
        # Run for 200 steps. This will change based on how you set your controller
        for x in range(200):
            # Set one coil winding to high
            GPIO.output(STEP, GPIO.HIGH)
            # Allow it to get there.
            sleep(0.005)  # Dictates how fast stepper motor will run
            # Set coil winding to low
            GPIO.output(STEP, GPIO.LOW)
            sleep(0.005)  # Dictates how fast stepper motor will run
        print("restart")

# Once finished clean everything up
except KeyboardInterrupt:
    print("cleanup")
    GPIO.cleanup()
