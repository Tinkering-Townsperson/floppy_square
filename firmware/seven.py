from machine import Pin  # type: ignore


class SevenSegmentDisplay:
	patterns = (
#	 	(A, B, C, D, E, F, G),  # noqa
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

	def __init__(self, A: int, B: int, C: int, D: int, E: int, F: int, G: int):
		"""Initialize the display

		Args:
			A (int): Pin for Segment A
			B (int): Pin for Segment B
			C (int): Pin for Segment C
			D (int): Pin for Segment D
			E (int): Pin for Segment E
			F (int): Pin for Segment F
			G (int): Pin for Segment G
		"""

		segments = (A, B, C, D, E, F, G)
		self.pins = [Pin(segment, Pin.OUT) for segment in segments]
		self.current_pattern = (0, 0, 0, 0, 0, 0, 0)
		self.update_pattern()

	def value(self, value: int | bool):
		"""Toggle the display

		Args:
			value (int or bool): Value to set (on or off)
		"""

		if value:
			self.update_pattern()
		else:
			for pin in self.pins:
				pin.value(0)

	def reset(self):
		"""Reset the display
		"""

		self.current_pattern = (0, 0, 0, 0, 0, 0, 0)

		self.update_pattern()

	def display_digit(self, digit):
		"""Set `current_pattern` to the pattern for the given digit, then update the display.

		Args:
			digit (int): Digit to display
		"""

		self.current_pattern = self.patterns[digit]

		self.update_pattern()

	def update_pattern(self):
		"""Updates displayed pattern to the one stored in the `current_pattern` attribute.
		"""

		for i in range(0, 7):
			self.pins[i].value(self.current_pattern[i])


class DisplayGroup:
	def __init__(self, *displays: SevenSegmentDisplay):
		"""Initialize the display group

		Args:
			*displays (SevenSegmentDisplay): Displays in the group
		"""

		self.displays = displays

	def display_number(self, number: int):
		"""Display a number across multiple displays

		Args:
			number (int): The number to display
		"""

		number_string = str(number)

		if len(number_string) > len(self.displays):
			number_string = number_string[-len(self.displays):]
		elif len(number_string) < len(self.displays):
			number_string = "0" * (len(self.displays) - len(number_string)) + number_string

		for i in range(len(self.displays)):
			self.displays[i].display_digit(int(number_string[i]))
