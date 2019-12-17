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
checksum = 0
for x, y in zip(*np.where(map == 35)):
    try:
        if map[x-1, y] == map[x+1, y] == map[x, y-1] == map[x, y+1] == 35:
            checksum += x*y
    except:
        pass

print(checksum)


for line in map:
    for char in line:
        print(f'{chr(char)} ' if char != 46 else '  ', end='')
    print()