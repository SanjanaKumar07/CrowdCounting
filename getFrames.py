import cv2
import numpy as np
import requests

try:
    url = 'http://192.168.43.1:8080/shot.jpg'


    '''postUrl = 'http://127.0.0.1:5000/getIp'
    res = requests.post(postUrl,data={'hello':'hello'})
    print(res.text)
    ip_list = str(res.text).split(' ')

    for ip in ip_list:
        url = 'http://' + str(ip) + "/shot.jpg"'''


    drawing = False
    mode = True
    (ix, iy) = (-1, -1)
    rect = (0,0,0,0)
    startPoint = False
    endPoint = False
    def draw_shape(event, x, y, flags, param):
        global rect,startPoint,endPoint

        # get mouse click
        if event == cv2.EVENT_LBUTTONDOWN:
            if startPoint == True and endPoint == True:
                startPoint = False
                endPoint = False
                doneRect = rect
                rect = (0, 0, 0, 0)

            if startPoint == False:
                rect = (x, y, 0, 0)
                startPoint = True
            elif endPoint == False:
                rect = (rect[0], rect[1], x, y)
                endPoint = True

    doneRect = True
    while True:
        img_req = requests.get(url)
        img_arr = np.array(bytearray(img_req.content),dtype = np.uint8)
        capture = cv2.imdecode(img_arr, -1)
        frame = cv2.resize(capture, (640, 480))
        cv2.setMouseCallback('url image',draw_shape)
        print('startPoint: ',startPoint)
        print('endPoint: ',endPoint)
        cv2.imshow('url image',frame)
        if startPoint and endPoint:
            doneRect = False
            x1 = rect[0]
            y1 = rect[1]
            x2 = rect[2]
            y2 = rect[3]
            print('doneRect: ',rect)
            frame = frame[rect[1]:rect[3],rect[0]:rect[2]]
            cv2.imshow('completed img',frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            capture.release()
            cv2.destroyAllWindows()
            break


except:
    cv2.destroyAllWindows()
