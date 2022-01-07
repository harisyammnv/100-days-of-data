import torch
import numpy as np

device = "cuda" if torch.cuda.is_available() else "cpu"
tensor_1 = torch.tensor([[1, 2, 3], [4, 5, 6]], dtype=torch.float32, device=device)
print(tensor_1)

# Other common initialization methods

X = torch.empty(size=(3, 3))
print(X)
y = torch.zeros((3, 3))
print(y)

z = torch.rand((3, 3))
print(z)

a = torch.eye(5, 5)
print(a)

b = torch.linspace(start=0.1, end=1, steps=10)
print(b)

x1 = torch.empty(size=(1,5)).normal_(mean=0, std=1)
x2 = torch.empty(size=(1, 5)).uniform_(1)

print(x1)
print(x2)

x3 = torch.arange(4)
print(x3.bool())
print(x3.short())
print(x3.long())
print(x3.half())
print(x3.float())
print(x3.double())


np_array = np.zeros((5, 5))
print(np_array)
tensor_2 = torch.from_numpy(np_array)
print(tensor_2)
np_array = tensor_2.numpy()
print(np_array)