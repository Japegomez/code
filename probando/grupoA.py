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
	ControlByte = 0x40 + (exp - 1) * 2
	set_gpio(8, 0)
	spiComm.xfer2([ControlByte, 0x0a, 0x28], 5000000, 1000)
	set_gpio(8, 1)

# Set pins as output/input on both banks


def set_pins(exp, output=1):
	ControlByte = 0x40 + (exp - 1) * 2
	valueByte = 0x00 if output else 0xff

	set_gpio(8, 0)
	spiComm.xfer2([ControlByte, 0x00, valueByte], 5000000, 1000)
	spiComm.xfer2([ControlByte, 0x01, valueByte], 5000000, 1000)
	set_gpio(8, 1)

# Set output pins low level


def set_low(exp):
	ControlByte = 0x40 + (exp - 1) * 2

	set_gpio(8, 0)
	spiComm.xfer2([ControlByte, 0x14, 0x00], 5000000, 1000)
	spiComm.xfer2([ControlByte, 0x15, 0x00], 5000000, 1000)
	set_gpio(8, 1)


# spi connection
spiComm = spidev.SpiDev()
spiComm.open(0, 0)


for i in range(1, 4):
	set_HAEN(i)
	set_pins(i)
	set_low(i)


while True:

	try:
	    # ponemos todo el expansor1 y expansor2 a 0
		set_gpio(8, 0)
		set_low(1)
		set_low(2)
		set_gpio(8, 1)

		# caso A.1
		set_gpio(8, 0)
		# A7 A6 A5 A4 A3 A2 A1 A0 / 00001110
		spiComm.xfer2([0x40, 0x14, 0x0e], 5000000, 1000)
		# B7 B6 B5 B4 B3 B2 B1 B0 / 00010101
		spiComm.xfer2([0x40, 0x15, 0x15], 5000000, 1000)
		set_gpio(8, 1)

		print("LED1 5V 100ohms")
		time.sleep(2)

        # ponemos todo el expansor1 a 0
		set_gpio(8, 0)
		set_low(1)
		set_low(2)
		set_gpio(8, 1)

		# caso A.2
		set_gpio(8, 0)
		# A7 A6 A5 A4 A3 A2 A1 A0 / 00001110
		spiComm.xfer2([0x40, 0x14, 0x0e], 5000000, 1000)
		# B7 B6 B5 B4 B3 B2 B1 B0 / 00001101
		spiComm.xfer2([0x40, 0x15, 0x0d], 5000000, 1000)
		set_gpio(8, 1)

		print("LED1 5V 300ohms")
		time.sleep(2)

        # ponemos todo el expansor1 a 0
		set_gpio(8, 0)
		set_low(1)
		set_low(2)
		set_gpio(8, 1)

		# caso A.3
		set_gpio(8, 0)
		# A7 A6 A5 A4 A3 A2 A1 A0 / 00001101
		spiComm.xfer2([0x40, 0x14, 0x0d], 5000000, 1000)
		# B7 B6 B5 B4 B3 B2 B1 B0 / 00010101
		spiComm.xfer2([0x40, 0x15, 0x15], 5000000, 1000)
		set_gpio(8, 1)

		print("LED1 12V 100ohms")
		time.sleep(2)

        # ponemos todo el expansor1 a 0
		set_gpio(8, 0)
		set_low(1)
		set_low(2)
		set_gpio(8, 1)

		# caso A.4
		set_gpio(8, 0)
		# A7 A6 A5 A4 A3 A2 A1 A0 / 00001101
		spiComm.xfer2([0x40, 0x14, 0x0d], 5000000, 1000)
		# B7 B6 B5 B4 B3 B2 B1 B0 / 00001101
		spiComm.xfer2([0x40, 0x15, 0x0d], 5000000, 1000)
		set_gpio(8, 1)

		print("LED1 12V 300ohms")
		time.sleep(2)
	except KeyboardInterrupt:
		spiComm.close()
