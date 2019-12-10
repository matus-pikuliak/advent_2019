import numpy as np

asteroids = [
    np.array([i, j])
    for i, line in enumerate(open('input'))
        for j, char in enumerate(line.strip())
    if char == '#'
]


def can_see(a, b, other):

    if a is b:
        return False

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


def generate_key_function(zero):

    def key_function(tpl):
        tpl = np.array(tpl)
        tpl -= zero
        tpl = tpl / np.linalg.norm(tpl)
        if tpl[1] >= 0:
            return tpl[0] - 1
        else:
            return 1 - tpl[0]

    return key_function


for asteroid in asteroids:
    if np.array_equal(asteroid, np.array([22, 17])):
        central = asteroid
        kf = generate_key_function(central)
        break


pointer = 199
while True:
    visible = sorted(
        [asteroid
        for asteroid
        in asteroids
        if can_see(central, asteroid, asteroids)],
        key=kf
    )

    if len(visible) <= pointer:
        pointer -= len(visible)
        for asteroid in visible:
            asteroids.remove(asteroid)
    else:
        print(visible[pointer])
        break
