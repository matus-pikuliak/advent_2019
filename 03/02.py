import itertools

instructions = [
    [
        (point[0], int(point[1:]))
        for point
        in line.split(',')
    ]
    for line
    in open('input').readlines()
]


def compute_points(instructions):

    new_point = {
        'U': lambda x, y, z, l: (x + l, y, z + l),
        'D': lambda x, y, z, l: (x - l, y, z + l),
        'R': lambda x, y, z, l: (x, y + l, z + l),
        'L': lambda x, y, z, l: (x, y - l, z + l),
    }

    points = [(0, 0, 0)]
    for direction, length in instructions:
        points.append(
            new_point[direction](*points[-1], length)
        )
    return points

points = [
    compute_points(i)
    for i
    in instructions
]


def cross(a_1, a_2, b_1, b_2):
    if a_1 == b_1 or a_1 == b_2:
        return a_1
    if a_2 == b_1 or a_2 == b_2:
        return a_2
    if a_1[0] == a_2[0] and b_1[0] == b_2[0]:
        return None
    if a_1[1] == a_2[1] and b_1[1] == b_2[1]:
        return None
    if a_1[0] == a_2[0]:
        return cross(b_1, b_2, a_1, a_2)
    if a_1[0] > a_2[0]:
        return cross(a_2, a_1, b_1, b_2)
    if b_1[1] > b_2[1]:
        return cross(a_1, a_2, b_2, b_1)
    if a_1[0] < b_1[0] < a_2[0] and b_1[1] < a_1[1] < b_2[1]:
        return b_1[0], a_1[1]
    return None


def distance(a_1, a_2, b_1, b_2):
    c = cross(a_1[:2], a_2[:2], b_1[:2], b_2[:2])
    if c is None:
        return 0
    return a_1[2] + b_1[2] + abs(c[0] - a_1[0]) + abs(c[0] - b_1[0]) + abs(c[1] - a_1[1]) + abs(c[1] - b_1[1])


num_lines = len(points[0]) - 1
min_distance = 10e10
for i, j in itertools.product(range(num_lines), range(num_lines)):
    dist = distance(*points[0][i: i + 2], *points[1][j: j + 2])
    if 0 < dist < min_distance:
        min_distance = dist

print(min_distance)