#this is the one that your are editing and using
import cv2
import numpy as np
face_cascade = cv2.CascadeClassifier('cascades/data/haarcascade_frontalface_default.xml')


cap = cv2.VideoCapture(0)


while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5)
    for (x,y,w,h) in faces:
        print("I see you")
        roi_gray = gray[y:y+h,x:x+w]
        #img_item = "myimage.png"
#        cv2.imwrite(img_item, roi_gray)
        
        #change for diffrent viedo input reseulations 
        IH = 640
        IW = 480 
        #test if this is right by puting a blue rim
        cv2.rectangle(frame, (0, 0), (IH, IW), (255,0,0), 3)
       
       
        # might use tensorflow to keep learning
        
        
        size = "Size"
        color = (0, 255, 255)
        stroke = 1
        X_cord = x + w
        Y_cord = y + h
        Y_Text = (y - 2)
        Y_Text2 = (y + 11)
        X_Text = (x + 1)
        text = "Distance={}x{}".format(x, y, w, h)
        text2 = "Size={}x{}".format(w, h)
        cv2.rectangle(frame, (x, y), (X_cord, Y_cord), color, stroke)
        
        
        cv2.putText(frame, text, (X_Text, Y_Text),
			cv2.FONT_HERSHEY_SIMPLEX, 0.45, (color), stroke)
        cv2.putText(frame, text2, (X_Text, Y_Text2),
			cv2.FONT_HERSHEY_SIMPLEX, 0.45, (color), stroke)
    # Display the resulting frame
    cv2.imshow('faces',frame)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()