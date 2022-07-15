#######################################################
#     Spiros Daskalakis                               #
#     last Revision: 14/07/2022                       #
#     Python Version:  3.9                            #
#     Email: daskalakispiros@gmail.com                #
#######################################################

from pyftdi.ftdi import Ftdi
import psemi_mapping as psemi_switch
from pyftdi.gpio import GpioAsyncController

print("Print FTDI Connected Devices:")
print(Ftdi.show_devices())

gpio = GpioAsyncController()
# FT232R features a single port, which is 8-bit wide: DBUS,
# Direction
# A logical 0 bit represents an input pin
# A logical 1 bit represents an output pin
gpio.configure('ftdi://ftdi:232:AQ00ANA8/1', direction=0b_1111_1111)
# Set all pins to 0
gpio.write(0x0)

gpio.write(psemi_switch.LED_ON)
# Example
my_PE42562 = psemi_switch.PE42X62_dict
PE42562_outputs = ['RFC_RF1', 'RFC_RF2', 'RFC_RF3', 'RFC_RF4', 'RFC_RF5', 'RFC_RF6']
# Control Loop thru all the outputs of the RF switch.
for key in PE42562_outputs:
    print(key, '->', my_PE42562[key])
    gpio.write(my_PE42562[key])
