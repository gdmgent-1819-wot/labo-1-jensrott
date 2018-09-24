""" Labo 1
    Mario
"""

# Import everything we need
from sense_hat import SenseHat

import sys

# Loading in SenseHat
try:
    # Initialize SenseHat
    sense_hat = SenseHat()
    sense_hat.set_imu_config(False, False, False)
except:
    print('Unable to initialize the Sense Hat library: {}'.format(sys.exc_info()[0]))
    sys.exit(1)# Initialize
sense = SenseHat()


def main():
    # TODO  

# Check if there is a main        
if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, SystemExit):
        print('Interrupt received! Stopping the application...')
    finally:
        print('Cleaning up the mess...')
        sys.exit(0)