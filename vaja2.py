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
    #vaša implementacija
    slika_robov=0
    return slika_robov 

def my_sobel(slika):
    #vaša implementacija
    slika_robov=0
    return slika_robov 

def canny(slika, sp_prag, zg_prag):
    #vaša implementacija
    slika_robov=0
    return slika_robov 


img = cv2.imread("lenna.png",0)
cv2.imshow("roberts algoritem",my_roberts(img))
cv2.waitKey()
cv2.destroyAllWindows()