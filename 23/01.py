from intcode import IntCode

code = [
    int(num)
    for num
    in open('input').read().split(',')
]

def create_computer(id):
    computer = IntCode(code).run()
    next(computer)
    computer.send(id)
    return computer

computers = [create_computer(i) for i in range(50)]
queues = [[] for _ in range(50)]

while True:
    for i, c in enumerate(computers):
        a = next(c)
        if a < 0:
            if queues[i]:
                c.send(queues[i].pop(0))
                next(c)
                c.send(queues[i].pop(0))
            else:
                c.send(-1)
        else:
            if a == 255:
                print(next(c), next(c))
            else:
                queues[a].append(next(c))
                queues[a].append(next(c))
