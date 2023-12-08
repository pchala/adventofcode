def getLines():
    with open('input.txt') as f:
        for l in f:
            yield l.strip()


def makeList(l):
    return [int(x) for x in l.split(' ') if x != '']


def getNumbers():
    for l in getLines():
        card, rest = l.split(':')
        win, ours = rest.strip().split('|')
        res = [i for i in makeList(ours.strip()) if i in makeList(win.strip())]
        if len(res):
            yield 2 ** (len(res) - 1)


print(sum(getNumbers()))
