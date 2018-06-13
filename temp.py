from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

__version__ = '1.0.0'
__author__ = 'Alfredo Mercado'

import cv2

bernie = cv2.imread('../assets/bernie.jpg', cv2.IMREAD_COLOR)

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    cv2.imshow('webcam', frame)
    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()