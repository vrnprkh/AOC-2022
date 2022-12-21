data = []

with open("python/Day 8/test.txt") as f:
    data = f.readlines()

for i in range(len(data)):
    if ("\n" in data[i]):
        data[i] = data[i][:-1] # remove \n
    

processed = []
for layer in data:
  processed.append([int(e) for e in layer])


def checkVisible(grid, y, x):
  leny = len(grid)
  lenx = len(grid[0])
  height = grid[y][x]
  # UP
  i = y
  up = 1
  while i > 0:
    i -= 1
    if grid[i][x] >= height:
      up = 0
      break
  
  #down
  i = y
  down = 1
  while i < leny - 1:
    i += 1
    if grid[i][x] >= height:
      down = 0
      break
  
   # left
  j = x
  left = 1
  while j > 0:
    j -= 1
    if grid[y][j] >= height:
      left = 0
      break
  
  #right
  j = x
  right = 1
  while j < lenx - 1:
    j += 1
    if grid[y][j] >= height:
      right = 0
      break
  
  return max(up, down, left, right)

def score(grid, x, y):
  leny = len(grid)
  lenx = len(grid[0])
  height = grid[y][x]
  # UP
  i = y
  up = 0
  while i > 0:
    i -= 1
    if grid[i][x] >= height:
      up += 1
      break
    up += 1
  #down
  i = y
  down = 0
  while i < leny - 1:
    i += 1
    if grid[i][x] >= height:
      down += 1
      break
    down += 1
  
   # left
  j = x
  left = 0
  while j > 0:
    j -= 1
    if grid[y][j] >= height:
      left += 1
      break
    left += 1
  
  #right
  j = x
  right = 0
  while j < lenx - 1:
    j += 1
    if grid[y][j] >= height:
      right += 1
      break
    right += 1
  
  return up * left * down * right
total = 0
maxScore = 0
for y in range(len(processed)):
  for x in range(len(processed[0])):
    total += checkVisible(processed, y, x)
    maxScore = max(maxScore, score(processed, y, x))
print(total)
print(maxScore)