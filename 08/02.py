import numpy as np

image = np.array([
    int(char)
    for char
    in open('input').read()
]).reshape((-1, 6, 25))

for row in range(6):
    for col in range(25):
        for layer in range(100):
            if image[layer, row, col] < 2:
                print('X' if image[layer, row, col] else ' ', end='')
                break
    print()
