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

nat = None
last_nat_y = 0
while True:
    idle = True
    for i, c in enumerate(computers):
        a = next(c)
        if a < 0:
            if queues[i]:
                idle = False
                c.send(queues[i].pop(0))
                next(c)
                c.send(queues[i].pop(0))
            else:
                c.send(-1)
        else:
            idle = False
            if a == 255:
                nat = next(c), next(c)
            else:
                queues[a].append(next(c))
                queues[a].append(next(c))
    if idle and nat:
        if nat[1] == last_nat_y:
            print(nat[1])
            exit()
        last_nat_y = nat[1]
        queues[0].append(nat[0])
        queues[0].append(nat[1])
