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
            yield injectNumbers(l.strip())


def injectNumbers(l):
    for i in range(len(l)):
        for word in rep.keys():
            if l[i:].startswith(word):
                l = l[:i] + rep[word] + l[i + 1:]
    return l


def getNumbers():
    for l in getLines():
        n = re.sub("[^0-9]", "", l)
        yield int(n[0] + n[-1])


print(sum(getNumbers()))
