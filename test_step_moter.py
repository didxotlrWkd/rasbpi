import wiringpi
import time

STP_PIN = 4
DIR_PIN = 1
EN_PIN = 6

wiringpi.wiringPiSetup()
wiringpi.pinMode(STP_PIN, wiringpi.OUTPUT)
wiringpi.pinMode(DIR_PIN, wiringpi.OUTPUT)
wiringpi.pinMode(EN_PIN, wiringpi.OUTPUT)

wiringpi.digitalWrite(EN_PIN, wiringpi.LOW)
time.sleep(3)
print("start")
wiringpi.digitalWrite(EN_PIN, wiringpi.HIGH)
step_delay = 0.0000005 

try:
    for _ in range(3):
       wiringpi.digitalWrite(DIR_PIN, wiringpi.LOW)
       for _ in range(25000):   
           wiringpi.digitalWrite(STP_PIN, wiringpi.HIGH)
           time.sleep(step_delay)
           wiringpi.digitalWrite(STP_PIN, wiringpi.LOW)
           time.sleep(step_delay)
        
       print("hi")
       time.sleep(1)
       wiringpi.digitalWrite(DIR_PIN, wiringpi.HIGH)
       time.sleep(1)
       print("dir change")
       for _ in range(25000):
            wiringpi.digitalWrite(STP_PIN, wiringpi.HIGH)
            time.sleep(step_delay)
            wiringpi.digitalWrite(STP_PIN, wiringpi.LOW)
            time.sleep(step_delay)

       time.sleep(1)

except KeyboardInterrupt:
    pass


finally:
    wiringpi.digitalWrite(EN_PIN, wiringpi.LOW)
    wiringpi.digitalWrite(STP_PIN, wiringpi.INPUT)
    wiringpi.digitalWrite(DIR_PIN, wiringpi.INPUT)
    wiringpi.digitalWrite(EN_PIN, wiringpi.INPUT)


