import cv2
import time



def detect_face(img):
    face_img = img.copy()
    face_rects = fade_cascade.detectMultiScale(face_img)
    
    for (x, y, w, h) in face_rects:
        cv2.rectangle(face_img, (x, y), (x+w, y+h), (255, 0, 0), 10)
        
    return face_img


cv2.namedWindow('Face detection traditional')

capture = cv2.VideoCapture(0)
fade_cascade = cv2.CascadeClassifier('../../opencv_udemy/DATA/haarcascades/haarcascade_frontalface_default.xml')

while capture.isOpened():
    
    ret, frame = capture.read()
    
    if ret == True:
    
        #time.sleep(1/20)
        
        img_to_show = detect_face(frame)
    
        cv2.imshow('Face detection traditional', img_to_show)
    
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
        
capture.release()
cv2.destroyAllWindows()