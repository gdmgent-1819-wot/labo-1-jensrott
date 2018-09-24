""" Labo 1
    Fireworks
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

def draw_pixels():
    while True:
        for x in range(0,8):
            for y in range(0,8):
                sense_hat.clear()
                sense_hat.set_pixel(x,y, randint(0,255), randint(0,255), randint(0,255))
                
def main():
    draw_pixels()
    
# Check if there is a main        
if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, SystemExit):
        print('Interrupt received! Stopping the application...')
    finally:
        print('Cleaning up the mess...')
        sys.exit(0)
            
