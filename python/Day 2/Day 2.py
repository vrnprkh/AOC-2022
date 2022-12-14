data = []
with open("python/Day 2/puzzleInput.txt") as f:
    data = f.readlines()

formattedData = []

for e in data:
    formattedData.append(e.split())

LetterToNum = {
    "A":1,
    "B":2,
    "C":3,
    "X":1,
    "Y":2,
    "Z":3,
}

def getScore(elfNum, playerNum):
    # Draw
    if (playerNum == elfNum):
        return playerNum + 3
    
    # win
    if ((playerNum == 3 and elfNum == 2) or (playerNum == 2 and elfNum == 1) or (playerNum == 1 and elfNum == 3)):
        return playerNum + 6
    
    # loss
    return playerNum


total1 = 0
for e in formattedData:
    total1 += getScore(LetterToNum[e[0]], LetterToNum[e[1]])


print(total1)
total2 = 0
for e in formattedData:
    elf = LetterToNum[e[0]]
    if (e[1] == "X"):
        player = (elf + 1) % 3 + 1
    elif (e[1] == "Y"):
        player = elf
    elif (e[1] == "Z"):
        player = elf % 3 + 1
    

    total2 += getScore(elf, player)

print(total2)