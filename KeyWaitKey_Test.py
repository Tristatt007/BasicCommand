# -*- coding: utf-8 -*-
"""
Created on Sat Jun  9 14:51:36 2018

@author: Cheng
"""

import cv2 
def test(): 
    
    lena = cv2.imread('C:\\Users\\Cheng\\Desktop\\IMG_5716.JPG') 
    while True: 
        cv2.imshow('image', lena) 
        while (cv2.waitKey(0) & 0xFF != ord('q') ): #waitKey如果参数为0，表示无限期的等待键盘输入
            pass 
            cv2.destroyAllWindows() 
#exit()
if __name__ == '__main__': 
        test() 
        a = 2

