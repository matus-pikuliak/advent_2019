import numpy as np

image = np.array([
    int(char)
    for char
    in open('input').read()
]).reshape((-1, 6, 25))

min_zeros = 150
for layer in image:
    zeros = np.sum(layer == 0)
    if zeros < min_zeros:
        min_zeros = zeros
        print(zeros, np.sum(layer == 1) * np.sum(layer == 2))

