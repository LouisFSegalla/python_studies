import numpy as np
import matplotlib.pyplot as plt

x_input = [0,1,2]
y_input = [1, 3 ,2]
def objective_function(x):
    return np.exp(-x)*np.sin(2*np.pi*x)

# x_input = np.linspace(0,2,10)
# y_input = objective_function(x_input)

plt.plot(x_input,y_input,'b*')

if(len(x_input) != len(y_input)):
    print('Tamanhos diferentes')
    
num_points = len(x_input)

A = np.zeros([4*(num_points-1), 4*(num_points-1)])
b = np.zeros([4*(num_points-1)])
x = np.zeros([4*(num_points-1)])


for linha in range(0,(num_points-1),1):
    for coluna in range(0,4,1):
        #S_i(x_i)
        A[2*linha][4*linha + coluna] = x_input[linha]**(3-coluna)
        #S_i+1(x_i+1)
        A[2*linha+1][4*linha + coluna] = x_input[linha+1]**(3-coluna)
        #y_i
        b[2*linha] = y_input[linha]
        #y_i+1
        b[2*linha+1] = y_input[linha + 1]



num_eq = (num_points-2)
total_eq = 2*(num_points-1) + num_eq
init_eq  = 2*(num_points-1)
for linha in range(init_eq,total_eq,1):
    #S'i(x_i) = S'i+1(x_i+1)
    A[linha][4*(num_eq - (total_eq - linha)) + 0] = 3*x_input[(num_eq - (total_eq - linha))+1]**2
    A[linha][4*(num_eq - (total_eq - linha)) + 1] = 2*x_input[(num_eq - (total_eq - linha))+1]**1
    A[linha][4*(num_eq - (total_eq - linha)) + 2] = 1
    A[linha][4*(num_eq - (total_eq - linha)) + 3] = 0
    A[linha][4*(num_eq - (total_eq - linha)) + 4] = -3*x_input[(num_eq - (total_eq - linha))+1]**2
    A[linha][4*(num_eq - (total_eq - linha)) + 5] = -2*x_input[(num_eq - (total_eq - linha))+1]**1
    A[linha][4*(num_eq - (total_eq - linha)) + 6] = -1
    A[linha][4*(num_eq - (total_eq - linha)) + 7] =  0
    #S''i(x_i) = S''i+1(x_i+1)
    A[linha+num_eq][4*(num_eq - (total_eq - linha)) + 0] = 6*x_input[(num_eq - (total_eq - linha))+1]
    A[linha+num_eq][4*(num_eq - (total_eq - linha)) + 1] = 2
    A[linha+num_eq][4*(num_eq - (total_eq - linha)) + 2] = 0
    A[linha+num_eq][4*(num_eq - (total_eq - linha)) + 3] = 0
    A[linha+num_eq][4*(num_eq - (total_eq - linha)) + 4] = -6*x_input[(num_eq - (total_eq - linha))+1]
    A[linha+num_eq][4*(num_eq - (total_eq - linha)) + 5] = -2
    A[linha+num_eq][4*(num_eq - (total_eq - linha)) + 6] =  0 
    A[linha+num_eq][4*(num_eq - (total_eq - linha)) + 7] =  0 
    

A[4*(num_points-1)-2][0] = 6*x_input[0]
A[4*(num_points-1)-2][1] = 2

A[4*(num_points-1)-1][4] = 6*x_input[num_points-1]
A[4*(num_points-1)-1][5] = 2

A_inv = np.linalg.inv(A)
b = b[:, np.newaxis]
x = np.dot(A_inv,b)

#print equation 
for i in range(0,num_points-1,1):
    print('Equation ', i, ': ',x[4*i],'x³ + ', x[4*i + 1],'x² + ',x[4*i+2],'x + ',x[4*i+3])

def printSplineRestul(coef,x_input,y_input,div):
    num_points = len(x_input)
    for i in range(0,num_points-1,1):
        x_spline = np.linspace(x_input[i],x_input[i+1],div)
        y_spline = coef[4*i]*(x_spline**3) + coef[4*i + 1]*(x_spline**2) + coef[4*i+2]*(x_spline) + coef[4*i+3]
        plt.plot(x_spline,y_spline,'b-')
        
    plt.plot(x_input,y_input,'r*')
    plt.grid()
    plt.show()
    
printSplineRestul(x,x_input,y_input,10)