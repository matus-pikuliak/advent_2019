import numpy as np

asteroids = [
    np.array([i, j])
    for i, line in enumerate(open('input'))
        for j, char in enumerate(line.strip())
    if char == '#'
]


def can_see(a, b, other):
    for c in other:
        if c is a or c is b:
            continue

        if (
            (a[0] <= c[0] <= b[0] or a[0] >= c[0] >= b[0])
            and
            (a[1] <= c[1] <= b[1] or a[1] >= c[1] >= b[1])
        ):
            ac = a - c
            ab = a - b
            if ab[0] * ac[1] == ab[1] * ac[0]:
                return False

    return True


max = 0
for station in asteroids:
    current = sum(
        can_see(station, observed, other=asteroids)
        for observed in asteroids
        if observed is not station
    )

    if current > max:
        print(station, current)
        max = current
