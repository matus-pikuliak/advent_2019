import numpy as np
np.set_printoptions(linewidth=100000, threshold=1000000)

from intcode import IntCode

code = [
    int(num)
    for num
    in open('input').read().split(',')
]

computer = IntCode(code).run()

map = np.zeros((100, 100), dtype=np.int) - 1
origin = np.array([50, 50])
map[tuple(origin)] = 1

dirs = {
    1: np.array([-1, 0]),
    2: np.array([1, 0]),
    3: np.array([0, -1]),
    4: np.array([0, 1]),
}

return_dir = {
    1: 2,
    2: 1,
    3: 4,
    4: 3
}


def explore(current_position, direction):

    new_pos = current_position + dirs[direction]
    if map[tuple(new_pos)] != -1:
        return

    next(computer)
    computer.send(direction)
    reply = next(computer)

    map[tuple(new_pos)] = reply

    if reply == 0:
        return

    for i in range(4):
        explore(new_pos, i + 1)

    next(computer)
    computer.send(return_dir[direction])
    next(computer)


for i in range(4):
    explore(origin, i+1)


for i in range(2, 1000):
    for x, y in zip(*np.where(map == i)):
        pos = np.array([x, y])
        for dir in dirs.values():
            new_pos = pos + dir
            if map[tuple(new_pos)] == 1:
                map[tuple(new_pos)] = i + 1
        print('Part 2: ', i - 2)
print('Part 1:', map[tuple(origin)] - 2)
