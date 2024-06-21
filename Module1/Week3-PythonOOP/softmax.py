import torch
import torch.nn as nn
import math


class Softmax(nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, data):
        return (math.e ** data) / sum([math.e ** x for x in data])


class softmax_stable(nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, data):
        m = max(data)
        return (math.e ** (data - m) / sum([math.e ** (x - m) for x in data]))


data = torch.Tensor([1, 2, 3])
softmax = Softmax()
output = softmax(data)
print(output)
# tensor([0.0900, 0.2447, 0.6652])

data = torch.Tensor([1, 2, 3])
softmax_stable = softmax_stable()
output = softmax_stable(data)
print(output)
# tensor([0.0900, 0.2447, 0.6652])
