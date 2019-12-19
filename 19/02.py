import numpy as np
np.set_printoptions(linewidth=100000, threshold=1000000)

from intcode import IntCode

code = [
    int(num)
    for num
    in open('input').read().split(',')
]


def output(x, y):
    computer = IntCode(code).run()
    next(computer)
    computer.send(x)
    next(computer)
    computer.send(y)
    return next(computer)


def get_ends(x):

    y = 0
    while True:
        y += 100
        if output(x, y):
            y -= 100
            break
        if y > x:
            raise AttributeError

    flag = True
    while True:
        y += 1
        if flag and output(x, y):
            start = y
            flag = False
        if not flag and not output(x, y):
            return start, y-1

# range found via manual binary search between 1000 - 10000

for x in range(1400, 1500):
    if get_ends(x)[0] == get_ends(x - 99)[1] - 99:
        print((x - 99) * 10000 + get_ends(x)[0])
        break