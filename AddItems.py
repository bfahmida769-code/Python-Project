items=["Rose","Tulip","Daisy","Sunflower","Lily","Orchid","Marigold","Lavender","Jasmine","Peony","Chrysanthemum","Carnation","Daffodil","Iris","Hibiscus","Begonia","Azalea","Camellia","Gardenia","Freesia"]
items=[item.lower().strip() for item in items]
user_input=input("Add new flower to the list:").lower().strip()
if user_input in items:
        print(f"'{user_input}' is already in the list.")
else:
        print(f"'{user_input}' is not in the list. Adding it now.")
        items.append(user_input.lower().strip())
print("\nUpdated flower list:")
print(items)