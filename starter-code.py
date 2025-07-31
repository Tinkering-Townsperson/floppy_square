from machine import Pin, SPI
import gc9a01 as gc9a01
# hardware config
SCL_PIN = 14  # chip pin 19
SDA_PIN = 15  # chip pin 20
DC_PIN = 4    # chip pin 6
CS_PIN = 5    # chip pin 7
RST_PIN = 6   # chip pin 9
spi = SPI(1, baudrate=60000000, sck=Pin(SCL_PIN), mosi=Pin(SDA_PIN))
# initialize the display
tft = gc9a01.GC9A01(
    spi, 240, 240,
    dc=Pin(DC_PIN, Pin.OUT),
    cs=Pin(CS_PIN, Pin.OUT),
    reset=Pin(RST_PIN, Pin.OUT),
    )
tft.fill(gc9a01.BLACK)
print("black")
# x, y, width, height
# red
tft.fill_rect(50,  75, 50, 60, gc9a01.color565(255, 0, 0))
print("red")
# green
tft.fill_rect(100, 75, 50, 60, gc9a01.color565(0, 255, 0))
print("green")
# blue
tft.fill_rect(150, 75, 50, 60, gc9a01.color565(0, 0, 255))
print("blue")
