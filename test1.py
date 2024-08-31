print('1')
import cv2
from darkflow.net.build import TFNet
print('2')
import numpy as np
import time
import requests
import json
options = {
    'model': 'cfg/yolo.cfg',
    'load': 'bin/yolov2.weights',
    'threshold': 0.2,
    'gpu': 1.0
}
print('abc')
try:
    print('inside try')
    tfnet = TFNet(options)
    capture = cv2.VideoCapture('sample.mp4')
    capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    while True:
        print('while ke andar')
        stime = time.time()

        ret, frame = capture.read()

        results1 = tfnet.return_predict(frame)
        for color1, result1 in zip(colors, results1):
            print('inside for of video cam')
            tl = (result1['topleft']['x'], result1['topleft']['y'])
            br = (result1['bottomright']['x'], result1['bottomright']['y'])
            label = result1['label']
            confidence = result1['confidence']
            text = '{}: {:.0f}%'.format(label, confidence * 100)
            frame = cv2.rectangle(frame, tl, br, color1, 5)
            frame = cv2.putText(
                frame, text, tl, cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 2)
        print('FPS {:.1f}'.format(1 / (time.time() - stime)))
        results = tfnet.return_predict(capture0)
        for color, result in zip(colors, results):
            tl = (result['topleft']['x'], result['topleft']['y'])
            br = (result['bottomright']['x'], result['bottomright']['y'])
            label = result['label']
            confidence = result['confidence']
            text = '{}: {:.0f}%'.format(label, confidence * 100)
            capture0 = cv2.rectangle(capture0, tl, br, color, 5)
            capture0 = cv2.putText(
                capture0, text, tl, cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 2)
        print('FPS {:.1f}'.format(1 / (time.time() - stime)))

        cv2.imshow(windowName1, capture0)
        cv2.imshow(windowName2, frame)


        if cv2.waitKey(1) & 0xFF == ord('q'):
            capture.release()
            cv2.destroyAllWindows()
            break

except:
    cv2.destroyAllWindows()
