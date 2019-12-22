from intcode import IntCode

code = [
    int(num)
    for num
    in open('input').read().split(',')
]


def run_spring(file):

    computer = IntCode(code).run()

    while True:
        out = next(computer)
        if out >= 0:
            try:
                print(chr(out), end='')
            except ValueError:
                print(out)
                break
        else:
            for c in open(file).read():
                computer.send(ord(c))
                next(computer)
            computer.send(10)

run_spring('01.spring')
run_spring('02.spring')