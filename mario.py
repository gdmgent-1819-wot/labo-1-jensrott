""" Labo 1
    Mario
"""

# Import everything we need
from sense_hat import SenseHat, ACTION_PRESSED, ACTION_HELD, ACTION_RELEASED

# Loading in SenseHat 
try:
    # Initialize SenseHat
    sense_hat = SenseHat()
    sense_hat.set_imu_config(False, False, False)
except:
    print('Unable to initialize the Sense Hat library: {}'.format(sys.exc_info()[0]))
    sys.exit(1)# Initialize 
sense = SenseHat()

# Defining colores 
R = [255, 0, 0]  # Red
S = [234,192,134] # Skin
X = [139,69,19] # Brown
B = [0,0,255] # Blue
O = [255,255,255] # White
Y = [255,255,0] # Yellow
G = [0,255,0] # Green

mario_high = [
    O, O, O, O, O, O, O, O,
    O, O, R, R, R, O, O, O,
    O, R, R, R, R, R, O, O,
    O, O, S, G, G, S, O, O,
    O, B, B, B, B, B, B, O,
    O, B, Y, B, B, Y, B, O,
    O, O, B, B, B, B, O, O,
    O, O, X, B, B, X, O, O
]

mario_low = [
     
    O, O, R, R, R, O, O, O,
    O, R, R, R, R, R, O, O,
    O, O, S, G, G, S, O, O,
    O, B, B, B, B, B, B, O,
    O, B, Y, B, B, Y, B, O,
    O, O, B, B, B, B, O, O,
    O, O, X, B, B, X, O, O,
    O, O, O, O, O, O, O, O,
]

def pushed_up(event):
    sense.clear()
    sense.set_pixels(mario_high)
    if event.action != ACTION_RELEASED:
        sense.clear()
        sense.set_pixels(mario_low)
        
        
def refresh():
    sense.clear()
    sense.set_pixels(mario_low)

sense.stick.direction_up = pushed_up