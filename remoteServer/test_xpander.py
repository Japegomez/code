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


spiComm = spidev.SpiDev()
spiComm.open(0, 0)

#configure IOCON check https://www.mouser.es/datasheet/2/268/MCP23017_Data_Sheet_DS20001952-2998473.pdf page17
set_gpio(8, 0)
spiComm.xfer2([0x40, 0x0a, 0x28], 5000000, 1000)
set_gpio(8, 1)

# Set pins as output on both banks
set_gpio(8, 0)
spiComm.xfer2([0x40, 0x00, 0x00], 5000000, 1000)
set_gpio(8, 1)

set_gpio(8, 0)
spiComm.xfer2([0x40, 0x01, 0x00], 5000000, 1000)
set_gpio(8, 1)

# Set output pins low level
set_gpio(8, 0)
spiComm.xfer2([0x40, 0x14, 0x00], 5000000, 1000)
set_gpio(8, 1)

set_gpio(8, 0)
spiComm.xfer2([0x40, 0x15, 0x00], 5000000, 1000)
set_gpio(8, 1)



#Same on second chip
#configure IOCON 
set_gpio(8, 0)
spiComm.xfer2([0x42, 0x0a, 0x28], 5000000, 1000)
set_gpio(8, 1)

# Set pins as output on both banks
set_gpio(8, 0)
spiComm.xfer2([0x42, 0x00, 0x00], 5000000, 1000)
set_gpio(8, 1)

set_gpio(8, 0)
spiComm.xfer2([0x42, 0x01, 0x00], 5000000, 1000)
set_gpio(8, 1)

# Set output pins low level
set_gpio(8, 0)
spiComm.xfer2([0x42, 0x14, 0x00], 5000000, 1000)
set_gpio(8, 1)

set_gpio(8, 0)
spiComm.xfer2([0x42, 0x15, 0x00], 5000000, 1000)
set_gpio(8, 1)

while True:

	try:

		set_gpio(18, 0)
		# microchip1 all portA I/0 set to 1
		spiComm.xfer2([0x40, 0x14, 0xff], 5000000, 1000)
		# microchip1 all portB I/0 set to 1
		spiComm.xfer2([0x40, 0x15, 0xff], 5000000, 1000)
		# microchip2 all portA I/0 set to 0
		spiComm.xfer2([0x42, 0x14, 0x00], 5000000, 1000)
		# microchip2 all portB I/0 set to 0
		spiComm.xfer2([0x42, 0x15, 0x00], 5000000, 1000)
		set_gpio(18, 1)

		time.sleep(2)

		set_gpio(18, 0)
		# microchip1 all portA I/0 set to 0
		spiComm.xfer2([0x40, 0x14, 0x00], 5000000, 1000)
		# microchip1 all portB I/0 set to 0
		spiComm.xfer2([0x40, 0x15, 0x00], 5000000, 1000)
		# microchip2 all portA I/0 set to 1
		spiComm.xfer2([0x42, 0x14, 0xff], 5000000, 1000)
		# microchip2 all portB I/0 set to 1
		spiComm.xfer2([0x42, 0x15, 0xff], 5000000, 1000)
		set_gpio(18, 1)


		time.sleep(2)

	except KeyboardInterrupt:
		spiComm.close()
