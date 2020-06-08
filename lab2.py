import numpy as np


arr = np.array([[1, 2], [-5, -2], [0, 0]])

#Найти сумму всех отрицательных элементов матрицы 
print(np.count_nonzero(arr < 0))

#Найти число нулевых элементов матрицы
print(np.count_nonzero(arr == 0))

#Переставить два столбца матрицы местами
a = np.array([[10, 20, 30, 40, 50],
       [ 6,  7,  8,  9, 10]])
permutation = [0,4,1,3,2]
perm_mat = np.zeros((len(permutation), len(permutation)))
for idx, i in enumerate(permutation):
    perm_mat[idx, i] = 1

print(a)
print(np.dot(a, perm_mat))

#Найти сумму первых двух строк матрицы. Результат вывести как массив из одной строки
print("sum")
print(np.sum(arr[0:2], axis = 1))
print(np.sum(arr[0:2]))
