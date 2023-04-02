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
    r1o=np.zeros(slika.shape[:2])
    r2o=np.zeros(slika.shape[:2])
    slika_robov=np.zeros(slika.shape,dtype=np.uint8)
    for i in range(0,slika.shape[0]-1):
      for j in range(0,slika.shape[1]-1):
         slika_del=slika[i:i+2,j:j+2]
         r1o[i][j]=np.sum(slika_del*r1)
         r2o[i][j]=np.sum(slika_del*r2)
    slika_robov=np.sqrt(np.square(r1o)+np.square(r2o))
    slika_robov=np.uint8(slika_robov)
    return slika_robov 

def my_prewitt(slika):
    dimension= slika.shape
    r1 = np.array([[1,0, -1],[1, 0,-1], [1,0,-1]])
    r2 = np.array([[1,1,1],[0,0,0], [-1,-1,-1]])
    r1p=np.zeros(slika.shape[:2])
    r2p=np.zeros(slika.shape[:2])
    slika_robov=np.zeros(slika.shape,dtype=np.uint8)
    for i in range(0,slika.shape[0]-2):
      for j in range(0,slika.shape[1]-2):
         slika_del=slika[i:i+3,j:j+3]
         r1p[i][j]=np.sum(slika_del*r1)
         r2p[i][j]=np.sum(slika_del*r2)
    slika_robov=np.sqrt(np.square(r1p)+np.square(r2p))
    slika_robov=np.uint8(slika_robov)
    return slika_robov 

def my_sobel(slika):
   pass

def canny(slika, sp_prag, zg_prag):
    slika_robov=cv2.Canny(slika,sp_prag,zg_prag)
    return slika_robov 


   

img = cv2.imread("lenna.png",0)
#cv2.imshow("roberts algoritem",my_roberts(img))
#cv2.imshow("prewwit algoritem",my_prewitt(img))
cv2.imshow("sobel algoritem",my_sobel(img))
#cv2.imshow("canny algoritem (10,300)",canny(img,10,300))
#cv2.imshow("canny algoritem (50,150)",canny(img,50,150))
cv2.waitKey()
cv2.destroyAllWindows()