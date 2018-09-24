""" Labo 1
    Message
"""

# Import everything we need
from sense_hat import SenseHat
from time import sleep
import sys


# Loading in SenseHat 
try:
    # Initialize SenseHat
    sense_hat = SenseHat()
    sense_hat.set_imu_config(False, False, False)
except:
    print('Unable to initialize the Sense Hat library: {}'.format(sys.exc_info()[0]))
    sys.exit(1)
    
def main():
    while True:
        # Show the message
        sense.show_message("Hello! We are New Media Development :)")
        
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

