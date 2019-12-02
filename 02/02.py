import itertools

from intcode import intcode

input_mem = [
    int(num)
    for num
    in open('input').read().split(',')
]

for noun, verb in itertools.product(range(100), range(100)):
    mem = list(input_mem)
    mem[1] = noun
    mem[2] = verb
    if intcode(mem)[0] == 19690720:
        print(100 * noun + verb)

