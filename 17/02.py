import numpy as np
np.set_printoptions(linewidth=100000, threshold=1000000)

from intcode import IntCode

code = [
    int(num)
    for num
    in open('input').read().split(',')
]

computer = IntCode(code).run()

signals =[signal for signal in computer]
map = np.array(signals[:-1]).reshape(41, -1)[:, :-1]

pos = np.array([26, 40])
dir = np.array([-1, 0])


def right(dir):
    return np.array([dir[1], -dir[0]])


def left(dir):
    return -right(dir)


def check_map(pos):
    if any(pos < 0):
        return -1
    try:
        return map[tuple(pos)]
    except:
        return -1


while True:
    steps = 0

    while check_map(pos + dir) == 35:
        steps += 1
        pos += dir

    print(steps, end=' ')
    if check_map(pos + right(dir)) == 35:
        print('R', end=' ')
        dir = right(dir)

    elif check_map(pos + left(dir)) == 35:
        print('L', end=' ')
        dir = left(dir)

    else:
        break