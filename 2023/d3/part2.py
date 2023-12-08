def getLines():
    with open('input.txt') as f:
        for x, l in enumerate(f):
            for y, c in enumerate(l.strip()):
                yield x, y, c


symbols = []
parts = []


def fillLists():
    coord = []
    i = 0
    for x, y, c in getLines():
        if c.isdigit():
            coord.append((x, y))
            i = i * 10 + int(c)
        else:
            if i != 0:
                parts.append((coord, i))
                coord = []
                i = 0
            if c == '*':
                symbols.append((x, y))


fillLists()


def distance(p1, p2):
    return (p1[0] - p2[0])**2 + (p1[1] - p2[1]) ** 2


def checkPart(coords):
    for c in coords:
        for s in symbols:
            if distance(c, s) <= 2:
                return True
    return False


def checkDist():
    for part in parts:
        if checkPart(part[0]):
            yield(part[1])


def checkParttt(s, part):
    for c in part[0]:
        if distance(c, s) <= 2:
            return True
    return False        


def checkStar():
    for s in symbols:
        i = []
        for part in parts:
            if checkParttt(s,part):
                i.append(part[1])
        if len(i) == 2:
            yield i[0]*i[1]


print(sum(checkStar()))
