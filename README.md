# RaspberryPI_CO2_Monitor
## CO2 monitoring with a rasperry pi :monkey:

This projects aims to monitor the CO2-level of a room and displays it on a RGB-LED. In addition to that, if the CO2-level of the room is higher than healthy for people, a buzzer starts to beep in order to warn the people in that room. To furthermore visualize the CO2-Level a RGB-LED is functioning as a kind of traffic light to prohylacticly signal the conentration.

In times of covid, this application finds use in schools and other buildings where many people are gathered in one room together.
That is due to the fact that a low CO2-level is also signalising a low level of aersol. The beep of the buzzer reminds to ventilate the room. 

In addition to the CO2-level measurement, this application also measures the humidity and the temperature of the room. Those measurements are uploaded to an online database so the behaviour of the room can be monitored.

*Link to the online database:* https://thingspeak.com/channels/1290605

## hardware equipment needed
- 1 x [Rasberry Pi with Power Supply](https://www.raspberrypi.org/products/): Version 3 and up 
- 1 x [Temperature Sensor](https://media.digikey.com/pdf/Data%20Sheets/Adafruit%20PDFs/DHT11_Humidity_TempSensor.pdf): DHT11-Type 
- 1 x [CO2 Sensor](https://www.winsen-sensor.com/d/files/PDF/Infrared%20Gas%20Sensor/NDIR%20CO2%20SENSOR/MH-Z19%20CO2%20Ver1.0.pdf)
- 1 x [Active Buzzer](https://arduinomodules.info/ky-012-active-buzzer-module/)
- 1 x [RGB LED](https://arduinomodules.info/ky-016-rgb-full-color-led-module/)
- 1 x [Push Button](https://www.amazon.de/Youmile-100er-Pack-Miniatur-Mikro-Taster-Tastschalter-Qualit%C3%A4tsschalter-Miniature-6-x-5-mm/dp/B07Q1BXV7T/)
- 1 x 200Ohm Resistor
- Jumper Wires: Male to Male, Female to Male

## INSTRUCTION MANUAL
### HARDWARE SETUP
| Component | Pin|
| :---: | :---: |
| DHT11 | 301 |
| MHZ19 | 301 |
| Buzzer | 301 |
| RGB LED Green Pin | 301 |
| RGB LED Red Pin | 301 |
| RGB LED Blue Pin | 301 |
| Button | 301 |

LED serial resistor =220k

### SOFTWARE SETUP
To correctly run this application just simply download the "final_project.py" file on your raspberry pie via the Github website. 
Alternatively you can also copy this "gh repo clone bomrena/RaspberryPI_CO2_Monitor" command into your Console if you are running a Linux operating system on your raspberry pie.
Now to start the script just double click the "final_project.py" file and everything should work.

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
[testfile](/)


## FINAL PROJECT

