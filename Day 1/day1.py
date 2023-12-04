import re
with open("day1input.txt", "r") as file:
    f = file.readlines()
count = 0
for line in f:
    numbers = re.findall(r"\d",line)
    first = numbers[0]if numbers else None
    last = numbers[-1] if numbers else None
    count += ((int(first)*10) + int(last))
    #Second method (not used) 
    tempSearch = re.search(r"\d",line)
    temp = tempSearch.group()
print (count)