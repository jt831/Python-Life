import torch
import numpy as np
import time

'''x = torch.tensor([5.5, 3], dtype=torch.int32)
y = torch.tensor([5.5, 4], dtype=torch.int32)
id_before = id(y)
y = y+x
a = np.ones(5)
b = torch.from_numpy(a)
c = torch.tensor(a)
print(c)
b += 1
print(a)
print(id(y) == id_before)'''

A = np.zeros((4, 1))
print(A.shape)
