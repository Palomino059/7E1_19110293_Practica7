import cv2
import numpy as np

cap = cv2.VideoCapture(0)

BlueBajo = np.array([100,100,20],np.uint8)
BlueAlto = np.array([135,255,255],np.uint8)

while True:
    ret, frame = cap.read()
    if ret == True:
        # Parte de HSV  
        frameHSV = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
        maskBlue = cv2.inRange(frameHSV,BlueBajo,BlueAlto)
        
        maskBluevis = cv2.bitwise_and(frame,frame, mask = maskBlue)

        "------ Ruido -------"
        kernel = np.ones((15,15), np.float32)/255
        smoothed = cv2.filter2D(maskBluevis, -1, kernel)

        blur = cv2.GaussianBlur(maskBluevis,(15,15),0)
        median = cv2.medianBlur(maskBluevis,15)
        bilateral = cv2.bilateralFilter(maskBluevis, 15, 75, 75)

        "------- Morfologicamente---"
        kernel2 = np.ones((5,5), np.uint8)
        erosion = cv2.erode(maskBlue, kernel2, iterations = 1)
        dilation = cv2.dilate(maskBlue, kernel2, iterations = 1)

        opening = cv2.morphologyEx(maskBlue, cv2.MORPH_OPEN, kernel2)
        closing = cv2.morphologyEx(maskBlue, cv2.MORPH_CLOSE, kernel2)
        
         
    
        "------- Azul --------"
        cv2.imshow('maskBluevis',maskBluevis)
        cv2.imshow('frame',frame)
        cv2.imshow('maskBlue',maskBlue)
        #cv2.imshow('smoothed',smoothed)
        #cv2.imshow('blur',blur)
        #cv2.imshow('median',median)
        #cv2.imshow('bilateral',bilateral)

        cv2.imshow('erosion',erosion)
        cv2.imshow('dilation',dilation)
        cv2.imshow('opening', opening)
        cv2.imshow('closing', closing)

         
        if cv2.waitKey(1) & 0xFF == ord('a'):
            break

cap.release()
cv2.destroyAllWindows() 

      

