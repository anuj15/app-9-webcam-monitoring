import time

import cv2

import send_mail

video = cv2.VideoCapture(0)
time.sleep(5)
first_frame = None

while True:
    check, frame = video.read()
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray_frame_gau = cv2.GaussianBlur(gray_frame, (1, 1), 0)

    if first_frame is None:
        first_frame = gray_frame_gau

    delta_frame = cv2.absdiff(first_frame, gray_frame_gau)
    thresh_frame = cv2.threshold(delta_frame, 100, 255, cv2.THRESH_BINARY)[1]
    dil_frame = cv2.dilate(thresh_frame, None, iterations=2)
    contours, check = cv2.findContours(dil_frame, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for contour in contours:
        if cv2.contourArea(contour) < 10000:
            continue
        x, y, w, h = cv2.boundingRect(contour)
        rec = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)
        if rec.any():
            send_mail.print_send_mail()
    cv2.imshow('video 2', frame)

    key = cv2.waitKey(delay=1)
    if key == ord('q'):
        break

video.release()
