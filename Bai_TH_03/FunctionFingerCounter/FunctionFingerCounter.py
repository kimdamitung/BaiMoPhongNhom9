import cv2
import numpy as np
import mediapipe as mp

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=True, max_num_hands=2, min_detection_confidence=0.5)
hand_videos = mp_hands.Hands(static_image_mode=False, max_num_hands=2, min_detection_confidence=0.5)
mp_drawing = mp.solutions.drawing_utils

def Detected_HandsLandmarks(img, hands, Draw=True):
	output = img.copy()
	imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
	results = hands.process(imgRGB)
	if results.multi_hand_landmarks and Draw:
		for hand_landmarks in results.multi_hand_landmarks:
			mp_drawing.draw_landmarks(output, hand_landmarks, mp_hands.HAND_CONNECTIONS, mp_drawing.DrawingSpec((255, 255, 255), 2, 2), mp_drawing.DrawingSpec((0, 255, 0), 2, 2))
	return output, results

def Counter_Fingers(img, results, Draw=True):
	height, width, _ = img.shape
	output = img.copy()
	count = {
		'RIGHT': 0,
		'LEFT': 0
	}
	finger_tips_ids = [
					mp_hands.HandLandmark.INDEX_FINGER_TIP,
					mp_hands.HandLandmark.MIDDLE_FINGER_TIP,
					mp_hands.HandLandmark.RING_FINGER_TIP,
					mp_hands.HandLandmark.PINKY_TIP
	]
	fingers_status = {
		'RIGHT_THUMB': False, 
		'RIGHT_INDEX': False, 
		'RIGHT_MIDDLE': False, 
		'RIGHT_RING': False,
        'RIGHT_PINKY': False, 
        'LEFT_THUMB': False, 
        'LEFT_INDEX': False, 
        'LEFT_MIDDLE': False,
        'LEFT_RING': False, 
        'LEFT_PINKY': False
	}
	for index, info in enumerate(results.multi_handedness):
		hand_label = info.classification[0].label
		hand_landmarks = results.multi_hand_landmarks[index]
		for idx in finger_tips_ids:
			finger_name = idx.name.split("_")[0]
			if (hand_landmarks.landmark[idx].y < hand_landmarks.landmark[idx - 2].y):
				fingers_status[hand_label.upper() + "_" + finger_name] = True
				count[hand_label.upper()] += 1
		TIP_x = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].x
		MCP_x = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP - 2].x
		if (hand_label == 'Right' and (TIP_x < MCP_x)) or (hand_label == 'Left' and (TIP_x > MCP_x)):
			fingers_status[hand_label.upper() + "_THUMB"] = True
			count[hand_label.upper()] += 1
	if Draw:
		cv2.putText(output, "Counter finger: ", (20, 30),cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,255), 2)
		cv2.putText(output, str(sum(count.values())), (width // 3 - 100, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)
	return output, fingers_status, count