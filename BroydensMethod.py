# -*- coding: utf-8 -*-
"""
Created on Sat Mar  5 12:57:13 2022

@author: luisf
"""

import numpy as np

# def function(x):
#     return  np.array([x[0] + 2*x[1] - 2, x[0]**2 + 4*x[1]**2 - 4])

def function(x):
    return  np.array([x[0] + x[1] + x[2] - 3, x[0]**2 + x[1]**2 + x[2]**2 - 5, np.exp(x[0]) + x[0]*x[1] - x[0]*x[2] - 1])

# def function(x):
#     return np.array([x[0]  + 0.5 * (x[0] - x[1])**3 - 1.0, 0.5 * (x[1] - x[0])**3 + x[1]])

def Y(Xold,Xnew):
    return function(Xnew) - function(Xold)

def s(Xold,Xnew):
    return Xnew - Xold


def A(Aold,Xold,Xnew):
    sVal = s(Xold,Xnew)
    yVal = Y(Xold,Xnew)
    
    p = ((sVal - (Aold.dot(yVal))).dot(sVal.T.dot(Aold))) / ((sVal.T.dot(Aold)).dot(yVal))
    Anew = Aold + p
    return Anew


X0 = np.array([[0],[0],[0]])
A0 = np.eye(X0.size)
Y0 = function(X0)

it    = 20
count = 0

while(count < it):
    print('Iteration ', count)
    Xnew = X0 - A0.dot(Y0)
    A0 = A(A0,X0,Xnew)
    Y0 = function(Xnew)
    X0 = Xnew
    count += 1
    
print('x0    = \n', X0)
print('------------------------------------------')
print('f(x0) = \n', function(X0))
print('------------------------------------------')
print('A0 = \n', A0)
print('------------------------------------------')
print('Erro = \n', Y0)