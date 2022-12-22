data = []

with open("python/Day 06/test.txt") as f:
    data = f.readlines()


for i in range(len(data)):
    if ("\n" in data[i]):
        data[i] = data[i][:-1] # remove \n
    

# checks for same letters
def unique(text):
    for i in range(len(text)): # 0 1 2 3 
        for j in range(len(text) - i - 1): # j = 0 1 2 3 - 
            if text[i] == text[j + i + 1]: # i compared to i + 1 + j
                return False
    
    return True

def findMarker(text, n):
    for i in range(len(text) - n):
        if unique(text[i:i+n]):
            return i + n
    

print(findMarker(data[0], 4))
print(findMarker(data[0], 14))