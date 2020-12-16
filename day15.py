
class Number:
    def __init__(self, nr, initPos):
        self.nr = nr
        self.lastPos = initPos
        self.used = 1
        self.currPos = initPos

    def findNumber(self):
        if self.used == 1:
            return 0
        else:
            return self.currPos - self.lastPos

    def say(self, newPos):
        if self.used == 1:
            self.currPos = newPos
            self.used = 2
        else:
            self.lastPos = self.currPos
            self.currPos = newPos
            self.used += 1


line = [1, 20, 11, 6, 12, 0]

testLine = [0, 3, 6]

mapp = {}

lineUsing = line

i = 1

while i - 1 < len(lineUsing):
    nr = lineUsing[i - 1]
    mapp[nr] = Number(nr, i)
    i += 1

last = mapp[lineUsing[-1]]

while i != 30000001:
    numberToSay = last.findNumber()
    if numberToSay in mapp.keys():
        mapp[numberToSay].say(i)
    else:
        mapp[numberToSay] = Number(numberToSay, i)
    last = mapp[numberToSay]


    i += 1
    if i == 30000001:
        print("fin: " + str(numberToSay))

