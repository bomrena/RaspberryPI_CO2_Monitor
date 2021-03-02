import RPi.GPIO as GPIO
import sys
import urllib2 #library needed for url actions
from time import sleep
import Freenove_DHT as DHT
GPIO.setwarnings(False)

DHTPin = 11
buzzer = 8

baseURL = "http://api.thingspeak.com/update?api_key=DIKFU2NDD22KUA70&"  #URL for the Thingspeak (Database) Channel. Teh api_key authorizes our channel
fieldCO2 = "field1="     #to upload the data directly into the right graphs, these fields are needed to be adressed
fieldTEMP = "field2="
fieldHUM = "field3="
fieldWARNING = "field4="

dht = DHT.DHT(DHTPin)   #create a DHT class object
def loop():
    while(True):
        temp_data = dht.readDHT11()
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
        print("Humidity : %.2f, \t Temperature : %.2f \n"%(dht.humidity,dht.temperature))
        sleep(5)

if __name__ == '__main__':
    print ('Program is starting ... ')
    try:
        loop()
    except KeyboardInterrupt:
        GPIO.cleanup()
        exit() 
