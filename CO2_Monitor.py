import RPi.GPIO as GPIO
import sys
import urllib.request as urllib2 #library needed for url actions
from time import sleep
import time
import Freenove_DHT as DHT
import mh_z19
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

LED_blue = 10           # blue LED is connected to Pin 10
LED_red = 12            # red LED is connected to Pin 12
LED_green = 13          # green LED is connected to Pin 13
DHTPin = 11
buzzer = 8

color_red=0xFF0000
color_green=0x00FF00
color_orange=0x0F0F00


GPIO.setup(LED_blue, GPIO.OUT)  #Blue LED
GPIO.setup(LED_red, GPIO.OUT)   #Red LED
GPIO.setup(LED_green, GPIO.OUT) #Green LED



pwm_red = GPIO.PWM(LED_red, 5000)   #PWM with Frequency of 2kHz
pwm_blue = GPIO.PWM(LED_blue, 5000)
pwm_green = GPIO.PWM(LED_green, 5000)

pwm_red.start(0)                # duty cycle set 0
pwm_blue.start(0)
pwm_green.start(0)

pwm_blue.ChangeDutyCycle(0)



baseURL = "http://api.thingspeak.com/update?api_key=DIKFU2NDD22KUA70&"  #URL for the Thingspeak (Database) Channel. Teh api_key authorizes our channel
fieldCO2 = "field1="     #to upload the data directly into the right graphs, these fields are needed to be adressed
fieldTEMP = "field2="
fieldHUM = "field3="
fieldWARNING = "field4="

dht = DHT.DHT(DHTPin)   #create a DHT class object


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

setColor(color_orange)

def loop():
    while(True):
        temp_data = dht.readDHT11()
        co2_data=mh_z19.read()
        
        i = urllib2.urlopen(baseURL + fieldCO2 + str(co2_data["co2"])) #this command later opens a url. The "+" arguments are additions to the base url.
                                                                           #"fieldTemp" leads to the right graph, while the "str(...)" string is the actual data
        i.read()     #opening the stored function x
        i.close()    #closing the function
        sleep(20)    #the databse accepts new data every 15 seconds
        
        if (temp_data is dht.DHTLIB_OK):      #read DHT11 and get a return value. Then determine whether data read is normal according to the return value.
           print("DHTLIB_OK!!")
           x = urllib2.urlopen(baseURL + fieldTEMP + str(dht.temperature)) #this command later opens a url. The "+" arguments are additions to the base url.
                                                                           #"fieldTemp" leads to the right graph, while the "str(...)" string is the actual data
           x.read()     #opening the stored function x
           x.close()    #closing the function
           sleep(20)    #the databse accepts new data every 15 seconds
           if(dht.humidity < 100):
                y = urllib2.urlopen(baseURL + fieldHUM + str(dht.humidity))
                y.read()
                y.close()
        print("Humidity : %.2f, \t Temperature : %.2f, \t CO2: %.2f \n"%(dht.humidity,dht.temperature,co2_data["co2"]))
        sleep(10)
        if(co2_data["co2"]<1000):       #co2 < 1000ppm normal outdor level
              setColor(color_green)  
        elif(co2_data["co2"]<1000):  #co2: 1000-2000ppm level associated with complains of drowsiness and poor air 
                setColor(color_orange)  
        
        else:                           #co2: > 2000 level associated with headaches, sleepiness and poor concentration
                setColor(color_red)  





if __name__ == '__main__':
    print ('Program is starting ... ')
    try:
        loop()
    except KeyboardInterrupt:
        GPIO.cleanup()
        exit() 
