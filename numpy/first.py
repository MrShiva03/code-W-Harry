import numpy as np
import random
# a= int(input("enter first number: "))
# b= int(input("enter second number:"))
# sum= a-b
# print("sum of numbers: ")

# str = input("enter a number")
# print(str.endswith("r"))

# arr = np.arange(1,11)
# print(5*arr)

# matrix = np.arange(1,13).reshape(3,4)
# print(matrix)

# matrix = np.arange(1,10).reshape(3,3)
# transpose_matrix = matrix.T
# print(matrix.T)

# arr = np.arange(1,11)
# mean_val = np.mean(arr)
# print(mean_val)

# arr = np.arange(1,11)
# sum_val = np.sum(arr)
# print(sum_val)

# arr = np.arange(1,11)
# max_val = np.max(arr)
# print(max_val)

# arr1 = np.arange(1,11)
# arr2 = np.arange(9,21)
# print(arr1,arr2)

# arr1 = np.arange(1,11)
# arr2 = np.arange(10,20)
# sum_value = arr1 + arr2
# print(sum_value)

# arr1 = np.arange(1,10)
# arr2 = np.arange(11,21)
# mulpy_value = 2*arr1
# print(mulpy_value)

# num = [random.randint(1,100) for num in range(13)]
# # sorted_num = sorted(num)
# num.sort() 
# print(num)

num = [random.randint(1,100) for _ in range(10)]
num = [100 if x > 50 else x for x in num]
print(num)
even_indices = [i for i, x in enumerate(num) if x%2 == 0]
print("Indices of even values:", even_indices)


