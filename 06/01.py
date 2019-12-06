orbits = dict(
    reversed(line.strip().split(')'))
    for line
    in open('input')
)


def get_orbited(planet):
    if planet in orbits:
        return {orbits[planet]} | get_orbited(orbits[planet])
    return set()

print(
    sum(
        len(get_orbited(planet))
        for planet
        in set(orbits.keys()) | set(orbits.values())
    )
)