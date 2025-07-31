from machine import Pin  # type: ignore
import utime  # type: ignore

# Define the GPIO pins for each segment
segments = (12, 13, 7, 8, 9, 11, 10)
# Define the digit patterns for 0-9 on the 7-segment display
# 1 means the segment is on, 0 means the segment is off
patterns = (
# 	(A, B, C, D, E, F, G),  # noqa
	(1, 1, 1, 1, 1, 1, 0),  # 0
	(0, 1, 1, 0, 0, 0, 0),  # 1
	(1, 1, 0, 1, 1, 0, 1),  # 2
	(1, 1, 1, 1, 0, 0, 1),  # 3
	(0, 1, 1, 0, 0, 1, 1),  # 4
	(1, 0, 1, 1, 0, 1, 1),  # 5
	(1, 0, 1, 1, 1, 1, 1),  # 6
	(1, 1, 1, 0, 0, 0, 0),  # 7
	(1, 1, 1, 1, 1, 1, 1),  # 8
	(1, 1, 1, 0, 0, 1, 1)   # 9
)

# Initialize the GPIO pins
pins = [Pin(seg, Pin.OUT) for seg in segments]


def display_digit(digit):
	# Get the pattern for the digit
	pattern = patterns[digit]

	# Set each segment to the correct state
	for i in range(0, 7):
		pins[i].value(pattern[i])


num = 0

# Test the display
while True:
	for i in range(10):
		start = utime.ticks_ms()
		while utime.ticks_diff(utime.ticks_ms(), start) < 1000:
			try:
				num = int(input("Enter a digit (0-9): "))
			except ValueError:
				print()
			else:
				display_digit(num)
