"""
Labo 1
Pixelator
"""

# Importing everything we need 
from sense_hat import SenseHat
from random import randint
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
    
# Give a start number and end number you want the speed at, I generate a random between the two 
def startEnd(start, end):
    randomNumber = randint(start, end)
    print(randomNumber)
    return start + end

# If you want to add your own number that is possible. Left this here because why not? ¯\_(ツ)_/¯ 
def putInNumber():
    # Also possible this way, we will need to make it an integer to work 
    SelfInput = int(input('Put in how long you want to wait everytime: '))
    return SelfInput
    
def loopOver():
    for y in range(0,8):
        for x in range(0,8):
            # Clear the screen only show what is overlooped  
            sense_hat.clear()
            sense_hat.set_pixel(x,y, randint(0,255), randint(0,255), randint(0,255))
            # The speed at which the loop goes # 
            sleep(startEnd(0,2))


def main():
    while True:
        loopOver()
            
# Check if there is a main         
if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, SystemExit):
        print('Interrupt received! Stopping the application...')
    finally:
        print('Cleaning up the mess...')
        sys.exit(0)
            
