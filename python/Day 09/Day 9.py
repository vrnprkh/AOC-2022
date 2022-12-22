data = []

with open("python/Day 09/test.txt") as f:
    data = f.readlines()

for i in range(len(data)):
    if ("\n" in data[i]):
        data[i] = data[i][:-1] # remove \n
    
process = [(e[0], int(e[1])) for e in [row.split() for row in data]]

class Board:
  def __init__(self): 
    self.visited = {(0,0)}
    self.taily = 0
    self.tailx = 0
    self.heady = 0
    self.headx = 0
  
  def distance(self):
    return max(abs(self.taily - self.heady), abs(self.tailx - self.headx))
    
  def getSize(self):
    return len(self.visited)
  def move(self, move):
    yOff = 0
    xOff = 0
    if move[0] == "U":
      yOff = 1
    elif move[0] == "D":
      yOff = -1
    elif move[0] == "R":
      xOff = 1
    else:
      xOff = -1
    
    for i in range(move[1]):
      
      self.heady += yOff
      self.headx += xOff
      if self.distance() > 1:
        self.taily = self.heady - yOff
        self.tailx = self.headx - xOff
        
        self.visited.add((self.tailx, self.taily))
    

board = Board()

for move in process:
  board.move(move)




print(board.getSize())

def signof(x):
  if x > 0:
    return 1
  if x < 0:
    return -1
  return 0

class Board2():
  def __init__(self):
    self.knots = [[0,0] for i in range(10)]
    self.visited = {(0,0)}
  
  def distance(self, i1, i2):
    return max(abs(self.knots[i1][0] - self.knots[i2][0]), abs(self.knots[i1][1] - self.knots[i2][1]))
  
  def getSize(self):
    return len(self.visited)
  
  # transforms i1 to follow i2
  def follow(self, i1, i2):
    if self.distance(i1, i2) > 1: # this is way smarter essentially floors to 1 or -1 if distance is bigger than 2
      self.knots[i1][0] += min(abs(self.knots[i2][0] - self.knots[i1][0]), 1) * signof(self.knots[i2][0] - self.knots[i1][0])
      self.knots[i1][1] += min(abs(self.knots[i2][1] - self.knots[i1][1]), 1) * signof(self.knots[i2][1] - self.knots[i1][1])

  def move(self, move):
    yOff = 0
    xOff = 0
    if move[0] == "U":
      yOff = 1
    elif move[0] == "D":
      yOff = -1
    elif move[0] == "R":
      xOff = 1
    else:
      xOff = -1
    
    
    for i in range(move[1]):
      self.knots[0][0] += xOff
      self.knots[0][1] += yOff
      for j in range(len(self.knots) - 1):
        self.follow(j + 1, j)
      self.visited.add((self.knots[-1][0], self.knots[-1][1]))

board2 = Board2()
for move in process:
  board2.move(move)
  

print(board2.getSize())