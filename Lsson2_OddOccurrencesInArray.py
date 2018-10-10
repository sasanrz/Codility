# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 13:09:53 2018

@author: Sasan Raeissian sasanrz@gmail.com

"""
import numpy as np
import pandas as pd
A= [9, 3, 9, 3, 9, 7, 9]

def solution(A):
    stat=1
    while(stat==1):
        s=A[0]
        if A.count(s)!=1:
            A.remove(s)
            A.remove(s)
        else:
            print(s)
            stat=0
            
solution(A)