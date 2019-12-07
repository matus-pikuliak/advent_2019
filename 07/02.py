import itertools

from intcode import IntCode

code = [
    int(num)
    for num
    in open('input').read().split(',')
]

max_output = 0
for permutation in itertools.permutations(range(5, 10)):
    input = 0
    amps = []
    gens = []
    for phase in permutation:
        amps.append(IntCode(code, [phase, input]))
        gens.append(amps[-1].run())
        input = next(gens[-1])

    try:
        while True:
            for gen in gens:
                input = gen.send(input)
    except StopIteration:
        output = amps[-1].output[-1]
        if output > max_output:
            max_output = output
            print(max_output)
