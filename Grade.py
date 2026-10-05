while True:
    x=input("Enter your marks: ")

    if x.isdigit(): #Checks if input is integer
        x=int(x)
        break
    else:
        print("Not an integer! Enter again.")

#Grade Check
if 97<=x<=100:
    print("Grade is A+")
elif 93<=x<=96:
    print("Grade is A")
elif 90<=x<=92:
    print("Grade is A-")
elif 87<=x<=89:
    print("Grade is B+")
elif 83<=x<86:
    print("Grade is B")
elif 80<=x<82:
    print("Grade is B-")
elif 77<=x<79:
    print("Grade is C+")
elif 73<=x<76:
    print("Grade is C")
elif 70<=x<72:
    print("Grade is C-")
elif 67<=x<69:
    print("Grade is D+")
elif 63<=x<66:
    print("Grade is D")    
elif 60<=x<62:
    print("Grade is D-")
elif x<60:
    print("Grade is F")         

else:
    print("Invalid marks! Marks should be between 0 and 100.")