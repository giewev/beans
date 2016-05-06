import RPi.GPIO as GPIO
import time

class Controller(object):
    def __init__(self):
        self.led = 15
        self.claw_open = 36
        self.claw_close = 38
        self.wrist_up = 33
        self.wrist_down = 40
        self.elbow_up = 11
        self.elbow_down = 13
        self.shoulder_down = 19
        self.shoulder_up = 21
        self.shoulder_left = 37
        self.shoulder_right = 35
        
        self.setup()

    def run_pin(self, number, duration):
        GPIO.output(number, True)
        time.sleep(duration)
        GPIO.output(number, False)

    def enable_pin(self, number):
        GPIO.output(number, True)

    def disable_pin(self, number):
        GPIO.output(number, False)

    def demo_all(self):
        self.run_pin(self.led, 1)
        self.run_pin(self.wrist_up, 1)
        self.run_pin(self.wrist_down, 1)
        self.run_pin(self.elbow_up, 1)
        self.run_pin(self.elbow_down, 1)
        self.run_pin(self.shoulder_up, 1)
        self.run_pin(self.shoulder_down, 1)
        self.run_pin(self.shoulder_left, 1)
        self.run_pin(self.shoulder_right, 1)
        self.run_pin(self.claw_open, 1)
        self.run_pin(self.claw_close, 1)

    def setup(self):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.led, GPIO.OUT)
        GPIO.setup(self.claw_open, GPIO.OUT)
        GPIO.setup(self.claw_close, GPIO.OUT)
        GPIO.setup(self.wrist_up, GPIO.OUT)
        GPIO.setup(self.wrist_down, GPIO.OUT)
        GPIO.setup(self.elbow_up, GPIO.OUT)
        GPIO.setup(self.elbow_down, GPIO.OUT)
        GPIO.setup(self.shoulder_up, GPIO.OUT)
        GPIO.setup(self.shoulder_down, GPIO.OUT)
        GPIO.setup(self.shoulder_left, GPIO.OUT)
        GPIO.setup(self.shoulder_right, GPIO.OUT)

        GPIO.output(self.led, False)
        GPIO.output(self.claw_open, False)
        GPIO.output(self.claw_close, False)
        GPIO.output(self.wrist_up, False)
        GPIO.output(self.wrist_down, False)
        GPIO.output(self.elbow_up, False)
        GPIO.output(self.elbow_down, False)
        GPIO.output(self.shoulder_up, False)
        GPIO.output(self.shoulder_down, False)
        GPIO.output(self.shoulder_left, False)
        GPIO.output(self.shoulder_right, False)

    def cleanup(self):
        GPIO.cleanup()
        
