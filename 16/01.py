import numpy as np
np.set_printoptions(linewidth=100000, threshold=1000000)

signal = [int(char) for line in open('input') for char in line]


def pattern(digit):

    bases = [0, 1, 0, -1]
    first_flag = False

    while True:
        for base in bases:
            for _ in range(digit):
                if first_flag:
                    yield base
                else:
                    first_flag = True


def step(signal):
    return [
        abs(sum(
            s * p
            for s, p
            in zip(signal, pattern(i + 1))
        )) % 10
        for i
        in range(len(signal))
    ]


for _ in range(100):
    signal = step(signal)

for i in range(8):
    print(signal[i], end='')

