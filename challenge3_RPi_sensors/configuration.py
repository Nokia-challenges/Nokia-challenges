import RPi.GPIO as GPIO

class Configuration:
    def __init__(self):
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)

        # pinout for raspberry pi 3b+
        self.GPIO_ECHO = 27
        self.GPIO_TRIG = 4
        self.GPIO_RED = 23
        self.GPIO_GREEN = 24
        self.GPIO_BLUE = 22
        self.GPIO_PIR = 25
        self.GPIO_BUZZER = 26
        
        # pin configurations
        GPIO.setup(self.GPIO_ECHO, GPIO.IN)
        GPIO.setup(self.GPIO_TRIG, GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(self.GPIO_RED, GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(self.GPIO_GREEN, GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(self.GPIO_BLUE, GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(self.GPIO_PIR, GPIO.IN)
        GPIO.setup(self.GPIO_BUZZER, GPIO.OUT, initial=GPIO.LOW)