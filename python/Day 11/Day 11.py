class Monkey:
  def __init__(self, monkeyType, items, opValue, testDiv, tpass, fpass):
    self.monkeyType = monkeyType
    self.items = items
    self.opValue = opValue
    self.testDiv = testDiv
    self.tpass = tpass
    self.fpass = fpass
    self.inspects = 0
  
  # returns a list of lists [[tpass items], [fpass items]], will also update inspects, and empty items
  def detPasses(self):
    self.inspects += len(self.items)
    # update values
    if self.monkeyType == "+":
      for i, item in enumerate(self.items):
        self.items[i] = int((item + self.opValue) / 3)
    elif self.monkeyType == "*":
      for i, item in enumerate(self.items):
        self.items[i] = int(item * self.opValue / 3)
    else:
      for i, item in enumerate(self.items):
        self.items[i] = int(item * item / 3)
    
    tlist = []
    flist = []
    for item in self.items:
      if item % self.testDiv == 0:
        tlist.append(item)
      else:
        flist.append(item)
      
    self.items = []
    return [tlist, flist]
  
  def addItems(self, nItems):
    for item in nItems:
      self.items.append(item)
  

monkeys0 = [
  Monkey("*", [79, 98], 19, 23, 2, 3),
  Monkey("+", [54, 65, 75, 74], 6, 19, 2, 0),
  Monkey("O", [79, 60, 97], 0, 13, 1, 3),
  Monkey("+", [74], 3, 17, 0, 1),
]

monkeys1 = [
  Monkey("*", [98, 89, 52],                      2,  5, 6, 1),
  Monkey("*", [57, 95, 80, 92, 57, 78],         13,  2, 2, 6),
  Monkey("+", [82, 74, 97, 75, 51, 92, 83],      5, 19, 7, 5),
  Monkey("+", [97, 88, 51, 68, 76],              6,  7, 0, 4),
  Monkey("+", [63],                              1, 17, 0, 1),
  Monkey("+", [94, 91, 51, 63],                  4, 13, 4, 3),
  Monkey("+", [61, 54, 94, 71, 74, 68, 98, 83],  2,  3, 2, 7),
  Monkey("O", [90, 56],                          0, 11, 3, 5),
]



class SuperMonkey:
  def __init__(self, monkeys): # assume monkeys are in order
    self.monkeys = monkeys
  
  def doround(self):
    for monkey in self.monkeys:
      passes = monkey.detPasses()
      self.monkeys[monkey.tpass].addItems(passes[0])
      self.monkeys[monkey.fpass].addItems(passes[1])

  def monkeyBusiness(self):
    return sorted([monkey.inspects for monkey in self.monkeys])[-1] * sorted([monkey.inspects for monkey in self.monkeys])[-2]


test = SuperMonkey(monkeys0)
test2 = SuperMonkey(monkeys1)
for i in range(20):
  test.doround()
  test2.doround()


print(test.monkeyBusiness())
print(test2.monkeyBusiness())

class Monkey2:
  def __init__(self, monkeyType, items, opValue, testDiv, tpass, fpass):
    self.monkeyType = monkeyType
    self.items = items
    self.opValue = opValue
    self.testDiv = testDiv
    self.tpass = tpass
    self.fpass = fpass
    self.inspects = 0
  
  # returns a list of lists [[tpass items], [fpass items]], will also update inspects, and empty items
  def detPasses(self):
    self.inspects += len(self.items)
    # update values
    if self.monkeyType == "+":
      for i, item in enumerate(self.items):
        self.items[i] = item + self.opValue
    elif self.monkeyType == "*":
      for i, item in enumerate(self.items):
        self.items[i] = item * self.opValue
    else:
      for i, item in enumerate(self.items):
        self.items[i] = item * item
    
    tlist = []
    flist = []
    for item in self.items:
      if item % self.testDiv == 0:
        tlist.append(item)
      else:
        flist.append(item)
      
    self.items = []
    return [tlist, flist]
  
  def addItems(self, nItems):
    for item in nItems:
      self.items.append(item)


monkey2s0 = [
  Monkey2("*", [79, 98], 19, 23, 2, 3),
  Monkey2("+", [54, 65, 75, 74], 6, 19, 2, 0),
  Monkey2("O", [79, 60, 97], 0, 13, 1, 3),
  Monkey2("+", [74], 3, 17, 0, 1),
]

monkey2s1 = [
  Monkey2("*", [98, 89, 52],                      2,  5, 6, 1),
  Monkey2("*", [57, 95, 80, 92, 57, 78],         13,  2, 2, 6),
  Monkey2("+", [82, 74, 97, 75, 51, 92, 83],      5, 19, 7, 5),
  Monkey2("+", [97, 88, 51, 68, 76],              6,  7, 0, 4),
  Monkey2("+", [63],                              1, 17, 0, 1),
  Monkey2("+", [94, 91, 51, 63],                  4, 13, 4, 3),
  Monkey2("+", [61, 54, 94, 71, 74, 68, 98, 83],  2,  3, 2, 7),
  Monkey2("O", [90, 56],                          0, 11, 3, 5),
]


class SuperMonkey2:
  def __init__(self, monkeys): # assume monkeys are in order
    self.monkeys = monkeys
    self.common = 1
    for monkey in self.monkeys:
      self.common *= monkey.testDiv
    
  
  def doround(self):
    for monkey in self.monkeys:
      passes = monkey.detPasses()
      self.monkeys[monkey.tpass].addItems([e % self.common for e in passes[0]])
      self.monkeys[monkey.fpass].addItems([e % self.common for e in passes[1]])

  def monkeyBusiness(self):
    return sorted([monkey.inspects for monkey in self.monkeys])[-1] * sorted([monkey.inspects for monkey in self.monkeys])[-2]




test20 = SuperMonkey2(monkey2s0)
test21 = SuperMonkey2(monkey2s1)




for i in range(10000):
  test20.doround()
  test21.doround()

print(test20.monkeyBusiness())
print(test21.monkeyBusiness())