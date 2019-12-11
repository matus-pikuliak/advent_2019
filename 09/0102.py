import itertools

from intcode import IntCode

code = [
    int(num)
    for num
    in open('input').read().split(',')
]

computer = IntCode(code).run()
next(computer)
computer.send(1)
for res in computer:
    print(res)


computer = IntCode(code).run()
next(computer)
computer.send(2)
for res in computer:
    print(res)

