import itertools

from intcode import IntCode

code = [
    int(num)
    for num
    in open('input').read().split(',')
]

max_output = 0
for permutation in itertools.permutations(range(5)):
    input = 0
    for phase in permutation:
        amp = IntCode(code, [phase, input])
        input = next(amp.run())
    if input > max_output:
        print(input, permutation)
        max_output = input
