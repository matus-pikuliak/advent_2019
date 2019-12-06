orbits = [
    tuple(line.strip().split(')'))
    for line
    in open('input')
]

planets = {
    planet: None
    for orbit in orbits
        for planet in orbit
}


def compute(planet):
    if planets[planet] is not None:
        return planets[planet]
    planets[planet] = sum(
        compute(orbiting) + 1
        for (orbited, orbiting)
        in orbits
        if orbited == planet
    )
    return planets[planet]

print(
    sum(
        compute(planet)
        for planet
        in planets
    )
)