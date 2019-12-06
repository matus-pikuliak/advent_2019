orbits = dict(
    reversed(line.strip().split(')'))
    for line
    in open('input')
)


def get_orbited(planet):
    if planet in orbits:
        return {orbits[planet]} | get_orbited(orbits[planet])
    return set()

print(len(get_orbited('SAN') ^ get_orbited('YOU')))
