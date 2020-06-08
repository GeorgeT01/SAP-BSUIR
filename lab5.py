from scipy.optimize import fsolve
import math
import numpy as np


#Найти корни полинома
z = np.roots([3,-2,5,-42,0]) 
print(z)

#Решить нелинейное уравнение
def equation(p):
    x = p
    return (np.cos(x) - 2 * np.sin(2 * x) - 0.2)

x =  fsolve(equation, (1))
print(equation((x)))



#Решить нелинейную систему
def equations(p):
    x, y = p
    return (2*x-5*y**2 +1, -1 * x**2 + y - 5)

x, y =  fsolve(equations, (1, 1))

print (equations((x, y)))