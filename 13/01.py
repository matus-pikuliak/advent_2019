import numpy as np
np.set_printoptions(linewidth=200)
from intcode import IntCode

code = [
    int(num)
    for num
    in open('input').read().split(',')
]

map = np.zeros((22, 37), dtype=np.int)
computer = IntCode(code).run()

while True:
    try:
        y = next(computer)
        x = next(computer)
        map[x, y] = next(computer)
    except StopIteration:
        print(np.sum(map == 2))
        print(map)
        break