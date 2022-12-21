data = []

with open("python/Day 7/test.txt") as f:
    data = f.readlines()

for i in range(len(data)):
    if ("\n" in data[i]):
        data[i] = data[i][:-1] # remove \n
  
class Dir:
  def __init__(self, name):
    self.files = {}
    self.subDirs = {}
    self.name = name
  
  def addDir(self, newDir):
    self.subDirs[newDir.name] = newDir
  
  def addFile(self, file):
    self.files[file.name] = file
  
  def getSize(self):
    sum = 0
    for e in self.files:
      sum += self.files[e].size
    
    for e in self.subDirs:
      sum += self.subDirs[e].getSize()
    
    return sum

class File:
  def __init__(self, name, size):
    self.size = size
    self.name = name


# command WITHOUT $ cd 
def cd(path, command):
  if command == "..":
    for i in reversed(range(len(path) - 1)):
      if path[i] == "/":
        return path[:i + 1]
  if command == "/":
    return "/"
  
  return path + command + "/"

def addDirFromPath(path, parent, dir):
  tempPath = path.split("/")
  newPath = [e for e in tempPath if e != ""]
  return addDirFromPathHelper(newPath, parent ,dir)

def addDirFromPathHelper(modPath, parent, dir):
  if len(modPath) == 0:
    parent.addDir(dir)
  elif len(modPath) == 1:
    parent.subDirs[modPath[0]].addDir(dir)
  else:
    addDirFromPathHelper(modPath[1:], parent.subDirs[modPath[0]], dir)


def addFileFromPath(path, parent, file):
  tempPath = path.split("/")
  newPath = [e for e in tempPath if e != ""]
  return addFileFromPathHelper(newPath, parent ,file)

def addFileFromPathHelper(modPath, parent, file):
  
  if len(modPath) == 0:
    parent.addFile(file)
  elif len(modPath) == 1:
    parent.subDirs[modPath[0]].addFile(file)
  else:
    addFileFromPathHelper(modPath[1:], parent.subDirs[modPath[0]], file)


#construct
rootDir = Dir("/")
path = "/"
for command in data[1:]: # we ignore the first line
  if command[0] == "$":
    if command[2] == "c":
      path = cd(path, command[5:]) # assume it exists already
    else:
      pass # for ls we wait
  else:
    tempCommand = command.split(" ")
    if tempCommand[0] == "dir":

      addDirFromPath(path, rootDir, Dir(tempCommand[1]))
    else:
      addFileFromPath(path, rootDir, File(tempCommand[1], int(tempCommand[0])))


print(rootDir.getSize())

def sizeLTN(dir, n):
  total = 0
  size = dir.getSize()
  if size <= n:
    total += size
  
  for e in dir.subDirs:
    total += sizeLTN(dir.subDirs[e], n)
  
  return total

print(sizeLTN(rootDir, 100000))

# finds the size of the smallest directory, >= than n
def findSmallest(dir, n):
  minSize = dir.getSize()
  if minSize < n:
    minSize = 100000000000 # really big :O
  
  for e in dir.subDirs:
    minSize = min(findSmallest(dir.subDirs[e], n), minSize)

  return minSize

print(findSmallest(rootDir, 30000000 - (70000000 - rootDir.getSize())))