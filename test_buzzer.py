import RPi.GPIO as GPIO
import time
buzzer = 8
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(buzzer, GPIO.OUT) #buzzer

pwm_buzzer = GPIO.PWM(buzzer, 100)
pwm_buzzer.start(0)
while True:
    pwm_buzzer.ChangeDutyCycle(100)
    

