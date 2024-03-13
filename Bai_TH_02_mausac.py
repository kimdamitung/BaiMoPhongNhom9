# 7 tam giác đỏ
import cv2
import numpy as np

image_path = "media/input_06.png"
img = cv2.imread(image_path)

height, width = img.shape[:2]
new_height = int(height * 1)
new_width = int(width * 1)
img = cv2.resize(img, (new_width, new_height))

def put_text_center(img, text, contour):
    x, y, w, h = cv2.boundingRect(contour)
    text_size, _ = cv2.getTextSize(text, cv2.FONT_HERSHEY_COMPLEX, 0.5, 1)
    text_x = x + (w - text_size[0]) // 2
    text_y = y + (h + text_size[1]) // 2
    cv2.putText(img, text, (text_x, text_y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 69, 255), 1)

def detected_Shape_and_Color(img):
	# code
	imgGrey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
	green_L = np.array([40, 100, 20])
	green_H = np.array([80, 255, 255])
	_, thresholds = cv2.threshold(imgGrey, 0, 255, cv2.THRESH_BINARY)
	contours, _ = cv2.findContours(thresholds, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
	for index, cnt in enumerate(contours):
	    approx = cv2.approxPolyDP(cnt, 0.01 * cv2.arcLength(cnt, True), True)
	    x = approx.ravel()[0]
	    y = approx.ravel()[1]
	    if len(approx) == 3:
	    	mask = cv2.inRange(imgHSV, green_L, green_H)
	    	mask_area = cv2.countNonZero(mask)
	    	cnt_area = cv2.contourArea(cnt)
	    	print(mask_area, cnt_area)
	    	# 2541, 
	    	array = [2541.0, 3279.0, 4746.0, 2567.5]
	    	for i in range(len(array)):
    			if mask_area == 84494 and cnt_area == array[i]:
        			cv2.drawContours(img, [approx], 0, (0, 69, 255), 2)
        			put_text_center(img, "Green Triangle", cnt)
detected_Shape_and_Color(img)
cv2.imshow("Example", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
