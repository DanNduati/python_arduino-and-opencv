import serial
import time

ser = serial.Serial('/dev/ttyACM0',9600)
while (ser.isOpen()):
	if (ser.read()=='1'):
		print("btn pressed")
	if(ser.read()== '0'):
		print("btn released")