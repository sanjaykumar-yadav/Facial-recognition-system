import cv2
import sys

faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
video_capture = cv2.VideoCapture(0)
id = input('Enter user ID:')
i=0
while(video_capture.isOpened()):

    retval, frame = video_capture.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(35, 35)
    )

    for (x, y, w, h) in faces:
        i=i+1;
        cv2.imwrite("Database/User."+str(id)+"."+str(i)+".jpg",frame[y:y+h,x:x+w])
        cv2.rectangle(frame, (x, y), (x+w, y+h), (50, 50, 200), 2)
        cv2.waitKey(20)
    cv2.imshow('Video', frame)
    cv2.waitKey(1)
    if(i>20):
     break
video_capture.release()

    
