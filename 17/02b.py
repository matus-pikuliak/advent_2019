import numpy as np
np.set_printoptions(linewidth=100000, threshold=1000000)

from intcode import IntCode

code = [
    int(num)
    for num
    in open('input').read().split(',')
]

code[0] = 2
computer = IntCode(code).run()

input = iter(open('instructions').read())
while True:
    out = next(computer)
    if out > 1000:
        print(out)
    if out > 0:
        print(chr(out), end='')
    else:
        computer.send(ord(next(input)))
