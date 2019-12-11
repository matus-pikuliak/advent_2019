import numpy as np
from intcode import IntCode

code = [
    int(num)
    for num
    in open('input').read().split(',')
]

map = np.zeros((1000, 1000))
x, y = 500, 500
dx, dy = -1, 0
visited = set()

computer = IntCode(code).run()
while True:
    try:
        visited.add((x, y))
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

print(len(visited))