# RaspberryPI_CO2_Monitor
## CO2 monitoring with a rasperry pi :monkey:

This project aims to monitor the CO2-level of a room and displays it on a RGB-LED. In addition to that, if the CO2-level of the room is higher than healthy for people, a buzzer starts to beep in order to warn the people in that room. To furthermore visualize the CO2-Level a RGB-LED is functioning as a kind of traffic light to prophylactically signal the concentration.

In times of covid, this application finds use in schools and other buildings where many people are gathered in one room together. That is due to the fact that a low CO2-level is also signalising a low level of aerosol. The beep of the buzzer reminds to ventilate the room.

In addition to the CO2-level measurement, this application also measures the humidity and the temperature of the room. Those measurements are uploaded to an online database so the behaviour of the room can be monitored.

*Link to the online database:* https://thingspeak.com/channels/1290605

## hardware equipment needed
- 1 x [Rasberry Pi with Power Supply](https://www.raspberrypi.org/products/): Version 3 and up 
- 1 x [Temperature Sensor](https://media.digikey.com/pdf/Data%20Sheets/Adafruit%20PDFs/DHT11_Humidity_TempSensor.pdf): DHT11-Type 
- 1 x [CO2 Sensor](https://www.winsen-sensor.com/d/files/PDF/Infrared%20Gas%20Sensor/NDIR%20CO2%20SENSOR/MH-Z19%20CO2%20Ver1.0.pdf)
- 1 x [Active Buzzer](https://arduinomodules.info/ky-012-active-buzzer-module/)
- 1 x [RGB LED](https://arduinomodules.info/ky-016-rgb-full-color-led-module/)
- 1 x [Push Button](https://www.amazon.de/Youmile-100er-Pack-Miniatur-Mikro-Taster-Tastschalter-Qualit%C3%A4tsschalter-Miniature-6-x-5-mm/dp/B07Q1BXV7T/)
- 3 x 220Ohm Resistor
- Jumper Wires: Male to Male, Female to Male

## INSTRUCTION MANUAL
### HARDWARE SETUP

The conections between the RPI and the components are visible in the following table:

| Component | Pin|
| :---: | :---: |
| DHT11 | 11 |
| MHZ19 RX | 8 |
| MHZ19 TX | 10 |
| Buzzer | 16 |
| RGB LED Green Pin | 13 |
| RGB LED Red Pin | 12 |
| RGB LED Blue Pin | 15 |
| Button | 18 |

LED serial resistor = 220 Ohm

### SOFTWARE SETUP

To execute the project, you first have to download the libary for the mhz19 module. 

This can be done as follows:
` pip install mh-z19 `

To read one co2 value from the sensor, use the following instruction:
` sudo python -m mh_z19 `

To correctly run this application just simply download the "CO2_Monitor.py" file on your raspberry pi via the Github website. 
Alternatively you can also copy this "gh repo clone bomrena/RaspberryPI_CO2_Monitor" command into your Console if you are running a Linux operating system on your raspberry pi.
Now start the skript as superuser and everything should work. The sudo rights are necessary because of conflicts when opening a serial communication.

When you have opened the terminal you need to navigate to the folder where you have the copy of the final project. If you have done this you can now start the project with the command:
` sudo python  CO2_Monitor.py `

Download the software of the final project via the following link.

[Final Project](/CO2_Monitor.py)

#### TROUBLESHOOTING SIDENOTE
If you get an error running the python script using your normal python shell then try running it via "Geany".

## RGB-LED
As already mentioned in the hardware equipment part, the LED used as an optical indicator for the CO2 value of the room.
There are three different light-modes:

- green:   250 - 1000 ppm (normal outdoor air level - typical level found in occupied spaces with good air exchange)
- orange:  1000 - 2000 ppm (level associated with complaints of drowsiness and poor air)
- red:     2000 and above (level associated with headaches, sleepiness and poor concentration)

source: https://www.indoordoctor.com/indoor-carbon-dioxide-levels-health/

The RGB-led is made out of three different leds (red, green, blue). The color of the emitted light depends on the duty cycle of each of the leds.
- The red led is connected on PIN 12
- The green led is connected on PIN 13
- The blue led is connected on PIN 10

In order to see what duty-cycle you need for your color of the led, visit: https://www.w3schools.com/colors/colors_rgb.asp

[RGB_TST](/test_RGB.py)
## ACTIVE BUZZER
The sound of the active buzzer can be controlled over the duty-cycle of the connected pin. It is connected to PIN 8 on the Raspberrypi.

[BUZ_TST](/test_buzzer.py)

## TEMPERATURE AND HUMIDITY SENSOR
The temperature and humidity sensor used in this project is the DHT11.
There is already a great explaination on how to use this sensor. You can find it on https://thinkingofpi.com/getting-started/raspberry-pi-dht11/
Please notice that the DHT11 is connected on PIN 11.

[TEMP&DATA_TST](/temp_online.py)


## DATABASE
The online database to display the measurements of the temperature und CO2 value is https://thingspeak.com/
You can create an account and are able to upload data on the database every 15 seconds.
You will get a key to your created database. With this key, you can upload data from every device you use. 

In order to select the correct graph to upload your data to, you just need to change the field to the one you want to use. We are using
- CO2: field1 (shows the CO2 level of the room)
- Temperature field2 (shows the temperature of the room)
- Humidity field3 (shows the humidity of the room)
- Warning field4 (shows if a warning was set active)



[TEMP&DATA_TST](/temp_online.py)

## CO2 SENSOR
the testfile for the CO2-Sensor can be downloaded via the following link.

Please notice that the RX-Pin of the MH-Z19 must be connected to PIN 8 and the TX-Pin to PIN 10.

[testfile](/co2_test.py)




