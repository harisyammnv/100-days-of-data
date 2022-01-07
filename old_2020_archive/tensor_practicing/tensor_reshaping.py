import torch

x = torch.arange(9)

x_re = x.view(3, 3) # for contiguous tensors
x_re = x.reshape(3, 3) # use this to be safe
print(x_re)

y = x_re.t()
print(y)

x1 = torch.rand((2, 5))
x2 = torch.rand((2, 5))

print(torch.cat((x1, x2), dim=0).shape)
print(torch.cat((x1, x2), dim=1).shape)

z = x_re.view(-1) # flatten
print(z)

batch = 64
x = torch.rand((batch, 2, 5))
z = x.view(batch, -1)

print(z.shape)

z = x.permute(0, 2, 1) # transpose for multiple dimensions
print(z.shape)

x = torch.arange(10)
print(x.unsqueeze(0).shape)
print(x.unsqueeze(1).shape)

print(x.unsqueeze(0).unsqueeze(1).shape)