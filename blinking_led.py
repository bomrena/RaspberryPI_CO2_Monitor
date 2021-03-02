import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
from time import sleep # Import the sleep function from the time module
GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(8, GPIO.OUT, initial=GPIO.LOW) # Set pin 8 to be an output pin and set initial value to low (off)
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #set pin 10 to be an input data pin

while True: # Run forever
    if GPIO.input(10) == GPIO.HIGH: # push-buton pressed
        GPIO.output(8, GPIO.HIGH) # Turn on
    else:
        GPIO.output(8, GPIO.LOW) # Turn off