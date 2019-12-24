import copy

map = [
    [
        ['.' for _ in range(5)]
        for _ in range(5)
    ]
    for _ in range(401)
]

for i, line in enumerate(open('input')):
    map[200][i] = list(line.strip())


def neighbours(d, x, y):
    if x > 0:
        yield map[d][x-1][y]
    else:
        if d > 0:
            yield map[d-1][1][2]
    if y > 0:
        yield map[d][x][y-1]
    else:
        if d > 0:
            yield map[d-1][2][1]
    if x < 4:
        yield map[d][x + 1][y]
    else:
        if d > 0:
            yield map[d-1][3][2]
    if y < 4:
        yield map[d][x][y + 1]
    else:
        if d > 0:
            yield map[d-1][2][3]

    if (x, y) == (1, 2):
        for i in range(5):
            if d < 399:
                yield map[d+1][0][i]
    if (x, y) == (3, 2):
        for i in range(5):
            if d < 399:
                yield map[d+1][4][i]
    if (x, y) == (2, 1):
        for i in range(5):
            if d < 399:
                yield map[d+1][i][0]
    if (x, y) == (2, 3):
        for i in range(5):
            if d < 399:
                yield map[d+1][i][4]


for i in range(200):

    new_map = copy.deepcopy(map)
    score = 0
    for d in range(199 - i, 202 + i):
        for x in range(5):
            for y in range(5):
                num_neighbours = sum(char == '#' for char in neighbours(d, x, y))
                if not (x == 2 and y == 2):
                    if map[d][x][y] == '#' and num_neighbours != 1:
                        new_map[d][x][y] = '.'
                    if map[d][x][y] == '.' and 1 <= num_neighbours <= 2:
                        new_map[d][x][y] = '#'
                if new_map[d][x][y] == '#':
                    score += 1
    map = new_map

print(score)
