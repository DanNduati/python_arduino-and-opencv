import numpy as np
import cv2
import serial

ser =serial.Serial('/dev/ttyACM0',9600)
detector= cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(1)

while(ser.isOpen()):
	_,frame  = cap.read()
	gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
	faces = detector.detectMultiScale(gray,1.3,5)
	#check whether the tuple containing faces detected has values
	if(len(faces)>0):
		ser.write('A'.encode())
		print("face detected at: ",faces)
	for(x,y,w,h) in faces:
		cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)
	cv2.imshow('img',frame)
	k = cv2.waitKey(1)
	if k == 27:
		break
cap.release()
cv2.destroyAllWindows()
