import cv2
import numpy as np
import serial
ser = serial.Serial('/dev/ttyACM0')
cap = cv2.VideoCapture(0)
while (ser.isOpen()):
	_,frame = cap.read()
	cv2.imshow('image',frame)
	k = cv2.waitKey(1)
	if (k == 27):
		break
	elif k == ord('s') & 0XFF:
		cv2.imwrite('pic.png',frame)
		break
cap.release()
cv2.destroyAllWindows()