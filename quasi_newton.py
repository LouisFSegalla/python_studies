# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 13:46:52 2022

@author: luisf
"""

#Quasi-Newton Method of optization using BFGS Algorithm

import numpy as np

def function(x):
    return x[0]**2 + 0.5*x[1]**2 + 3

def dfdx(x):
    return np.array([2*x[0], x[1]])

def St(Xnew,Xold):
    return Xnew - Xold

def Yt(Xnew,Xold):
    return dfdx(Xnew) - dfdx(Xold)

def Pt(s,y):
    return 1 / (np.transpose(y)*s)

def Xnew(Xold,H):
    return Xold - np.dot(H,dfdx(Xold))

def Hnew(Hold,Xnew,Xold):
    #A*Hold*B + C
    st = St(Xnew,Xold)
    yt = Yt(Xnew,Xold)
    p  = Pt(st,yt)
    A = ((np.eye(len(Hold)) - p*np.dot(st,np.transpose(yt))))
    B = ((np.eye(len(Hold)) - p*np.dot(yt,np.transpose(st))))
    C = p*st*np.transpose(st)
    return A*Hold*B + C
    


x0 = np.array([[1],[2]])
y0 = function(x0)
print('y0 = \n', y0)
dy0 = dfdx(x0)
print('dy0 = \n', dy0)

H0 = np.eye(len(x0))
print('H0 = \n', H0)
erro  = np.array([[1000],[1000]])
count = 0

while(count < 2):
    print('Iteration ', count)
    x1 = Xnew(x0,H0)
    dy1 = dfdx(x1)
    erro = dy1
    y1 = dy1 - dy0
    H1 = Hnew(H0,x1,x0)

    x0 = x1
    print('x0 = \n', x0)
    y0 = y1
    print('y0 = \n', y0)
    H0 = H1
    print('H0 = \n', H0)
    count = count+1




