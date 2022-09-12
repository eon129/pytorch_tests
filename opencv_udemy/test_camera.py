import cv2
import time

#capture = cv2.VideoCapture('testvideo.mp4')

def draw_rectangle(event, x, y, flags, param):
    
    global pt1, pt2, firstClick, secondClick
    
    if event == cv2.EVENT_LBUTTONDOWN:
        
        if firstClick == True and secondClick == True:
            pt1 = (0, 0)
            pt2 = (0, 0)
            firstClick = False
            secondClick = False
            
        if firstClick == False:
            pt1 = (x, y)
            firstClick = True
        elif secondClick == False:
            pt2 = (x, y)
            secondClick = True


pt1 = (0, 0)
pt2 = (0, 0)

firstClick = False
secondClick = False


cv2.namedWindow('Test')
cv2.setMouseCallback('Test', draw_rectangle)

capture = cv2.VideoCapture(0)


while capture.isOpened():
    
    ret, frame = capture.read()
    
    if ret == True:
    
        #time.sleep(1/20)
        
        if firstClick:
            cv2.circle(frame, center=pt1, radius=5, color=(0, 0, 255), thickness=-1)
            
        if firstClick and secondClick:
            cv2.rectangle(frame, pt1, pt2, (0, 0, 255), 3)
    
        cv2.imshow('Test', frame)
    
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
        
capture.release()
cv2.destroyAllWindows()