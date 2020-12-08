import copy


commands = {}
acc = 0
pc = 0


def check(pc2, mapping):

    if mapping[pc][1][0] == "nop":
        mapping[pc][1][0] = "jmp"
    else:
        mapping[pc][1][0] = "nop"

    while True:
        if pc2 >= 626:  # end of file
            return True
        currTryCom = mapping[pc2][1]
        if mapping[pc2][0] != -1:  # found loop
            return False
        elif currTryCom[0] == "nop":
            mapping[pc2][0] = 1
            pc2 += 1
        elif currTryCom[0] == "acc":
            mapping[pc2][0] = 1
            pc2 += 1
        else:
            mapping[pc2][0] = 1
            pc2 += currTryCom[1]


for i in range(626):
    line = input().split()
    line[1] = int(line[1])
    commands[i] = [-1, line]

found = False

while True:
    if pc >= 626:  # end of file
        break
    currCom = commands[pc][1]
    if commands[pc][0] != -1:  # found loop
        print("still looping")
        break
    elif currCom[0] == "nop":
        if not found and check(pc, copy.deepcopy(commands)):
            found = True
            currCom[0] = "jmp"
            commands[pc][0] = acc
            pc += currCom[1]
        else:
            commands[pc][0] = acc
            pc += 1
    elif currCom[0] == "acc":
        commands[pc][0] = acc
        acc += currCom[1]
        pc += 1
    else:
        c = copy.deepcopy(commands)
        if not found and check(pc, c):
            found = True
            currCom[0] = "nop"
            commands[pc][0] = acc
            pc += 1
        else:
            commands[pc][0] = acc
            pc += currCom[1]

print(found)
print(acc)