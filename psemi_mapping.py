#######################################################
#     Spiros Daskalakis                               #
#     last Revision: 14/07/2022                       #
#     Python Version:  3.9                            #
#     Email: daskalakispiros@gmail.com                #
#######################################################

# Interface Board Mapping
LS = 0b_0010_0000
V1 = 0b_1000_0000
V2 = 0b_0000_0010
V3 = 0b_0000_0100
V4 = 0b_0001_0000
GND_RESISTOR_PIN = 0b_0100_0000
GND_PIN = 0b_0000_0001
LED_OFF = 0b_0000_1000
LED_ON = 0b_0000_0000
# control logic truth table for PE42512 and PE42412 and PE426412 RF switches
PE42X12_dict = {
    'ALL_OFF': LS | V2 | V1,
    'RFC_RF1': LS | V4 | V3 | V1,
    'RFC_RF2': LS | V3 | V1,
    'RFC_RF3': LS | V4 | V1,
    'RFC_RF4': LS | V1,
    'RFC_RF5': LS | V4 | V3 | V2,
    'RFC_RF6': LS | V3 | V2,
    'RFC_RF7': LS | V4 | V2,
    'RFC_RF8': LS | V2,
    'RFC_RF9': LS | V4 | V3,
    'RFC_RF10': LS | V3,
    'RFC_RF11': LS | V4,
    'RFC_RF12': LS,
}
# control logic truth table for PE42482 and PE42582 and PE426482 switches
PE42X82_dict = {
    'ALL_OFF': LS | V4,
    'RFC_RF1': LS | V3 | V2 | V1,
    'RFC_RF2': LS | V2 | V1,
    'RFC_RF3': LS | V3 | V1,
    'RFC_RF4': LS | V1,
    'RFC_RF5': LS | V3 | V2,
    'RFC_RF6': LS | V2,
    'RFC_RF7': LS | V3,
    'RFC_RF8': LS,
}
# control logic truth table for PE42562 and PE42462 and PE426462 switches
PE42X62_dict = {
    'ALL_OFF': LS | V2 | V1,
    'RFC_RF1': LS | V3 | V1,
    'RFC_RF2': LS | V1,
    'RFC_RF3': LS | V3 | V2,
    'RFC_RF4': LS | V2,
    'RFC_RF5': LS | V3,
    'RFC_RF6': LS,
}
