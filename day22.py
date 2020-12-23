import copy


class Player:
    def __init__(self):
        self.deck = []

    def lose(self):
        return len(self.deck) == 0


pls = []
for i in range(2):
    p = Player()
    input()
    line = input()
    while line != "":
        p.deck.append(int(line))
        line = input()

    pls.append(copy.deepcopy(p))


p1 = pls[0]
p2 = pls[1]

while not p1.lose() and not p2.lose():
    c1 = p1.deck.pop(0)
    c2 = p2.deck.pop(0)
    if c1 > c2:
        p1.deck.append(c1)
        p1.deck.append(c2)
    else:
        p2.deck.append(c2)
        p2.deck.append(c1)

m = []
if p1.lose():
    m = p2.deck
else:
    m = p1.deck

m.reverse()
res = 0
for c in range(len(m)):
    res += (c+1) * m[c]

print(res)