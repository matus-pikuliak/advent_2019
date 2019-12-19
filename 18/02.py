import itertools
import pprint


def neighbours(point):
    x, y = point
    ns = []
    for n in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
        try:
            if map[n] != '#':
                ns.append(n)
        except KeyError:
            pass
    return ns


map = dict()
points = dict()

for i, line in enumerate(open('input')):
    for j, char in enumerate(line.strip()):
        map[(i, j)] = char
        if char == '@' or 'a' <= char <= 'z':
            points[char] = (i, j)

frontier = {points['@']}
needs = {points['@']: set()}
seen = {points['@']: set()}

while frontier:
    new_frontier = set()
    for f in frontier:
        for n in neighbours(f):
            if n not in needs:
                new_frontier.add(n)
                needs[n] = set(needs[f])
                seen[n] = set(seen[f])
                if 'A' <= map[n] <= 'Z':
                    needs[n].add(map[n].lower())
                if 'a' <= map[n] <= 'z':
                    seen[n].add(map[n].lower())
    frontier = new_frontier


needs = {points[point]: needs[points[point]] for point in points}
seen = {points[point]: seen[points[point]] for point in points}

for point in sorted(points):
    needs[points[point]] = needs[points[point]] - seen[points[point]]
    seen[points[point]] = seen[points[point]] - {point}

# remove if the key does not unlock anything and is seen on path to other key
out = set()
for point in points:
    if any(point in seen_value for seen_value in seen.values()) \
            and not any(point in need_value for need_value in needs.values()):
        out.add(point)

points = {k: v for k, v in points.items() if k not in out}
for point in sorted(points):
    seen[points[point]] -= out
    needs[points[point]] -= out

depends = {map[point]: need for point, need in needs.items()}

for point in depends:
    while True:
        in_len = len(depends[point])
        for p in list(depends[point]):
            depends[point] = depends[point].union(depends[p])
        out_len = len(depends[point])
        if out_len == in_len:
            break

sector_points = [[] for _ in range(4)]
for point, xy in points.items():
    x, y = xy
    if x > 40 and y > 40:
        sector_points[0].append(point)
    if x > 40 and y < 40:
        sector_points[1].append(point)
    if x < 40 and y > 40:
        sector_points[2].append(point)
    if x < 40 and y < 40:
        sector_points[3].append(point)

cache = {}
def path_len(a, b):

    if (a, b) in cache:
        return cache[(a, b)]
    if (b, a) in cache:
        return cache[(b, a)]

    frontier = {points[a]}
    paths = {points[a]: 0}

    while frontier:
        new_frontier = set()
        for f in frontier:
            for n in neighbours(f):
                if n not in paths:
                    new_frontier.add(n)
                    paths[n] = paths[f] + 1
        frontier = new_frontier

    for point, xy in points.items():
        cache[(a, point)] = paths[xy]

    return cache[(a, b)]


min = 10 ** 10
for paths in itertools.product(*[
    itertools.permutations(sector_points[i])
    for i in
    range(4)
]):

    try:
        for path in paths:
            for x, y in itertools.combinations(path, r=2):
                if y in depends[x]:
                    raise AttributeError
    except AttributeError:
        continue


    total = 0
    for path in paths:
        start = '@'
        for end in path:
            total += path_len(start, end)
            start = end
    total -= 8
    if total < min:
        min = total

print(min)

