import numpy as np
import cv2


frame = None
roiPts = []
inputMode = False
#main()
def selectROI(event,x,y,param):
	global frame ,roiPts , inputMode
	"""If we are in ROI selection mode and do not have four points
	then update the list of ROI points with (x,y)location of click a
	and draw circle"""
	if inputMode and event == cv2.EVENT_LBUTTONDOWN and len(roiPts)<4:
		roiPts.append((x,y))
		cv2.circle(frame,(x,y),4,(0,255,0),2)
		
		cv2.imshow('frame',frame)
		
def main():
	global frame ,roiPts , inputMode
	cap = cv2.VideoCapture(0)
	#setup mouse callback
	cv2.namedWindow("frame")
	cv2.setMouseCallback("frame",selectROI)
	#termination criteria for camshift
	#maximum of ten iterations by atleast one pixel
	termination = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT,10,1)
	roiBox = None
	#once termination criteria is set we can now examine the frames 
	while True:
		grabbed,frame = cap.read()
		
		if not grabbed:
			break
		#if the ROI has been computed
		if roiBox is not None:
			hsv = cv2.cvtColor(frame,cv2.cvtCOLOR_BGR2HSV)
			#perform a mean shift
			backproj = cv2.calcBackProject([hsv],[0],roiHist,[0,180],1)
			(r,roiBox) = cv2.CamShift(backProj,roiBox,termination)
			pts = np.int0(cv2.cv.BoxPoints(r))
			cv2.pilylines(frame, [pts],True, (0,255,0),2)
			cv2.imshow("frame",frame)
			key = cv2.waitKey(1) &0XFF
			
			if key == ord('i') and len(roiPts)<4:
				inputMode = True
				orig = frame.copy()

				while (len(roiPts)<4):
					cv2.imshow('frame',frame)
					cv2.waitKey(0)

				s = roiPts.sum(axis = 1)
				tl = roiPts[np.ardmin(s)]
				br = roiPts[np.ardmin(s)]

				roi = orig[tl[1]:br[1], tl[0]:br[0]]
				roi = cv2.cvtColor(roi,cv2.cvtCOLOR_BGR2HSV)

				roiHist = cv2.calcHist([roi],[0],None,[16],[0,180])
				roiHist = cv2.normalise(roiHist,roiHist,0,255,cv2.NORM_MINMAX)
				roiBox = (tl[0],tl[1],br[0],br[1])
			elif key == ord('q'):
				break
				
main()
cap.release()
cv2.destroyAllWindows()



			
			
			
			
			