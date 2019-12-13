import numpy as np
np.set_printoptions(linewidth=200)
from intcode import IntCode

code = [
    int(num)
    for num
    in open('input').read().split(',')
]
code[0] = 2

map = np.zeros((22, 37), dtype=np.int)
computer = IntCode(code).run()

for _ in range(22 * 37):
    y, x, val = [next(computer) for _ in range(3)]
    map[x, y] = val

while True:
    y = next(computer)

    if y == -999:
        # print(map)
        ball = np.where(map == 4)[1][0]
        paddle = np.where(map == 3)[1][0]
        if ball < paddle:
            computer.send(-1)
        elif ball > paddle:
            computer.send(1)
        else:
            computer.send(0)
    else:
        x, val = next(computer), next(computer)

    if y >= 0:
        map[x, y] = val

    if y == -1:
        print('Score', val)