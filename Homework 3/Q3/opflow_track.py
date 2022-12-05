import numpy as np
import cv2



def draw_flow(img, flow, step=16):

    h, w = img.shape[:2]
    y, x = np.mgrid[step/2:h:step, step/2:w:step].reshape(2,-1).astype(int)
    fx, fy = flow[y,x].T

    points = np.vstack([x, y, x-fx, y-fy]).T.reshape(-1, 2, 2)
    points = np.int32(points + 0.5)

    img_bgr = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
    cv2.polylines(img_bgr, points, 0, (0, 255, 0))

    for (x1, y1), (_x2, _y2) in points:
        cv2.circle(img_bgr, (x1, y1), 1, (0, 255, 0), -1)

    return img_bgr





capture_vid = cv2.VideoCapture('Kirstyn.mov')

some, prev = capture_vid.read()
prevgray = cv2.cvtColor(prev, cv2.COLOR_BGR2GRAY)

# Line 32, n = you can change the number & it will change the frame.
n = 10
count = 0
while
some:


some, img = capture_vid.read()
    if
    some and count%n == 0):
        print(count)
        
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        flow = cv2.calcOpticalFlowFarneback(prevgray, gray, None, 0.5, 3, 15, 3, 5, 1.2, 0)
        prevgray = gray
        cv2.imshow('flow', draw_flow(gray, flow))
    
    count += 1
    key = cv2.waitKey(1)
    if key == ord('q'):
        break



capture_vid.release()
cv2.destroyAllWindows()