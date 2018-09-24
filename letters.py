""" Labo 1
    Letters
"""

# Import everything we need
from sense_hat import SenseHat
from time import sleep
from random import randint
import sys

# Looping over the word 
def loopWord():
    # Put string in variable 
    string = "NMD"
    for letter in string:
            # Show the letter and give each letter a random color 
            sense_hat.show_letter(letter, text_colour = [randint(0,255), randint(0,255),randint(0,255)])
            # Wait between one letter 1 second 
            sleep(1)

# Loading in SenseHat 
try:
    # Initialize SenseHat
    sense_hat = SenseHat()
    sense_hat.set_imu_config(False, False, False)
except:
    print('Unable to initialize the Sense Hat library: {}'.format(sys.exc_info()[0]))
    sys.exit(1)

# Loop over the string 
def main():
    while True:
        loopWord()
        
        # Clear the screen 
        sense_hat.clear()
        
        # Re do the looping because we are still in the while loop #
        sleep(2)
        
# Check if there is a main        
if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, SystemExit):
        print('Interrupt received! Stopping the application...')
    finally:
        print('Cleaning up the mess...')
        sys.exit(0)
   
