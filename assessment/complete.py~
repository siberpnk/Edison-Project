#From the library, import the main class
#Note, it would need to be in the same folder or in the python PATH

#import the LCD class
from utilsComplete import I2CLCDDisplay
#import for the Gas, Dust, Loud classes
from utilsComplete import Gas, Dust, Loud
#Import time from the core python library
import time
#Import mraa for GPIO from the core python library
import mraa

#Setup thingspeak cloudplatform
#import thingspeak #If thingspeak not found please goover the thingspeak power point to install this on your edison

#channel_id  = "" # PUT CHANNEL ID HERE
#write_key   = "" # PUT YOUR WRITE KEY HERE
#thingspeak.Channel(id=channel_id,write_key=write_key)

#Create an instance of I2CLCDDisplay and call it LCDDisplay
LCDDisplay = I2CLCDDisplay()
#available functions
# LCDDisplay.LEDColor(255,255,255)         #RGB Set the background LCD color with values from 0-255 per color
# LCDDisplay.LCDPrint("Hello World!!!")    #Print text to the display
# LCDDisplay.LCDInstruction(0x80 + 0x00)   #Set the cursor to the start of the first line
# LCDDisplay.LCDInstruction(0x80 + 0x28)   #Set the cursor to the start of the second line
# LCDDisplay.LCDInstruction(0x01)	   #Clear the display

#Create an instance of TH02 and call it TH02 sensor
#TH02Sensor = TH02()
# str(TH02Sensor.getTemperature())     # String value of Temperature
# str(TH02Sensor.getHumidity())        # String value of Humidity

#Declare Digital inputs
button = mraa.Gpio(2);
dust = mraa.Gpio(3);
#(Declare button variable)
#(declare button direction)

#Declare Analog inputs
gas = mraa.Aio(0);
loud = mraa.Aio(1);
#(declare UV sensor variable and port)
#(declare Soil humidity sensor variable and port)
#(declare light sensor variable and port)

#Print your name and date 
#(Use the LCD functions to print your name)
#(Switch on the backlight)

#(wait a few seconds using the time.sleep(2) command

#Loop that runs through different sensor values 
i=0
#this variable is used to cycle through the different sensors when the button is pressed this will be increased by 1
while True:
        while(i==0):
                LCDDisplay.LCDInstruction(0x01)
                LCDDisplay.LEDColor(0,255,255)
                LCDDisplay.LCDInstruction(0x80)
                LCDDisplay.LCDPrint("Filled in by:")
                LCDDisplay.LCDInstruction(0x80 + 0x28)
                LCDDisplay.LCDPrint("Nikolai Kojevnikov")
                time.sleep(5)
                i=i+1
	#This code is used to increment i with 1
	if(button.read() == 1): #This will be true if the button is pressed
		i=i+1                 
                #Increment i with 1 to continue to the next sensor
        
        while(i==1):
                LCDDisplay.LCDInstruction(0x01)
                LCDDisplay.LEDColor(255,0,0)
                LCDDisplay.LCDInstruction(0x80)
                LCDDisplay.LCDPrint("Loudness:")
                LCDDisplay.LCDInstruction(0x80 + 0x28)
                LCDDisplay.LCDPrint(str(Loud().Ex()));
                time.sleep(1);
                if(button.read() == 1):
                    i=i+1
		#(Display the value of the UV sensor here)
        	#(Copy the code to register when the button is pressed to progress to the next sensor readout)
        while(i==2):
                LCDDisplay.LCDInstruction(0x01)
                LCDDisplay.LEDColor(0,255,0)
                LCDDisplay.LCDInstruction(0x80)
                LCDDisplay.LCDPrint("Gasiness:")
                LCDDisplay.LCDInstruction(0x80 + 0x28)
                LCDDisplay.LCDPrint(str(Gas().Ex()));
                time.sleep(1)
                if(button.read() == 1):
                    i=i+1
		#(Display the value of the Light sensor here)
		#(Copy the code to register when the button is pressed to progress to the next sensor readout)
        while(i==3):
                LCDDisplay.LCDInstruction(0x01)
                LCDDisplay.LEDColor(0,0,255)
                LCDDisplay.LCDInstruction(0x80)
                LCDDisplay.LCDPrint("Dustiness:")
                LCDDisplay.LCDInstruction(0x80 + 0x28)
                LCDDisplay.LCDPrint(str(Dust().Ex()));
                time.sleep(2)
                if(button.read() == 1):
                    i=0


