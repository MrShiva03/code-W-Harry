import numpy as np
import  random
# num = [random.randint(1,100) for _ in range(15)]
# print(num)

# arr = np.arange(1,10)
# num = np.mean(arr)
# rum = np.min(arr)
# print(rum)

# arr = [random.randint(1,100) for _ in range(10)]
# num = [0 if x > 50 else x for x in arr]
# sorted_num = np.sort(num)
# print(sorted_num)

arr = np.array([45, 82, 67, 90, 23, 88])
indices = np.where(arr>80)
print(indices)

