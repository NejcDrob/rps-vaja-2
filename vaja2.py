from cgi import test
from configparser import Interpolation
import cv2
from cv2 import meanStdDev
import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk


def my_roberts(slika):
    #vaša implementacija
    r1 = np.array([[1,0],[0,-1]])
    r2 = np.array([[0,1],[-1,0]])


    r1o = cv2.filter2D(slika,-1,r1)   
    r2o = cv2.filter2D(slika,-1,r2)

    roberts_odvoda = cv2.hconcat((r1o,r2o))

#roberts_amplituda = np.sqrt(r1o**2 + r2o**2)
    gamma = 0

    slika_robov = cv2.addWeighted(np.absolute(r1o),0.5, np.absolute(r2o),0.5,gamma)
    #cv2.imshow("Roberts Odvoda", roberts_odvoda)
   # cv2.imshow("Roberts Gradienti", (roberts_amplituda))
    return slika_robov 

def my_prewitt(slika):
    r1 = np.array([[1,0, -1],[1, 0,-1], [1,0,-1]])


    r2 = np.array([[1,1,1],[0,0,0], [-1,-1,-1]])
    p1o = cv2.filter2D(slika,-1,r1)
    p2o = cv2.filter2D(slika,-1,r2)

    prewitt_odvoda = cv2.hconcat((p1o,p2o))
    gamma = 1

    slika_robov = cv2.addWeighted(np.absolute(p1o),0.5, np.absolute(p2o),0.5,gamma)
#cv2.imshow("Prewitt Odvoda", prewitt_odvoda)
#cv2.imshow("Prewitt Gradienti", (prewitt_amplituda))
    return slika_robov 

def my_sobel(slika):
    img = cv2.imread("lenna.png",0) 

    gamma = 0
    sy = cv2.Sobel(slika,-1,0,1,3)
    sx = cv2.Sobel(slika,-1,1,0,3)

    sx = np.uint8(np.absolute(sx))
    sy = np.uint8(np.absolute(sy))

    slika_robov = cv2.addWeighted(sx,0.5, sy,0.5,gamma)
    compare = cv2.hconcat((sx,sy))
    return slika_robov 

def canny(slika, sp_prag, zg_prag):
    #vaša implementacija
    slika_robov=0
    return slika_robov 


img = cv2.imread("lenna.png",0)
cv2.imshow("roberts algoritem",my_roberts(img))
cv2.imshow("prewwit algoritem",my_prewitt(img))
cv2.imshow("sobel algoritem",my_sobel(img))
cv2.waitKey()
cv2.destroyAllWindows()