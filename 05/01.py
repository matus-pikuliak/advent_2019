from intcode import IntCode

intcode = IntCode([
    int(num)
    for num
    in open('input').read().split(',')
], 1)

intcode.run()