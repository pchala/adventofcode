import re

rep = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}


def getLines():
    with open('input.txt') as f:
        for l in f:
            yield l.strip()


def getCubes(l):
    d = {}
    for i in l.strip().split(','):
        count, color = i.split()
        d[color.strip()] = int(count)
    return d
    
def checkMax(results):
    r = []
    g = []
    b = []
    for k in results.split(';'):
        d = getCubes(k.strip())
        r.append(d.get('red',0))
        g.append(d.get('green',0))
        b.append(d.get('blue',0))
    if max(r) <= 12 and max(g) <= 13 and max(b) <= 14:
        return True
    else:
        return False

def getPower(results):
    r = []
    g = []
    b = []
    for k in results.split(';'):
        d = getCubes(k.strip())
        r.append(d.get('red',0))
        g.append(d.get('green',0))
        b.append(d.get('blue',0))
    return max(r)*max(g)*max(b)


def splitGame():            
    for line in getLines():
        game, results = line.split(':')
        yield getPower(results)
        # if checkMax(results):
        #     yield int(game[5:])




print(sum(splitGame()))
