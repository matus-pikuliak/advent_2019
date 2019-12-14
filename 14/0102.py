import math

reactions = {}
for line in open('input'):
    required, target = line.strip().split('=>')
    required = [
        r.split()
        for r
        in required.split(', ')
    ]
    target_count, target = target.split()
    reactions[target] = {
        'count': int(target_count),
        'req': {
            chem: int(count)
            for count, chem
            in required
        }
    }


def create(target_count, target, leftovers):

    if target_count == 0:
        return 0, leftovers

    reaction_count = math.ceil(target_count / reactions[target]['count'])

    required = dict(reactions[target]['req'])
    for chem in required:
        required[chem] *= reaction_count

    for chem, count in leftovers.items():
        if chem in required:
            count = min(required[chem], count)
            required[chem] -= count
            leftovers[chem] -= count

    ore_sum = 0
    for chem, count in required.items():
        if chem == 'ORE':
            ore_sum += count
        else:
            ore_count, leftovers = create(count, chem, leftovers)
            ore_sum += ore_count

    if target not in leftovers:
        leftovers[target] = 0
    leftovers[target] += reaction_count * reactions[target]['count'] - target_count

    return ore_sum, leftovers


print(create(1, 'FUEL', {}))

# Part 2 solved via manual binary search
print(create(7659732, 'FUEL', {}))