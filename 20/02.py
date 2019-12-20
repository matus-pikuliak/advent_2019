map = open('input').readlines()


def get_map(x, y):
    try:
        return map[x][y]
    except IndexError:
        return ' '


gates = dict()
in_connections = dict()
out_connections = dict()


def add_gate(name, x, y):
    print(name, x, y)
    if name in gates:
        if x > 110 or x == 2 or y > 110 or y == 2:
            out_connections[(x, y)] = gates[name]
            in_connections[gates[name]] = (x, y)
        else:
            in_connections[(x, y)] = gates[name]
            out_connections[gates[name]] = (x, y)
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


def neighbours(x, y, z):
    if get_map(x + 1, y) == '.':
        yield x + 1, y, z
    if get_map(x - 1, y) == '.':
        yield x - 1, y, z
    if get_map(x, y + 1) == '.':
        yield x, y + 1, z
    if get_map(x, y - 1) == '.':
        yield x, y - 1, z
    if (x, y) in out_connections and z >= 0:
        yield (*out_connections[(x, y)], z - 1)
    if (x, y) in in_connections:
        yield (*in_connections[(x, y)], z + 1)


paths = {(*gates['AA'], 0): 0}
frontier = {(*gates['AA'], 0)}
step = 0
while True:
    new_frontier = set()

    for point in frontier:
        for n in neighbours(*point):
            if n not in paths:
                new_frontier.add(n)
                paths[n] = step + 1

    frontier = new_frontier
    step += 1

    if (*gates['ZZ'], 0) in paths:
        print(paths[(*gates['ZZ'], 0)])
        break
