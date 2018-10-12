# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 13:09:53 2018

@author: Sasan Raeissian sasanrz@gmail.com

"""
def solution(A):
   N=len(A)
   if sum(A)==N*(N+1)/2 :
       return 1
   else:
       return 0