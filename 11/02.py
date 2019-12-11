import numpy as np
from intcode import IntCode

code = [
    int(num)
    for num
    in open('input').read().split(',')
]

map = np.zeros((100, 100))
x, y = 50, 50
map[x, y] = 1
dx, dy = -1, 0

computer = IntCode(code).run()
while True:
    try:
        next(computer)
        computer.send(map[x, y])
        map[x, y] = next(computer)

        if dx == 0:
            dx, dy = -dy, 0
        else:
            dx, dy = 0, dx
        if next(computer):
            dx, dy = -dx, -dy

        x += dx
        y += dy

    except StopIteration:
        break

for l in map == 1:
    for c in l:
        print('X' if c else ' ', end='')
    print()
