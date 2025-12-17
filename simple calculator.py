x = int(input("Enter your first number: "))
y = int(input("Enter your second number: "))
z = input("Select the operator(+,-,/,*,%) : ")


if z=="+":
    print(x+y)
elif z=="-":
    print(x-y)
elif z=="*":
    print(x*y)
elif z=="/":
    if y==0:
        print("You cannot divide by zero")
    else:
         print(x/y)
       
elif z=="%":
    print(x%y)
else:
    print("Wrong input")