import cv2
import numpy as np
import serial
import time
print("welcome to arduino-opencv photobooth")
print("press the red button to to take a picture and the other to exit")
ser = serial.Serial('/dev/ttyACM0')
cap = cv2.VideoCapture(0)

while(ser.isOpen()):
	
	ret,frame = cap.read()
	
	cv2.imshow('cam',frame)
	#k = cv2.waitKey(1)
	k = cv2.waitKey(1) & 0XFF
	
	if (ser.read()=='1' or k==27):
		print("no photo taken!!!")
		break
	elif (ser.read()=='0' or k== ord('s') & 0XFF):
		cv2.imwrite('pic.png',frame);
		print("photo taken!!!")
		break
cap.release()
cv2.destroyAllWindows()
print("goodbye")