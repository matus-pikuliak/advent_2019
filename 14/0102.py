import math

requirements = {}
for line in open('input'):
    req, out = line.strip().split('=>')
    req = [
        r.split()
        for r
        in req.split(', ')
    ]
    count, chem = out.split()
    requirements[chem] = {
        'count': int(count),
        'req': {
            chem: int(count)
            for count, chem
            in req
        }
    }


def create(count, chemical, leftovers):

    reaction_count = math.ceil(count / requirements[chemical]['count'])

    req = {
        req_chem: req_count * reaction_count
        for req_chem, req_count
        in requirements[chemical]['req'].items()
    }

    for left_chem, left_count in list(leftovers.items()):
        if left_chem in req:
            if req[left_chem] > left_count:
                req[left_chem] -= left_count
                del leftovers[left_chem]
            elif req[left_chem] == left_chem:
                del req[left_chem]
                del leftovers[left_chem]
            else:
                leftovers[left_chem] -= req[left_chem]
                del req[left_chem]

    ore_sum = 0
    for req_chem, req_count in req.items():
        if req_chem == 'ORE':
            ore_sum += req_count
        else:
            ore_count, leftovers = create(req_count, req_chem, leftovers)
            ore_sum += ore_count

    left_target = reaction_count * requirements[chemical]['count'] - count
    if left_target > 0:
        if chemical not in leftovers:
            leftovers[chemical] = 0
        leftovers[chemical] += left_target

    return ore_sum, leftovers


print(create(1, 'FUEL', {}))

# Part 2 solved via manual binary search
print(create(7659732, 'FUEL', {}))