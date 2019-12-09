import itertools

from intcode import IntCode

code = [
    int(num)
    for num
    in open('input').read().split(',')
]

i = IntCode(code, [1]).run()
while True:
    print(next(i))

i = IntCode(code, [2]).run()
while True:
    print(next(i))
