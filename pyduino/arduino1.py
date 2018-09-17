"""Read Serial data from the arduino"""
import serial
import time
#seral port then baud rate
#ttyACM0hh
ser= serial.Serial('/dev/ttyACM0',9600)
#time.sleep(2)
while (ser.isOpen()):
	"""do not assign the ser.read() method to a variable it doesnt work
	also ser.readline() doesnt work"""
	if(ser.read()=='5'):
		print ("Receiving data from arduino")