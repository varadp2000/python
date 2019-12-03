import cv2
import datetime
cap= cv2.VideoCapture(0)

#Change Input Width and Height
cap.set(3,1920)
cap.set(4,1080)


while True:
    ret,frame=cap.read()
    if ret==True:
        frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        
        dt=str(datetime.datetime.now())
        font=cv2.FONT_HERSHEY_SIMPLEX
        frame=cv2.putText(frame,dt,(10,50),font,1,(255,255,255),1,cv2.LINE_AA)
        cv2.imshow('Output',frame)
        if(cv2.waitKey(1)& 0xFF==ord('q')):
            break
    else:
        break
        
cap.release()
cv2.destroyAllWindows()





