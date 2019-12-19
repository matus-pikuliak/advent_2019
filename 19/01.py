import numpy as np
np.set_printoptions(linewidth=100000, threshold=1000000)

from intcode import IntCode

code = [
    int(num)
    for num
    in open('input').read().split(',')
]

sum = 0
for x in range(50):
    for y in range(50):
        computer = IntCode(code).run()
        next(computer)
        computer.send(x)
        next(computer)
        computer.send(y)
        sum += next(computer)

print(sum)
