from seven import SevenSegmentDisplay, DisplayGroup
from utime import sleep

display_tens = SevenSegmentDisplay(12, 13, 7, 8, 9, 11, 10)
display_ones = SevenSegmentDisplay(18, 19, 20, 21, 22, 16, 17)

display_group = DisplayGroup(display_tens, display_ones)

display_group.display_number(13)

for i in range(99):
    display_group.display_number(i)
    sleep(0.25)
