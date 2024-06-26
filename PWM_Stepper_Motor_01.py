# Based on: https://www.raspberrypi.org/forums/viewtopic.php?t=242928\.
#
# Software to drive 4 wire stepper motor using a TB6600 Driver
# PRi - RPi 3B
#
# Route 3.3 VDC to the controller "+" input for each: ENA, PUL, and DIR
#
# Connect GPIO pins as shown below) to the "-" input for each: ENA, PUL, and DIR
#
#
from time import sleep
import RPi.GPIO as GPIO
#
PUL = 1  # Stepper Drive Pulses
DIR = 15  # Controller Direction Bit (High for Controller default / LOW to Force a Direction Change).
ENA = 14  # Controller Enable Bit (High to Enable / LOW to Disable).
# DIRI = 14  # Status Indicator LED - Direction
# ENAI = 15  # Status indicator LED - Controller Enable
#
# NOTE: Leave DIR and ENA disconnected, and the controller WILL drive the motor in Default direction if PUL is applied.
# 
GPIO.setmode(GPIO.BCM)
# GPIO.setmode(GPIO.BOARD) # Do NOT use GPIO.BOARD mode. Here for comparison only. 
#
GPIO.setup(PUL, GPIO.OUT)
GPIO.setup(DIR, GPIO.OUT)
GPIO.setup(ENA, GPIO.OUT)
# GPIO.setup(DIRI, GPIO.OUT)
# GPIO.setup(ENAI, GPIO.OUT)0
#
print('PUL = GPIO 17 - RPi 3B-Pin #11')
print('DIR = GPIO 27 - RPi 3B-Pin #13')
print('ENA = GPIO 22 - RPi 3B-Pin #15')

print('Initialization Completed')

durationFwd = 5000 # This is the duration of the motor spinning. used for forward direction
durationBwd = 5000 # This is the duration of the motor spinning. used for reverse direction
print('Duration Fwd set to ' + str(durationFwd))
print('Duration Bwd set to ' + str(durationBwd))
#
delay = 0.05 # This is actualy a delay between PUL pulses - effectively sets the mtor rotation speed.
print('Speed set to ' + str(delay))
#
cycles = 1000 # This is the number of cycles to be run once program is started.
cyclecount = 0 # This is the iteration of cycles to be run once program is started.
print('number of Cycles to Run set to ' + str(cycles))

GPIO.output(ENA, GPIO.LOW)
   
print('ENA set to HIGH - Controller Enabled')

sleep(.5) # pause due to a possible change direction
GPIO.output(DIR, GPIO.LOW)
  
  
def forward():  
    print('DIR set to LOW - Moving Forward at ' + str(delay))
    print('Controller PUL being driven.')
    for x in range(durationFwd): 
        GPIO.output(PUL, GPIO.HIGH)
        sleep(delay)
        GPIO.output(PUL, GPIO.LOW)
        sleep(delay)

    print('ENA set to LOW - Controller Disabled')
    sleep(.5) # pause for possible change direction
    return
#
#
def reverse():
    GPIO.output(ENA, GPIO.HIGH)

    print('ENA set to HIGH - Controller Enabled')
    #
    sleep(.5) # pause due to a possible change direction
    GPIO.output(DIR, GPIO.HIGH)

    print('DIR set to HIGH - Moving Backward at ' + str(delay))
    print('Controller PUL being driven.')
    #
    for y in range(durationBwd):
        GPIO.output(PUL, GPIO.HIGH)
        sleep(delay)
        GPIO.output(PUL, GPIO.LOW)
        sleep(delay)
    GPIO.output(ENA, GPIO.LOW)
 
    print('ENA set to LOW - Controller Disabled')
    sleep(.5) # pause for possible change direction
    return


try: 
    while True:
        dir = int(input("check dir: "))
        if dir == 1:
            forward()
        elif dir == 2:
            reverse()
        else :
            GPIO.cleanup()
            break
except KeyboardInterrupt:
	print("cleanup")
	GPIO.cleanup()
