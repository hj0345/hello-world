import cv2
capture = cv2.VideoCapture("dataset/Dry+Ice.mp4")
while True:
    if(capture.get(cv2.CAP_PROP_POS_FRAMES) == capture.get(cv2.CAP_PROP_FRAME_COUNT)):
        capture.open("dataset/Dry+Ice.mp4")

    o_height = 480
    o_width = 640
    b_color = (0, 255, 0)
    b_x1y1 = (100, 100)
    b_x2y2 = (300, 300)

    a=1
    ret, frame = capture.read()
    frame = cv2.resize(frame, dsize=(o_width, o_height), interpolation=cv2.INTER_AREA)
    cv2.rectangle(frame, (100, 100), (300, 300), b_color, 3)
    cv2.imshow("VideoFrame", frame)

    if cv2.waitKey(33) > 0: break

capture.release()
cv2.destroyAllWindows()