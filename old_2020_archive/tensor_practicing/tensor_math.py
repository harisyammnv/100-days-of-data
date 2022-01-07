import torch

x = torch.tensor([1, 2, 3])
y = torch.tensor([9, 8, 7])

z1 = torch.add(x, y)
print(z1)
z2 = x - y
print(z2)

z3 = torch.true_divide(x, y)
print(z3)

t = torch.zeros(3)
t.add_(x) ## inplace operations
z = x.pow(2)
print(z)

z = x > 0
print(z)

x1 = torch.rand((2, 5))
x2 = torch.rand((5, 3))
x3 = torch.mm(x1, x2)
print(x3)

m = torch.rand((5, 5))
m_exp = m.matrix_power(3)
print(m_exp)

z = x * y
print(z)

z = torch.dot(x, y)
print(z)

batch=32
n=10
m=20
p=30

tensor1 = torch.rand((batch, n, m))
tensor2 = torch.rand((batch, m, p))

out_bmm = torch.bmm(tensor1, tensor2)
print(out_bmm)


x1 = torch.rand((5, 5))
x2 = torch.rand((1, 5))

z = x1 - x2
print(z)
z = x1 ** x2
print(z)

sum_x = torch.sum(x, dim=0)
values, indices = torch.max(x, dim=0)
abs_x = torch.abs(x)
z = torch.argmax(x, dim=0)
mean_x = torch.mean(x.float(), dim=0)
y_sort, indices2 = torch.sort(y, dim=0, descending=False)

z = torch.clamp(x, min=0)
print(z)

x = torch.tensor([1, 0, 1, 1], dtype=torch.bool)
print(torch.any(x))
print(torch.all(x))