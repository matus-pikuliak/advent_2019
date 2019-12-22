import math

deck_size = 119315717514047
focus = 2020
file = 'input'
steps = 101741582076661

a = 1
b = 0
for line in open(file):
    words = line.split()

    if words[1] == 'with':
        inc = int(words[-1])
        a *= inc
        b *= inc
    elif words[1] == 'into':
        a *= -1
        b *= -1
        b -= 1
    else:
        cut = int(words[-1])
        b -= cut

cache = {0: (a, b)}
for i in range(1, 50):
    a, b = cache[i - 1]
    a %= deck_size
    b %= deck_size
    cache[i] = (a ** 2, a * b + b)

while True:
    log = int(math.log2(steps))
    a, b = cache[log]
    focus = focus * a + b
    focus %= deck_size
    steps -= 2 ** log
    print(steps, log, focus)



