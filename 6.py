numbers=[14,8,21,21,5,17,14]
Largest=None
Second_Largest=None

for number in numbers:
    if Largest is None or number>Largest:
        if number!=Largest:
            Second_Largest=Largest
            Largest=number
    elif number!=Largest and(
        Second_Largest is None or number>Second_Largest
    ):

        Second_Largest=number
        
if Second_Largest is None:
    print("Fewer than two distinct values")
else:
    print("Largest distinct value:",Largest)
    print("Second largest distinct value:",Second_Largest)

