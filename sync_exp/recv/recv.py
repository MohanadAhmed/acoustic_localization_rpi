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
radio.setPALevel(NRF24.PA_ERROR)              #Power Amplification level to minimum
radio.setAutoAck(False)
radio.openReadingPipe(1, pipes[1])          #reading pipe1
radio.printDetails()
radio.ce(NRF24.HIGH)

radio.startListening()

#c= 299792458                               #speed of light
delay = []
while True:
    while not radio.available(0):          #check if radio is available
       time.sleep(0.001)

    receivedMessage = []
    radio.read(receivedMessage, 16)

    print("Received: {}".format(receivedMessage))

    string = ""
    for n in receivedMessage: 
        #Decode into standard unicode set
        if (n>=32 and n<=126):
            string += chr(n)
            
    curtiming = str(time.time())[0:14]                         #time the signal is received 
    print("Recieved time: ", curtiming)
    print("Transmitted time: ", string[0:14])                  #time the signal is transmitted
    print("Iteration: ", string[14:])
    difference = 1000*(float(curtiming)-float(string[0:14]))   #difference = time received-time transmitted
    #ToF = difference/c                                         #ToF=difference/c 
    print(difference)                                                 #print the time of flight
    delay.append(difference)                                          #append the time of flight to the delay array

    print("Number of received packets:", len(delay))           #print number of received packets
    print("Maximum Delay:", max(delay))                        #print the maximum delay