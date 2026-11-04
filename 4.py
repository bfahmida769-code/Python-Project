numbers=[4,7,2,7,9,7,1]
target=7
positions=[]

for index in range(len(numbers)):
    if numbers[index]==target:
        positions.append(index)

first_position=-1
for index in range(len(numbers)):
    if numbers[index]==target:
        first_position=index
        break
print("Target: ",target)
print("Positions: ",positions)
print("Number of occurrences: ",len(positions))

if first_position==-1:
    print("First occurrence: not found")
else:
    print("First occurrences:",first_position)
