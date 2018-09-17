import serial
import time
#seral port then baud rate
#ttyACM0hh
ser= serial.Serial('/dev/ttyACM0',9600)
#time.sleep(2)
while (ser.isOpen()):
	#write ascii character values
	ser.write('A'.encode())
	time.sleep(1)
	