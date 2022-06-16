import RPi.GPIO as GPIO
from lib_nrf24 import NRF24
import time, datetime
import spidev
import warnings
warnings.filterwarnings("ignore")

GPIO.setmode(GPIO.BCM)

pipes = [[0xe7, 0x1c, 0xe3],[0xe7, 0x1c, 0xe3]]


radio = NRF24(GPIO, spidev.SpiDev())  #create instance of radio
radio.begin(0, 17)                    #CE0 connected to GPIO 17
radio.setPayloadSize(16)              #payload size set to 16 bytes
radio.setChannel(100)                 #connected on channel 100

radio.setDataRate(NRF24.BR_250KBPS)   #the higher the datarate, the faster the transmission speed (but it is risky for long distance communication)
radio.setPALevel(NRF24.PA_MIN)        #Power Amplification level to minimum
radio.setAutoAck(False)

radio.openWritingPipe(pipes[1])       #write to pipe
radio.ce(NRF24.HIGH)                  #since the CE0 pin is active high
radio.printDetails()                
GPIO.setup(21, GPIO.OUT)

for x in range(101):
    timing = str(time.time())[0:14]
    data=[]
    data.append(timing)               #time
    data.append(str(x))               #iteration
    print(data)
    GPIO.output(21, 1)
    radio.write(''.join(data))
    GPIO.output(21, 0)
    print("We sent {}".format(timing))
    time.sleep(0.5)                  #delay of 0.01 second
    