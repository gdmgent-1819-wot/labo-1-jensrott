""" Labo 1
    Rolling Dice
"""

# Import everything we need
from sense_hat import SenseHat
from time import sleep
from random import randint
import sys

# Loading in SenseHat 
try:
    # Initialize SenseHat
    sense_hat = SenseHat()
    sense_hat.set_imu_config(False, False, False)
except:
    print('Unable to initialize the Sense Hat library: {}'.format(sys.exc_info()[0]))
    sys.exit(1)

def roll():
    raw = sense_hat.get_accelerometer_raw()
    x = raw['x']
    print(x)
    # TODO #       
            
def main():
    roll()
        
# Check if there is a main         
if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, SystemExit):
        print('Interrupt received! Stopping the application...')
    finally:
        print('Cleaning up the mess...')
        sys.exit(0)
