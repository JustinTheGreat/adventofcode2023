import re
with open("test.txt", "r") as file:
    f = file.readlines()
count = 0
digits = ["one","two","three","four","five","six","seven","eight","nine"]
def find_min_index(lst):
    if lst:
        min_value = min(lst)
        min_index = lst.index(min_value)
        return min_index
    else:
        return None
def find_max_index(lst):
    if lst:
        max_value = max(lst)
        max_index = lst.index(max_value)
        return max_index
    else:
        return None
for line in f:
    tempPositionList = []
    tempNumberList = []
    for x in digits:
        tempInfo = re.search(x,line)
        if tempInfo:
            tempPositionList.append(tempInfo.start())
            tempNumberList.append(tempInfo.group())
    maxIndex = find_min_index(tempPositionList)
    minIndex = find_max_index(tempPositionList)
    print (tempPositionList)
    print (tempNumberList)