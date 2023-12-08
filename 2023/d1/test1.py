def getHalves():
    l = 1
    with open('input.txt') as f:
        while True:
            char = f.read(1)
            if not char:
                break
            yield l, char
            l += 1


l = 0
for i, c in getHalves():
    if c == '(':
        l += 1
    if c == ')':
        l -= 1
    if l == -1:
        print(i)
