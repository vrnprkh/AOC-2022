data = []
with open("python/Day 03/puzzleInput.txt") as f:
    data = f.readlines()

for i in range(len(data)):
    data[i] = data[i][:-1] # remove \n

formattedData = []
for i in range(len(data)):
    formattedData.append([data[i][:int(len(data[i])/2)], data[i][int(len(data[i])/2):]])

priorityMap = {
    "a":1,
    "b":2,
    "c":3,
    "d":4,
    "e":5,
    "f":6,
    "g":7,
    "h":8,
    "i":9,
    "j":10,
    "k":11,
    "l":12,
    "m":13,
    "n":14,
    "o":15,
    "p":16,
    "q":17,
    "r":18,
    "s":19,
    "t":20,
    "u":21,
    "v":22,
    "w":23,
    "x":24,
    "y":25,
    "z":26,
    "A":1  + 26,
    "B":2  + 26,
    "C":3  + 26,
    "D":4  + 26,
    "E":5  + 26,
    "F":6  + 26,
    "G":7  + 26,
    "H":8  + 26,
    "I":9  + 26,
    "J":10 + 26,
    "K":11 + 26,
    "L":12 + 26,
    "M":13 + 26,
    "N":14 + 26,
    "O":15 + 26,
    "P":16 + 26,
    "Q":17 + 26,
    "R":18 + 26,
    "S":19 + 26,
    "T":20 + 26,
    "U":21 + 26,
    "V":22 + 26,
    "W":23 + 26,
    "X":24 + 26,
    "Y":25 + 26,
    "Z":26 + 26,
}


total = 0
for i, rucksack in enumerate(formattedData):
    matches = set()
    for item0 in rucksack[0]:
        for item1 in rucksack[1]:
            if item0 == item1:
                matches.add(priorityMap[item0])

    total += sum(matches)
    if len(matches) > 1:
        print(rucksack, matches, i)

print(total)

# part 2
total2 = 0
for i in range(int(len(data)/3)):
    total2 += priorityMap[[match for match in data[3 * i] if (match in data[3 * i + 1]) and (match in data[3 * i + 2])][0]]

print(total2)
