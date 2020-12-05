""" part 1
numbers = []

for i in range(200):
    curr = int(input())
    for nr in numbers:
        if curr + nr == 2020:
            print(curr * nr)
            exit()
    numbers.append(curr)
"""
# Part 2
numbers = []

for i in range(200):
    curr = int(input())
    for nr in numbers:
        for nr2 in numbers:
            if nr != nr2:
                if curr + nr + nr2 == 2020:
                    print(curr * nr * nr2)
                    exit()
    numbers.append(curr)
