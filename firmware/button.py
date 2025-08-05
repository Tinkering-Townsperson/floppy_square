from machine import Pin  # type: ignore


class Button:
	def __init__(self, pin: int, pullup: bool = True) -> None:
		self.pin = Pin(pin, Pin.IN, Pin.PULL_UP if pullup else Pin.PULL_DOWN)

	def value(self) -> bool:
		return self.pin.value()

	def __bool__(self) -> bool:
		return self.value()

	def onpress(self, func):
		self.pin.irq(trigger=Pin.IRQ_RISING, handler=func)
		return func

	def onrelease(self, func):
		self.pin.irq(trigger=Pin.IRQ_FALLING, handler=func)
		return func
