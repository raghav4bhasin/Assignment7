MyDict = {}

for x in range (1, 8):
    key = x
    val = input("Enter Value {}: ".format(x))
    MyDict[key] = val
    
print(" ")
print("Dictionary: ", MyDict)
