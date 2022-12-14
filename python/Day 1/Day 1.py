data = []

with open("python/Day 1/puzzleInput.txt") as f:
    data = f.readlines()
formattedData = []
for e in data:
    try:
        formattedData.append(int(e))
    except:
        formattedData.append(-1)

formattedData.append(-1)

runningTotal = 0
maxValue = 0
maxValues = [0,0,0]
for e in formattedData:
    if e != -1:
        runningTotal += e
        
    else:
        maxValue = max(runningTotal, maxValue)

        for i in range(len(maxValues)):
            if (maxValues[i] < runningTotal):
                maxValues[i] = runningTotal
                break
        maxValues.sort()
        runningTotal = 0

print(maxValue)
print(maxValues)
print(sum(maxValues))