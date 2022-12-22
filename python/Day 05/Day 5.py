data = []
with open("python/Day 05/puzzleInput.txt") as f:
    data = f.readlines()

for i in range(len(data)):
    if ("\n" in data[i]):
        data[i] = data[i][:-1] # remove \n

# find boxes
boxes = []
numberIndex = 0
for i, e in enumerate(data):
    if "[" in e:
        boxes.append(e)
    else:
        numberIndex = i
        break

columns = len(data[numberIndex].split())

boxMatrix = []

for i in range(len(boxes) * columns): # max number of boxes stack
    boxMatrix.append([])
    for j in range(columns):
        boxMatrix[-1].append(' ')

# fill matrix
for i in range(numberIndex):
    for j in range(columns):
        boxMatrix[-(i + 1)][j] = data[numberIndex - 1 - i][1 + j * 4]

def makemove1(boxes, n, x1, x2):
    if n == 0:
        return

    # find first box
    i = 0
    j = 0
    while  (i != len(boxMatrix) - 1) and (boxMatrix[i][x1 - 1] == ' '):
        i += 1
    print(i)
    # find spot above second box
    while (j != len(boxMatrix)) and (boxMatrix[j][x2 - 1] == ' ') :
        j += 1
    j -= 1

    boxes[j][x2 - 1] = boxes[i][x1 - 1]
    boxes[i][x1 - 1] = ' '
    makemove1(boxes, n - 1, x1, x2)


def makemove2(boxes, n, x1, x2):
     # find first box
    i = 0
    j = 0
    while  (i != len(boxMatrix) - 1) and (boxMatrix[i][x1 - 1] == ' '):
        i += 1

    # find spot above second box
    while (j != len(boxMatrix)) and (boxMatrix[j][x2 - 1] == ' ') :
        j += 1
    j -= n

    for t in range(n):
        boxes[j + t][x2 - 1] = boxes[i + t][x1 - 1]

        boxes[i + t][x1 - 1] = ' '


def draw(boxes):
    for layer in boxes:
        print(layer)

moves = []
for move in data[numberIndex + 2:]:
    moves.append([int(s) for s in move.split() if s.isdigit()])

draw(boxMatrix)

for move in moves:
    print()
    # makemove1(boxMatrix, move[0], move[1], move[2])
    makemove2(boxMatrix, move[0], move[1], move[2])
    draw(boxMatrix)
    
