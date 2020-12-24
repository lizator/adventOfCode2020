import copy

lowerSaves = {}


def playGame(p1l, p2l, deep, lower):
    if not deep in lower.keys():
        lower[deep] = {}
    #print(deep)
    gameStates = []
    p1 = Player()
    p1.deck = copy.deepcopy(p1l)
    p2 = Player()
    p2.deck = copy.deepcopy(p2l)
    loop = False
    while not p1.lose() and not p2.lose():
        currState = p1.deck + [-1] + p2.deck
        if currState in gameStates:
            loop = True
            break
        gameStates.append(currState)

        c1 = p1.deck.pop(0)
        c2 = p2.deck.pop(0)
        con = []
        if c1 <= len(p1.deck) and c2 <= len(p2.deck):
            key = ""
            for c in p1.deck:
                key += str(c) + ","
            key += "-"
            for c in p2.deck:
                key += str(c) + ","
            if key in lower[deep].keys():
                con = lower[deep][key]
            else:
                con = playGame(p1.deck, p2.deck, deep + 1, lower)
                lower[deep][key] = con
            if con[0]:
                p1.deck.append(c1)
                p1.deck.append(c2)
            else:
                p2.deck.append(c2)
                p2.deck.append(c1)
        elif c1 > c2:
            p1.deck.append(c1)
            p1.deck.append(c2)
        else:
            p2.deck.append(c2)
            p2.deck.append(c1)
    if loop or p2.lose():
        return [True, p1.deck]
    return [False, p2.deck]


class Player:
    def __init__(self):
        self.deck = []

    def lose(self):
        return len(self.deck) == 0


pls = []
for i in range(2):
    pls.append([])
    input()
    line = input()
    while line != "":
        pls[i].append(int(line))
        line = input()

lowers = {}

ret = playGame(pls[0], pls[1], 0, lowers)

m = ret[1]
print(ret)
m.reverse()
res = 0
for c in range(len(m)):
    res += (c+1) * m[c]

print(res)