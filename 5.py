items=["pen","book","pen","bag","book","ruler","pen"]

unique_items=[]
repeated_items=[]

for item in items:
    if item in unique_items:
        repeated_items.append(item)
    else:
        unique_items.append(item)

print("Unique items: ",unique_items)
print("Repeated occurrences:",repeated_items)
