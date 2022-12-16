data = []
with open("python/Day 4/puzzleInput.txt") as f:
    data = f.readlines()

for i in range(len(data)):
    if ("\n" in data[i]):
        data[i] = data[i][:-1] # remove \n
    

# each element is in the form ((x1, x2), (y1, y2))
formattedData = [[[int(p) for p in points[0].split("-")], [int(p) for p in points[1].split("-")]]for points in [e.split(",") for e in data]]

def checkContains(range1, range2):
    seats1 = [e for e in range(range1[0], range1[1] + 1)]
    seats2 = [e for e in range(range2[0], range2[1] + 1)]
    if len(seats1) < len(seats2):
        return checkContains(range2, range1)

    # assume size of range1 >= range2
    for i in seats2:
        if i not in seats1:
            return 0
    
    return 1

def checkOverlap(range1, range2):
    seats1 = [e for e in range(range1[0], range1[1] + 1)]
    seats2 = [e for e in range(range2[0], range2[1] + 1)]
    for i in seats1:
        if i in seats2:
            return 1
    return 0

total1 = 0
total2 = 0
for e in formattedData:
    total1 += checkContains(e[0], e[1])
    total2 += checkOverlap(e[0], e[1])
print(total1)
print(total2)