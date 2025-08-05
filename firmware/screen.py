from machine import Pin, SPI  # type: ignore
import gc9a01 as gc9a01  # type: ignore


class Screen:
	def __init__(self, scl: int = 14, sda: int = 15, dc: int = 4, cs: int = 5, rst: int = 6):
		self.scl = scl
		self.sda = sda
		self.dc = dc
		self.cs = cs
		self.rst = rst

		self.spi = SPI(1, baudrate=60000000, sck=Pin(self.scl), mosi=Pin(self.sda))

		self.tft = gc9a01.GC9A01(
			self.spi, 240, 240,
			dc=Pin(self.dc, Pin.OUT),
			cs=Pin(self.cs, Pin.OUT),
			reset=Pin(self.rst, Pin.OUT),
		)

		self.tft.fill(gc9a01.BLACK)
