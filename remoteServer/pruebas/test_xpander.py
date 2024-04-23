import spidev
import time

# Changes level from low to high and vice-versa in the gpio output pins
# Works using both spidev CS or external GPIO-based CS


#PINOUT

#A0 - A1 - A2 			tied to GND
#Reset					tied to 3V3
#MOSI					tied to rpi MOSI
#MISO					floating
#SCLK					tied to rpi SCLK
#CS						tied to rpi GPIO 18
#VSS					tied to GND
#VDD					tied to 3V3
#All Outputs			tied to Arduino directly
#INTA					floating
#INTB					floating



def reserve_gpio(gpios):
	for gpio in gpios:
		
		try:
			with open("/sys/class/gpio/export","w") as res:
				res.write("{}".format(gpio))

			with open("/sys/class/gpio/gpio{}/direction".format(gpio),"w") as dir:
				dir.write("out")

			with open("/sys/class/gpio/gpio{}/value".format(gpio),"w") as val:
				val.write("1")
			
			print "GPIO {} reserved".format(gpio)

		except:
			print "Unable to reserve GPIO ".format(gpio)
			pass

def set_gpio(gpio, value):
		
	try:
		with open("/sys/class/gpio/gpio{}/value".format(gpio),"w") as val:
			val.write("{}".format(value))
	
	except:
		pass
			
def unreserve_gpio(gpios):
	for gpio in gpios:
		
		try:
			with open("/sys/class/gpio/unexport","w") as res:
				res.write("{}".format(gpio))
			
			print "GPIO {} unreserved".format(gpio)

		except:
			print "Unable to unreserve GPIO ".format(gpio)
			pass


gpios = [18]

reserve_gpio(gpios)

spiComm = spidev.SpiDev()
spiComm.open(0,0)


set_gpio(18, 0)
spiComm.xfer2([0x40, 0x0a, 0x20], 5000000, 1000)
set_gpio(18, 1)

# Set pins as output on both banks
set_gpio(18, 0)
spiComm.xfer2([0x40, 0x00, 0x00], 5000000, 1000)
set_gpio(18, 1)

set_gpio(18, 0)
spiComm.xfer2([0x40, 0x01, 0x00], 5000000, 1000)
set_gpio(18, 1)

# Set output pins low level
set_gpio(18, 0)
spiComm.xfer2([0x40, 0x14, 0x00], 5000000, 1000)
set_gpio(18, 1)
		
set_gpio(18, 0)
spiComm.xfer2([0x40, 0x15, 0x00], 5000000, 1000)
set_gpio(18, 1)	



while True:

	try:
		set_gpio(18, 0)
		spiComm.xfer2([0x40, 0x14, 0xff], 5000000, 1000)
		set_gpio(18, 1)
		
		set_gpio(18, 0)
		spiComm.xfer2([0x40, 0x15, 0xff], 5000000, 1000)
		set_gpio(18, 1)	
		
		time.sleep(2)
		
		set_gpio(18, 0)
		spiComm.xfer2([0x40, 0x14, 0x00], 5000000, 1000)
		set_gpio(18, 1)
		
		set_gpio(18, 0)
		spiComm.xfer2([0x40, 0x15, 0x00], 5000000, 1000)
		set_gpio(18, 1)	
		
		time.sleep(2)
	
	except KeyboardInterrupt:
		spiComm.close()
		unreserve_gpio(gpios)