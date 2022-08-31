import cv2
import numpy as np

def draw_circle(event, x, y, flags, param):
    
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, (x, y), 100, (0, 0, 255), -1)
        
    elif event == cv2.EVENT_RBUTTONDOWN:
        cv2.circle(img, (x, y), 100, (255, 0, 255), -1)

cv2.namedWindow(winname='Test window')

cv2.setMouseCallback('Test window', draw_circle)

img = np.zeros((512,512, 3), np.int8)

while True:
    
    cv2.imshow('Test window', img)
    
    if cv2.waitKey(25) & 0xFF == 27:
        break
    
cv2.destroyAllWindows()