import serial  
import time  

locations=['/dev/ttyUSB0','/dev/ttyUSB1','/dev/ttyUSB2','/dev/ttyUSB3',  
'/dev/ttyS0','/dev/ttyS1','/dev/ttyS2','/dev/ttyS3']  
  
for device in locations:
    try:  
        ser = serial.Serial(device, 9600)   
    except:  
        print "Failed to connect to", device

ser.write(chr(255))
ser.write(chr(3))
ser.write(chr(150))

#time.sleep()

#ser.write(chr(255))
#ser.write(chr(4))
#ser.write(chr(0))

#time.sleep(2)

#ser.write(chr(255))
#ser.write(chr(7))
#ser.write(chr(176))
time.sleep(3)
ser.write(chr(255))
ser.write(chr(11))
ser.write(chr(25))
#time.sleep(1)

#ser.write(chr(255))
#ser.write(chr(7))
#ser.write(chr(254))

