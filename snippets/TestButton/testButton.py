import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library

button_pin = 10

def my_callback(channel):  
    if GPIO.input(button_pin):     # if port 25 == 1  
        print ("Rising edge detected on 25")
    else:                  # if port 25 != 1  
        print ("Falling edge detected on 25") 



GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)


GPIO.add_event_detect(button_pin, GPIO.BOTH,callback=my_callback, bouncetime=500) # Setup event on pin 10 rising edge


message = input("Press enter to quit\n\n") # Run until someone presses enter
GPIO.cleanup() # Clean up





