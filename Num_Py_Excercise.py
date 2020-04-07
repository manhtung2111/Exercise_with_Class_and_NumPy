import numpy as np
a = np.arange(15).reshape(3,5) # mang 2 chieu
b = np.arange(5) # mang 1 chieu
c = np.arange(24).reshape(2, 3, 4)  # mang 3 chieu
print(a)
print('')
print(b)
print('')
print(c)
print('')
print(a.sum(axis = 0)) # tong cua cac cot
print('')
print(a.min(axis = 0)) # gia tri min cua moi cot
print('')
print(a.min(axis = 1)) # gia tri min cua moi hang
print('')
for row in a:
    print(row)
print('')
for element in a.flat:
    print(element)


