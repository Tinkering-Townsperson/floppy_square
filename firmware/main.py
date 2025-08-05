"""
The main module for the floppy square game.

This module will contain the main gameloop/logic for the floppy square game.
"""

__version__ = "1.0.0"

###########
# IMPORTS #
###########

from seven import SevenSegmentDisplay, DisplayGroup
from screen import Screen
from button import Button


#########
# SETUP #
#########

# Display

SCL = 14
SDA = 15
DC = 4
CS = 5
RST = 6

screen = Screen(SCL, SDA, DC, CS, RST)

# Score counter

display_tens = SevenSegmentDisplay(12, 13, 7, 8, 9, 11, 10)
display_ones = SevenSegmentDisplay(18, 19, 20, 21, 22, 16, 17)

display_group = DisplayGroup(display_tens, display_ones)

# Buttons

button_a = Button(0, pullup=False)
button_b = Button(1, pullup=False)

##############
# GAME STATE #
##############


class States(object):
    ALIVE = "alive"
    WIN = "win"
    LOSE = "lose"


score = 0
state = States.ALIVE


##############
# GAME LOOP #
##############


def update_displays():
    display_group.display_number(score)


def handle_input():
    pass


@button_a.onclick
def button_a_pressed(*args, **kwargs):
    print("Hi!")


while state == States.ALIVE:
    update_displays()

if state == States.WIN:
    pass

if state == States.LOSE:
    pass
