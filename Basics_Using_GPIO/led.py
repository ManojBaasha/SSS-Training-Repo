from gpiozero import LED
import time
# Line 1 takes in library for controlling GPIO pins and line 2 imports a time library used for later

# Now we begin by using the library. We're using GPIO pin 17 as referenced from Raspi Documentation
# Source for pinout: notenoughtech.com/raspberry-pi/rpi-gpio/

# We create an LED object and call it "led", confusing but manageable. We use 17 to denote which GPIO pin we're using
'''
led = LED(17)
'''

# Now we use a built in function for the "led" object which is ".on()", this causes the led to flicker on
'''
led.on()
'''

# What if we want it to stay on for longer?

'''
led.on()
time.sleep(10)
'''

# We made the program halt its current state for ten seconds, allowing us to see the led stay on for 10 seconds!

# Let's make things more interesting and take in user input and combine it with conditional statements!

while True:
    # Take in user input
    yes_no_input = input("Would you like to turn on the LED? Type Y for Yes or N for No: ")
    
    # Error Checking
    if yes_no_input != "Y" and yes_no_input != "N":
        print("Please use Y for Yes or N for No ")
        continue
    
    # Break out since inputs are valid
    else:
        break

# Since the user wants the LED on we figure out for how long
if yes_no_input == "Y":
    
    # Loops until valid entry value is met
    while True:
        
        # Error handling approach, see this for more details: https://docs.python.org/3/tutorial/errors.html
        try:
            duration = int(input("For how long would you like the LED to stay on? "))
        
        # Error Checking
        except ValueError:
            print("Please enter a valid integer value ")
            continue
        
        #Break out since inputs are valid
        else:
            break
    

    # Initialize GPIO pin for use (we're using GPIO 17 in this example)
    led = LED(17)

    # Send power to GPIO pin 17
    led.on()

    # Halt the program for however long the user would like to keep the LED on
    time.sleep(duration)






