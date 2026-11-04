items=[]

while True:
    print("\n1. Add an item")
    print("2. Remove an item")
    print("3. Display the list")
    print("4. Quit")

    choice=input("Enter your choice: ")

    if choice=="1":
        item=input("Enter an iteam: ")
        items.append(item)
        print(item,"added")

    elif choice=="2":
        item=input("Enter the item to remove: ")
        if item in items:
            items.remove(item)
            print(item,"removed")
        else:
            print("Item not found")

    elif choice=="3":
        print("Current list: ",items)

    elif choice=="4":
        print("Program ended")
        break

    else:
       print("Invalid choice")
