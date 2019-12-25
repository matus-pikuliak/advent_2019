from intcode import IntCode
import itertools


def powerset(iterable):
    s = list(iterable)
    return itertools.chain.from_iterable(itertools.combinations(s, r) for r in range(len(s)+1))


code = [
    int(num)
    for num
    in open('input').read().split(',')
]

computer = IntCode(code).run()
commands = open('script')


def run_command(command=None):
    while True:
        out = next(computer)
        if out >= 0:
            print(chr(out), end='')
        else:
            if not command:
                command = input()
            for char in command:
                computer.send(ord(char))
                next(computer)
            computer.send(ord('\n'))
            break


for command in open('script'):
    run_command(command.strip())

items = ['candy cane', 'wreath', 'hypercube', 'food ration', 'weather machine', 'space law space brochure', 'prime number', 'astrolabe']

for combo in powerset(items):
    for item in items:
        if item in combo:
            run_command(f'take {item}')
        else:
            run_command(f'drop {item}')
    run_command(f'west')