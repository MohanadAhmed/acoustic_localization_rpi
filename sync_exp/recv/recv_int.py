#####################################################
# Reema Alnafisi
# Synchronization Test Experiment
# 13/06/2022
#####################################################

import RPi.GPIO as GPIO
from lib_nrf24 import NRF24
import time
import spidev
import warnings
warnings.filterwarnings("ignore")

GPIO.setmode(GPIO.BCM)

#array of bytes for addresses
pipes = [[0xe7, 0x1c, 0xe3],[0xe7, 0x1c, 0xe3]]


radio = NRF24(GPIO, spidev.SpiDev())        #create instance of radio
radio.begin(0, 17)                          #CE0 connected to GPIO 17
radio.setPayloadSize(16)                    #payload size set to 16 bytes
radio.setChannel(100)                       #connected on channel 100

radio.setDataRate(NRF24.BR_250KBPS)         #the higher the datarate, the faster the transmission speed (but it is risky for long distance communication)
radio.setPALevel(NRF24.PA_MIN)              #Power Amplification level to minimum
radio.setAutoAck(False)
radio.openReadingPipe(1, pipes[1])          #reading pipe1
radio.printDetails()


v=radio.read_register(0x00)
v2= v|(0b00110000)
radio.write_register(0x00, v2)
msg_received= False

def xfunc(channel):
    #GPIO.remove_event_detect(24)
    GPIO.output(21,1)
    msg_received = True

GPIO.setup(21, GPIO.OUT)
GPIO.setup(24, GPIO.IN)
GPIO.output(21,0)
GPIO.add_event_detect(24, GPIO.FALLING, callback=xfunc)

v2=radio.read_register(0x00)
print(bin(v2))

while True:
    #time.sleep(0.001)
    if radio.available(0):
        receivedMessage = []
        radio.read(receivedMessage, 16)
        print("Received: {}".format(receivedMessage))
        #radio.write_register(radio.STATUS, 0b01000111)
        #v3=radio.read_register(0x07)
        #v4= v3|(0b01000000)
        #radio.write_register(0x07, v4)
        GPIO.output(21,0)
        msg_received = False
