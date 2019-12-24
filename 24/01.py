import copy

map = [
    list(line.strip())
    for line
    in open('input')
]

def neighbours(x, y):
    if x > 0:
        yield map[x-1][y] == '#'
    if y > 0:
        yield map[x][y-1] == '#'
    if x < len(map) - 1:
        yield map[x + 1][y] == '#'
    if y < len(map[0]) - 1:
        yield map[x][y + 1] == '#'

scores = set()

while True:

    score = sum(
        (char == '#') * 2**i
        for i, char
        in enumerate(
            char
            for line in map
                for char in line
        )
    )
    if score in scores:
        print(score)
        break
    scores.add(score)

    new_map = copy.deepcopy(map)
    for x in range(len(map)):
        for y in range(len(map[0])):
            if map[x][y] == '#' and sum(neighbours(x, y)) != 1:
                new_map[x][y] = '.'
            if map[x][y] == '.' and 1 <= sum(neighbours(x, y)) <= 2:
                new_map[x][y] = '#'
    map = new_map