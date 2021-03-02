import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
blue = 11
red = 12
green = 13
button = 10
GPIO.setup(blue, GPIO.OUT) #Blue LED
GPIO.setup(red, GPIO.OUT) #Red LED
GPIO.setup(green, GPIO.OUT) #Green LED
GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_UP) #button PD

colors = [0xFF0000, 0x0F0F00, 0x00FF00]
pwm_red = GPIO.PWM(red, 5000) #PWM mit Frequenz 2kHz erstellen
pwm_blue = GPIO.PWM(blue, 5000)
pwm_green = GPIO.PWM(green, 5000)

pwm_red.start(0) # TV auf 0 setzen
pwm_blue.start(0)
pwm_green.start(0)

pwm_blue.ChangeDutyCycle(0)

def setColor(color):
    red_value=(color & 0x110000) >> 16
    green_value = (color & 0x001100) >> 8
    blue_value = (color & 0x000011) >> 0
    
    red_value = red_value*100/255
    green_value = green_value*100/255
    blue_value = blue_value*100/255
    
    pwm_red.ChangeDutyCycle(red_value)
    pwm_green.ChangeDutyCycle(green_value)
    pwm_blue.ChangeDutyCycle(blue_value)

i = 0
while True:
    if GPIO.input(button) == GPIO.LOW: # push-buton pressed
        setColor(colors[i]) #set color 
        i+=1 # increment i by 1
        if(i>=3): #reset i to 0
            i=0
        time.sleep(0.1) # no keybounce
    
