# 18 tam giác và tia chớp
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

def identified_Circle(img):
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	blurred = cv2.blur(gray, (3, 3))
	detected_circles = cv2.HoughCircles(blurred, cv2.HOUGH_GRADIENT, 1, 10, param1=40, param2=25, minRadius=20, maxRadius=35)
	if detected_circles is not None:
		detected_circles = np.uint16(np.around(detected_circles))
		for pt in detected_circles[0, :]:
			a, b, r = pt[0], pt[1], pt[2]
			cv2.circle(img, (a, b), r, (0, 69, 255), 2)
			cv2.putText(img, "Circle", (a, b), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 69, 255), 2)

def detected_Shape(img):
	# code
	imgGrey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	_, thresholds = cv2.threshold(imgGrey, 0, 255, cv2.THRESH_BINARY)
	contours, _ = cv2.findContours(thresholds, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
	for cnt in contours:
	    approx = cv2.approxPolyDP(cnt, 0.01 * cv2.arcLength(cnt, True), True)
	    x = approx.ravel()[0]
	    y = approx.ravel()[1]
	    print(len(approx))
	    if len(approx) in [3, 4, 5, 6, 7, 8, 9, 10]:
	    	continue
	    elif len(approx) == 11:
	    	cv2.drawContours(img, [approx], 0, (0, 69, 255), 2)
	    	put_text_center(img, "Thunder", cnt)


detected_Shape(img)
identified_Circle(img)
cv2.imshow("Example", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
