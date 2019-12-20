map = open('input').readlines()


def get_map(x, y):
    try:
        return map[x][y]
    except IndexError:
        return ' '


gates = dict()
connections = dict()


def add_gate(name, x, y):
    print(name, x, y)
    if name in gates:
        connections[(x, y)] = gates[name]
        connections[gates[name]] = (x, y)
    else:
        gates[name] = (x, y)


for i, line in enumerate(map):
    for j, char in enumerate(line):
        if 'A' <= char <= 'Z':
            if 'A' <= get_map(i+1, j) <= 'Z':
                gate = char + get_map(i+1, j)
                if get_map(i-1, j) == '.':
                    add_gate(gate, i-1, j)
                else:
                    add_gate(gate, i+2, j)

            if 'A' <= get_map(i, j+1) <= 'Z':
                gate = char + get_map(i, j+1)
                if get_map(i, j-1) == '.':
                    add_gate(gate, i, j-1)
                else:
                    add_gate(gate, i, j+2)


def neighbours(x, y):
    if get_map(x + 1, y) == '.':
        yield x + 1, y
    if get_map(x - 1, y) == '.':
        yield x - 1, y
    if get_map(x, y + 1) == '.':
        yield x, y + 1
    if get_map(x, y - 1) == '.':
        yield x, y - 1
    if (x, y) in connections:
        yield connections[(x, y)]


paths = {gates['AA']: 0}
step = 0
while True:
    for point, path in list(paths.items()):
        if path == step:
            for n in neighbours(*point):
                if n not in paths:
                    paths[n] = step + 1
    if gates['ZZ'] in paths:
        break
    step += 1

print(paths)