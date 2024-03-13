import cv2
import sys
import numpy as np
import math

sys.stdout.reconfigure(encoding='utf-8')

"""
STT 9: Sử dụng các hàm vẽ hình trong OpenCV, dùng ngôn ngữ Python và phần
mềm mô phỏng Pycharm hoặc tương đương để vẽ hình như sau và kèm tên của sinh viên
vào dưới chân của hình:
Mở rộng: Viết họ tên và vẽ 1 đường elip trên ảnh được mở từ camera
"""

def Write_Text_Img(img, X, Y, name, color = (0, 0, 255), title = 'Ten: '):
    text = title + name
    position = (X, Y)
    font = cv2.FONT_HERSHEY_SIMPLEX
    scale = 1
    font_size = 2
    cv2.putText(img, text, position, font, scale, color, font_size)

def four_propellers(img, goto_X, goto_Y):
    lenght = 400
    width = 350
    color = (255, 255, 255)
    thickness = 2
    # vẽ hình chữ nhật test hình stt9
    # cv2.rectangle(img, (int(goto_X - (lenght / 2)), int(goto_Y + (width / 2))), (int(goto_X + (lenght / 2)), int(goto_Y - (width / 2))), color, thickness)
    lenght_k = lenght / 100 * 60
    width_k = width / 100 * 70
    # vẽ hình tam giác đầu tên
    triangle_1 = np.array(
        [
            [goto_X, goto_Y],
            [goto_X + lenght_k - lenght, goto_Y + width / 2],
            [goto_X - lenght_k + lenght, goto_Y + width / 2]
        ],
        np.int32
    )
    cv2.polylines(img, [triangle_1], isClosed=True, color=(255, 255, 255), thickness = 2)
    # vẽ hình tam giác thứ hai
    triangle_2 = np.array(
        [
            [goto_X, goto_Y],
            [goto_X + lenght_k - lenght, goto_Y - width / 2],
            [goto_X - lenght_k + lenght, goto_Y - width / 2]
        ],
        np.int32
    )
    cv2.polylines(img, [triangle_2], isClosed=True, color=(255, 255, 255), thickness = 2)
    # vẽ hình tam giác thứ ba
    triangle_3 = np.array(
        [
            [goto_X, goto_Y],
            [goto_X + lenght / 2, goto_Y + width - width_k],
            [goto_X + lenght / 2, goto_Y - width + width_k]
        ],
        np.int32
    )
    cv2.polylines(img, [triangle_3], isClosed=True, color=(255, 255, 255), thickness = 2)
    # vẽ hình tam giác thứ tư
    triangle_4 = np.array(
        [
            [goto_X, goto_Y],
            [goto_X - lenght / 2, goto_Y + width - width_k],
            [goto_X - lenght / 2, goto_Y - width + width_k]
        ],
        np.int32
    )
    cv2.polylines(img, [triangle_4], isClosed=True, color=(255, 255, 255), thickness = 2)

def MoRong():
    cap = cv2.VideoCapture(0)
    cap.set(3, 640)
    cap.set(4, 480)
    if not cap.isOpened():
        print("Cannot open camera!!!!!!")
        exit()
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break
        frame = cv2.resize(frame, (1500,1000), fx=0, fy=0, interpolation=cv2.INTER_AREA)
        cv2.ellipse(frame, (250, 250), (100, 50), 45, 0, 360, (0, 0, 255), 2)
        name = 'Tung Hai Quang'
        Write_Text_Img(frame, 0, 750, '9', title='Nhom: ', color=(255, 255, 102))
        Write_Text_Img(frame, 0, 800, name, color=(255, 255, 102))
        cv2.imshow("Video", frame)
        k = cv2.waitKey(1) & 0xFF
        if k == 27:
            break
    cap.release()
    cv2.destroyAllWindows()

image_path = "media/kimdami.jpg"
img = cv2.imread(image_path)
img = np.zeros((640,480,3), np.uint8)
#đều chỉnh tọa độ
X = 250
Y = 250


if img is not None:
    name = 'Tung, Hai, Quang, Huy'
    Write_Text_Img(img, 0, 550, '9', title='Nhom: ')
    Write_Text_Img(img, 0, 600, name)
    four_propellers(img, X, Y)
    cv2.imshow("STT 9", img)
    cv2.waitKey(0);
    cv2.destroyAllWindows()
    print(img.shape[0], img.shape[1])
    MoRong()
else:
    print("Lỗi. Không dẫn được ảnh")
