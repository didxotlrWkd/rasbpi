import RPi.GPIO as GPIO
import time

EN = 22

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

GPIO.setup(EN, GPIO.OUT)

GPIO.output(EN , GPIO.LOW)
