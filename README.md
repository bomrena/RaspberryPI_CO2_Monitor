# RaspberryPI_CO2_Monitor
## CO2 Monitoring with a Rasperry Pi :monkey:

This projects aims to monitor the CO2-level of a room and displays it on a RGB-LED. In addition to that, if the CO2-level of the room is higher than healthy for people, a buzzer starts to beep in order to warn the people in that room. To furthermore visualize the CO2-Level a RGB-LED is functioning as a kind of traffic light to prohylacticly signal the conentration.

In times of covid, this application finds use in schools and other buildings where many people are gathered in one room together.
That is due to the fact that a low CO2-level is also signalising a low level of aersol. The beep of the buzzer reminds to ventilate the room. 

In addition to the CO2-level measurement, this application also measures the humidity and the temperature of the room. Those measurements are uploaded to an online database so the behaviour of the room can be monitored.

*Link to the online database:* https://thingspeak.com/channels/1290605


## Hardware equipment needed
- 1 x [Rasberry Pi with Power Supply](https://www.raspberrypi.org/products/): Version 3 and up 
- 1 x [Temperature Sensor](https://media.digikey.com/pdf/Data%20Sheets/Adafruit%20PDFs/DHT11_Humidity_TempSensor.pdf): DHT11-Type 
- 1 x [CO2 Sensor](https://www.winsen-sensor.com/d/files/PDF/Infrared%20Gas%20Sensor/NDIR%20CO2%20SENSOR/MH-Z19%20CO2%20Ver1.0.pdf)
- 1 x [Active Buzzer](https://arduinomodules.info/ky-012-active-buzzer-module/)
- 1 x [RGB LED](https://arduinomodules.info/ky-016-rgb-full-color-led-module/)
- 1 x 200Ohm Resistor
- Jumper Wires: Male to Male, Female to Male

## RGB-LED
[testfile](/test_RGB.py)

'''python

import RPi.GPIO as GPIO

import time

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BOARD)

blue = 11           # blue LED is connected to Pin 11
red = 12            # red LED is connected to Pin 12
green = 13          # green LED is connected to Pin 13
button = 10         # Button is connected to Pin 14

GPIO.setup(blue, GPIO.OUT)  #Blue LED
GPIO.setup(red, GPIO.OUT)   #Red LED
GPIO.setup(green, GPIO.OUT) #Green LED
GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_UP) #button PD

colors = [0xFF0000, 0x0F0F00, 0x00FF00]
pwm_red = GPIO.PWM(red, 5000)   #PWM with Frequency of 2kHz
pwm_blue = GPIO.PWM(blue, 5000)
pwm_green = GPIO.PWM(green, 5000)

pwm_red.start(0)    # duty cycle set 0
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
    if GPIO.input(button) == GPIO.LOW:  # push-buton pressed
        setColor(colors[i])             #set color 
        i+=1                            # increment i by 1
        if(i>=3):                       #reset i to 0
            i=0
        time.sleep(0.1)                 #no keybounce
'''
## Active buzzer
[testfile](/test_buzzer.py)
## Temperature and humidity sensor
[testfile](/test_buzzer.py)
## CO2 sensor
[testfile](/temp_online.py)
## Database
[testfile](/temp_online.py)
## Final project

