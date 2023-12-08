def getLines():
    with open('input.txt') as f:
        for j, l in enumerate(f, start=1):
            yield j, l.strip()


def makeList(l):
    return [int(x) for x in l.split(' ') if x != '']


d = {}


def getNumbers():
    for j, l in getLines():
        card, rest = l.split(':')
        win, ours = rest.strip().split('|')
        res = [i for i in makeList(ours.strip()) if i in makeList(win.strip())]
        k = len(res)
        d[j] = d.get(j, 1)
        if k:
            for i in range(1, k + 1):
                if (j + i < 209):
                    d[j + i] = d.get(j + i, 1) + d[j]


getNumbers()

print(sum(d.values()))
