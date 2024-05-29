from __future__ import unicode_literals, print_function, division
import uuid
from mylab import weblab
from flask_babel import gettext
from weblablib import weblab_user
import spidev

from mylab.api.models import Measurements

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

spiComm = spidev.SpiDev()

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
	set_gpio(8, 1);


@weblab.on_start
def start(client_data, server_data):
    print("************************************************************************")
    print("Preparing laboratory for user {}...".format(weblab_user.username))

    spiComm.open(0, 0)
    for i in range(1, 4):
        set_HAEN(i)
        set_pins(i)
    clean_resources()
    spiComm.close()
    print("Lab is ready!!")
    print("************************************************************************")


@weblab.on_dispose
def dispose():
    print("************************************************************************")
    print("Switching off laboratory for user {}...".format(weblab_user.username))
    clean_resources()
    spiComm.close()
    print("************************************************************************")




def clean_resources():
    for i in range(1, 4):
        set_low(i)

def hardware_status():
    return None

def get_measurements(caso, numero):
    # Implementar la lógica para obtener los valores de intensidad y tensión
    # Ejemplo de datos de prueba
    if(caso == 'A'):
        if(numero == 1):
            current_measurements = [30.1, 30.1, 30.1]
            voltage_measurements = [2.16, 3.05, 5.24]
        elif(numero == 2):
            current_measurements = [9.96,9.96,9.96]
            voltage_measurements = [1.89, 3.33, 5.24]
        elif(numero == 3):
            current_measurements = [92.3,92.3,92.3]
            voltage_measurements = [2.85, 9.07, 11.98]
        elif(numero == 4):
            current_measurements = [29.9,29.9,29.9]
            voltage_measurements = [2.15, 9.8, 11.98]
    else:
        current_measurements = [0,0,0]
        voltage_measurements = [0,0,0]
        
    return Measurements(id=uuid.uuid4(), current=current_measurements, voltage=voltage_measurements)

@weblab.task(unique='global')
def configure_lab(caso, numero):
    spiComm.open(0, 0)
    if weblab_user.time_left < 5:
        print("************************************************************************")
        print("Error: typically, configuring the lab takes around 5 seconds. So if ")
        print("the user has less than 5 seconds (%.2f) to use the laboratory, don't start " %
              weblab_user.time_left)
        print("this task. Otherwise, the user session will still wait until the task")
        print("finishes, delaying the time assigned by the administrator")
        print("************************************************************************")
        return {
            'success': False,
            'reason': "Too few time: {}".format(weblab_user.time_left)
        }
    

    if caso == 'A':
        if numero == 1:
            clean_resources()

            set_gpio(8, 0)
            # A7 A6 A5 A4 A3 A2 A1 A0 / 00001110
            spiComm.xfer2([0x40, 0x14, 0x0e], 5000000, 1000)
            # B7 B6 B5 B4 B3 B2 B1 B0 / 00010101
            spiComm.xfer2([0x40, 0x15, 0x15], 5000000, 1000)

            # A7 A6 A5 A4 A3 A2 A1 A0 / 00000000
            spiComm.xfer2([0x42, 0x14, 0x00], 5000000, 1000)
            set_gpio(8, 1)
            print("LED1 5V 100ohms")

        elif numero == 2:
            clean_resources()

            # caso A.2
            set_gpio(8, 0)
            # A7 A6 A5 A4 A3 A2 A1 A0 / 00001110
            spiComm.xfer2([0x40, 0x14, 0x0e], 5000000, 1000)
            # B7 B6 B5 B4 B3 B2 B1 B0 / 00001101
            spiComm.xfer2([0x40, 0x15, 0x0d], 5000000, 1000)

            # A7 A6 A5 A4 A3 A2 A1 A0 / 00000000
            spiComm.xfer2([0x42, 0x14, 0x00], 5000000, 1000)
            set_gpio(8, 1)
            print("LED1 5V 300ohms")

        elif numero == 3:
            clean_resources()
            # caso A.3
            set_gpio(8, 0)
            # A7 A6 A5 A4 A3 A2 A1 A0 / 00001101
            spiComm.xfer2([0x40, 0x14, 0x0d], 5000000, 1000)
            # B7 B6 B5 B4 B3 B2 B1 B0 / 00010101
            spiComm.xfer2([0x40, 0x15, 0x15], 5000000, 1000)

            # A7 A6 A5 A4 A3 A2 A1 A0 / 00000000
            spiComm.xfer2([0x42, 0x14, 0x00], 5000000, 1000)
            set_gpio(8, 1)

            print("LED1 12V 100ohms")

        elif numero == 4:
            clean_resources()
		    # caso A.4
            set_gpio(8, 0)
            # A7 A6 A5 A4 A3 A2 A1 A0 / 00001101
            spiComm.xfer2([0x40, 0x14, 0x0d], 5000000, 1000)
            # B7 B6 B5 B4 B3 B2 B1 B0 / 00001101
            spiComm.xfer2([0x40, 0x15, 0x0d], 5000000, 1000)

            # A7 A6 A5 A4 A3 A2 A1 A0 / 00000000
            spiComm.xfer2([0x42, 0x14, 0x00], 5000000, 1000)
            set_gpio(8, 1)

            print("LED1 12V 300ohms")

    spiComm.close()
    return {
        'success': True
    }
