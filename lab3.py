import numpy as np
from numpy.polynomial import Polynomial as Polynomial
from numpy.linalg import linalg as linalg
from scipy.optimize import linprog
import matplotlib.pyplot as plt

#Найти все корни уравнения
p = Polynomial([2, -1, -2, 1])
print(p.roots())
#Найти решение системы уравнений
a = np.array([[2,3], [2, 1,]])
b = np.array([11, 11])
x = linalg.solve(a, b)

print(x)
#Найти решение системы уравнений и ограничения 
c = [0, 0, 0]
A = [[1, 2, -1], [-1, 1, 1], [1, 1, -2], [-2, 3, -1]]
b = [2, 1, 0, -1]

res = linprog(c, A_ub=A, b_ub=b, options={"disp": True})
print(res)


#Нарисовать график функции 

# the function
y = x**5 - 2 * x + 1

# settings
x = np.linspace(-10,10,100)
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
plt.plot(x,y, 'r')

# show the plot
plt.show()