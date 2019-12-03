import cv2
import numpy as np
import pandas as pd

cap=cv2.VideoCapture(0);
fourcc= cv2.VideoWriter_fourcc(*'XVID')
out=cv2.VideoWriter('output.mp4',fourcc,20.0,(640,480))

while (True):
    ret,frame = cap.read()
    
    if ret== True:
        grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('frame', grey)
        out.write(frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
out.release()
cv2.destroyAllWindows()




