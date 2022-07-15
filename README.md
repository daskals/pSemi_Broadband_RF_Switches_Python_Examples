# pSemi_Broadband_RF_Switches_Python_Examples
Two Python Scripts for controlling the Broadband RF Switches from pSemi 

Link: https://www.psemi.com/products/family/broadband-rf-switches

The python script can control the:

--> PE42512/PE42412/PE426412 RF switches
--> PE42482/PE42582/PE426482 RF switches
--> PE42562/PE42462/PE426462 RF switches

The script uses the (red) USB Interface Board from Peregrine Semiconductor
-->  Its dased on the FT232R FTDI chip

Hints:
-->  Don't connect any Logic State Jumper on the RF switch Evaluation Board
--> In Windows: If the python doesn’t recognize the USB interface, you must install the WinUSB driver thru Zadig software (https://zadig.akeo.ie/)

Running steps:

-->  Copy the "psemi_mapping" file in the  Python project.
-->  Use the code in the "rf_switch.py" script to control your RF switch.

More info: Daskalakispiros@gmail.com

