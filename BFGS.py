# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 13:46:52 2022

@author: luisf
"""

#Quasi-Newton Method of optization using BFGS Algorithm

import numpy as np

def function(x):
    # return x[0]**2 + 0.5*x[1]**2 + 3
    return  x[0]**2 + x[1]**2 - 4
def dfdx(x):
    # return np.array([2*x[0], x[1]])
    return np.array([2*x[0], 2*x[1]])

def St(Xnew,Xold):
    return Xnew - Xold

def Yt(Xnew,Xold):
    return dfdx(Xnew) - dfdx(Xold)

def Pt(s,y):
    return 1 / (y.T.dot(s) + 1e-5)

def Xnew(Xold,H):
    return Xold - np.dot(H,dfdx(Xold))

def Hnew(Hold,Xnew,Xold):
    #A*Hold*B + C
    st = St(Xnew,Xold)
    yt = Yt(Xnew,Xold)
    p  = Pt(st,yt)
    A = ((np.eye(len(Hold)) - p*st.dot(yt.T)))
    B = ((np.eye(len(Hold)) - p*yt.dot(st.T)))
    C = p*st.dot(st.T)
    return A.dot(Hold.dot(B)) + C#A*Hold + C#
    


x0 = np.array([[1],[2]])
y0 = function(x0)
print('y0 = \n', y0)
dy0 = dfdx(x0)
print('dy0 = \n', dy0)

H0 = np.eye(len(x0))
print('H0 = \n', H0)
erro  = np.array([[1000],[1000]])
count = 5

for i in range(0,count,1):
    print('Iteration ', i)
    x1 = Xnew(x0,H0)
    dy1 = dfdx(x1)
    erro = dy1
        
    y1 = dy1 - dy0
    H1 = Hnew(H0,x1,x0)

    x0 = x1
    y0 = y1
    H0 = H1


print('x0    = \n', x0)
print('------------------------------------------')
print('f(x0) =', function(x0))
print('------------------------------------------')
print('H0 = \n', H0)
print('------------------------------------------')
print('Erro = \n', erro)
