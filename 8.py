items=["Notebook","Pen","calculator","Folder"]
prices=[120.0,15.0,850.0,80.0]
quantities=[2,5,1,3]

subtotal=0

for index in range(len(items)):
    line_total=prices[index]*quantities[index]
    subtotal +=line_total
    print(f"{items[index]}:TK{line_total: .2f}")

if subtotal>=1000:
    discount_rate=0.10
elif subtotal>=500:
    discount_rate=0.05
else:
    discount_rate=0

discount=subtotal*discount_rate
after_discount=subtotal-discount

if after_discount>=1000:
      delivery=0
else:
     delivery=60

final_total=after_discount+delivery

print(f"Subtotal:TK{subtotal: .2f}")
print(f"Discount:TK{discount: .2f}")
print(f"Delivery:TK{delivery: .2f}")
print(f"Final Total:TK{final_total: .2f}")



