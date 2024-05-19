import spidev
import time

# Changes level from low to high and vice-versa in the gpio output pins
# Works using both spidev CS or external GPIO-based CS


# PINOUT

# A0 - A1 - A2 			tied to GND
# Reset					tied to 3V3
# MOSI					tied to rpi MOSI
# MISO					floating
# SCLK					tied to rpi SCLK
# CS					tied to rpi GPIO 8
# VSS					tied to GND
# VDD					tied to 3V3
# All Outputs			tied to Arduino directly
# INTA					floating
# INTB					floating

def set_gpio(gpio, value):

	try:
		with open("/sys/class/gpio/gpio{}/value".format(gpio), "w") as val:
			val.write("{}".format(value))

	except:
		pass

# set IOCON.HAEN check https://www.mouser.es/datasheet/2/268/MCP23017_Data_Sheet_DS20001952-2998473.pdf page17
def set_HAEN(exp):
	AddresByte = 0x40 + exp - 1
	set_gpio(8, 0)
	spiComm.xfer2([AddresByte, 0x0a, 0x28], 5000000, 1000)
	set_gpio(8, 1)

# Set pins as output/input on both banks
def set_pins(exp, output=1):
	AddresByte = 0x40 + exp - 1
	valueByte = 0x00 if output else 0xff
	
	set_gpio(8, 0)
	spiComm.xfer2([AddresByte, 0x00, valueByte], 5000000, 1000)
	set_gpio(8, 1)

	set_gpio(8, 0)
	spiComm.xfer2([0x40, 0x01, valueByte], 5000000, 1000)
	set_gpio(8, 1)
	
# Set output pins low level
def set_low(exp):
	AddresByte = AddresByte = 0x40 + (exp - 1) * 2

	set_gpio(8, 0)
	spiComm.xfer2([AddresByte, 0x14, 0x00], 5000000, 1000)
	set_gpio(8, 1)

	set_gpio(8, 0)
	spiComm.xfer2([AddresByte, 0x15, 0x00], 5000000, 1000)
	set_gpio(8, 1)
	
#spi connection
spiComm = spidev.SpiDev()
spiComm.open(0, 0)


for i in range(1, 5):
	set_HAEN(i)
	set_pins(i)
	set_low(i)
	
	

while True:

	try:
		set_gpio(18, 0)
		spiComm.xfer2([0x40, 0x14, 0x00], 5000000, 1000)
		set_gpio(18, 1)

		set_gpio(18, 0)
		spiComm.xfer2([0x42, 0x14, 0x00], 5000000, 1000)
		set_gpio(18, 1)

		set_gpio(18, 0)
		spiComm.xfer2([0x40, 0x14, 0x01], 5000000, 1000)
		set_gpio(18, 1)
		
		set_gpio(18, 0)
		spiComm.xfer2([0x40, 0x15, 0x00], 5000000, 1000)
		set_gpio(18, 1)

		set_gpio(18, 0)
		spiComm.xfer2([0x42, 0x14, 0x00], 5000000, 1000)
		set_gpio(18, 1)

		set_gpio(18, 0)
		spiComm.xfer2([0x42, 0x15, 0x00], 5000000, 1000)
		set_gpio(18, 1)


		print("12V ON")
		time.sleep(2)
		set_gpio(18, 0)
		spiComm.xfer2([0x40, 0x14, 0x00], 5000000, 1000)
		set_gpio(18, 1)

		set_gpio(18, 0)
		spiComm.xfer2([0x42, 0x14, 0x00], 5000000, 1000)
		set_gpio(18, 1)
		
		set_gpio(18, 0)
		spiComm.xfer2([0x40, 0x14, 0x00], 5000000, 1000)
		set_gpio(18, 1)

		set_gpio(18, 0)
		spiComm.xfer2([0x40, 0x15, 0x00], 5000000, 1000)
		set_gpio(18, 1)
		
		set_gpio(18, 0)
		spiComm.xfer2([0x42, 0x14, 0x01], 5000000, 1000)
		set_gpio(18, 1)

		set_gpio(18, 0)
		spiComm.xfer2([0x42, 0x15, 0x00], 5000000, 1000)
		set_gpio(18, 1)

		print("5V ON")
		time.sleep(2)

	except KeyboardInterrupt:
		spiComm.close()
