import RPi.GPIO as GPIO
import time

class SBD10:
    def __init__(self, en_pin, dir_pin, stp_pin):
        self.en_pin = en_pin
        self.dir_pin = dir_pin
        self.stp_pin = stp_pin
        self.pulse_cnt = 0

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.en_pin, GPIO.OUT)
        GPIO.setup(self.dir_pin, GPIO.OUT)
        GPIO.setup(self.stp_pin, GPIO.OUT)
        GPIO.output(self.en_pin, GPIO.LOW)
        GPIO.output(self.dir_pin, GPIO.LOW)

    def enable(self, value):
        GPIO.output(self.en_pin, value)

    def direction(self, value):
        GPIO.output(self.dir_pin, value)

    def continuous_pulse(self, pulse_us):
        if pulse_us == 0:
            GPIO.output(self.stp_pin, GPIO.LOW)
            return

        if pulse_us > 0x3FFF:
            pulse_us = 0x3FFF
 
        pulse_period = pulse_us * 2  # Convert to period

        # 직접 count_pulse 콜백 함수 호출
        self.count_pulse(None)

        GPIO.output(self.stp_pin, GPIO.HIGH)
        time.sleep(pulse_period / 1000000.0)
        GPIO.output(self.stp_pin, GPIO.LOW)
        time.sleep(pulse_period / 1000000.0)

    def burst_pulse(self, pulse_us, cnt=0):
        if pulse_us == 0:
            return

        if pulse_us > 0x3FFF:
            pulse_us = 0x3FFF

        self.pulse_cnt = 0
        GPIO.add_event_detect(self.stp_pin, GPIO.RISING, callback=self.count_pulse)
        for _ in range(cnt + 1):
            self.continuous_pulse(pulse_us)

        GPIO.remove_event_detect(self.stp_pin)

    def count_pulse(self, channel):
        self.pulse_cnt += 1

if __name__ == "__main__":
    sbd10 = SBD10(en_pin=15, dir_pin=11, stp_pin=13)

    sbd10.enable(GPIO.LOW)  # Enable motor
    sbd10.direction(GPIO.LOW)  # Set motor direction

    # Continuous pulse for 10 seconds
    start_time = time.time()
    while time.time() - start_time < 10:
        sbd10.continuous_pulse(1000)  # Adjust pulse duration as needed
        print(f"Pulse count: {sbd10.pulse_cnt}")

    sbd10.enable(GPIO.HIGH)  # Disable motor

    GPIO.cleanup()  # Cleanup GPIO settings
