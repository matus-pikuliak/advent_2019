def fuel(weight):
    req = weight // 3 - 2
    if req > 0:
        return req + fuel(req)
    return 0

print(
    sum(
        fuel(int(line))
        for line
        in open('input')
    )
)
