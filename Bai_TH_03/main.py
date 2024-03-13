import cv2
import numpy as np
import mediapipe as mp
from FunctionFingerCounter.FunctionFingerCounter import Detected_HandsLandmarks, Counter_Fingers, hand_videos

# mp_hands = mp.solutions.hands
# hands = mp_hands.Hands(static_image_mode=True, max_num_hands=2, min_detection_confidence=0.5)
# hand_videos = mp_hands.Hands(static_image_mode=False, max_num_hands=2, min_detection_confidence=0.5)
# mp_drawing = mp.solutions.drawing_utils

camera_video = cv2.VideoCapture(0)
camera_video.set(3, 1980)
camera_video.set(4, 960)
# cv2.namedWindow('Duy Tung Counter Fingers', cv2.WINDOW_NORMAL)
fingers_statuses = None
while camera_video.isOpened():
	ok, frame = camera_video.read()
	if not ok:
		continue
	frame = cv2.flip(frame, 1)
	frame, results = Detected_HandsLandmarks(frame, hand_videos)
	if results.multi_hand_landmarks:
		frame, fingers_statuses, count = Counter_Fingers(frame, results)
	cv2.imshow("Fingers Counter", frame)
	k = cv2.waitKey(1) & 0xFF
	if(k == 27):
		break
camera_video.release()
cv2.destroyAllWindows()