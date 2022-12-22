data = []

with open("python/Day 10/test.txt") as f:
    data = f.readlines()

for i in range(len(data)):
    if ("\n" in data[i]):
        data[i] = data[i][:-1] # remove \n

data2 = [e.split() for e in data]
proc = []
for e in data2:
  if e[0] == "noop":
    proc.append(0)
  else:
    proc.append(int(e[1]))


class Computer:
  def __init__(self, code):
    self.pos = 0
    self.code = code
    self.cycle = 0
    self.X = 1
    self.q = 0
    self.delay = 0
  def simulate(self):
    self.cycle += 1
    if self.delay == 1:
      self.delay -= 1
      return

    self.X += self.q
    self.q = 0
    if self.pos > len(self.code):
      return
    elif self.code[self.pos] == 0:
      self.pos += 1
      return
    self.delay = 1
    self.q = self.code[self.pos]
    self.pos += 1



  def getSignal(self):
    return self.X * (self.cycle)
  def getX(self):
    return self.X
  

def simul(n, code):
  comp = Computer(code)
  for i in range(n):
    # print(comp.cycle, comp.getSignal(), comp.getX())
    comp.simulate()
    
  
  # print(comp.cycle ,comp.getSignal(), comp.getX())
  return comp.getSignal(), comp.getX()


# print(simul(20, proc))
# print(simul(60, proc))
# print(simul(100, proc))
# print(simul(140, proc))
# print(simul(180, proc))
# print(simul(220, proc))

total = 0
for i in range(6):
  total += simul(20 + i * 40, proc)[0]
print(total)


drawStr = ""
for i in range(6):
  drawLayer = ""
  for j in range(40):
    if abs(j - simul(i * 40 + j + 1, proc)[1]) <= 1:
      drawLayer += "#"
    else:
      drawLayer += "."
  drawStr += drawLayer + "\n"

print(drawStr)

