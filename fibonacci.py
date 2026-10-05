n=int(input("Enter n:"))
a=0
b=1
print("Fibonacci series:")
for i in range(0,n):
    print(a,end=" ")
    c=a+b
    a=b
    b=c