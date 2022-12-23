a = float(input("Enter first side of triangle "))
b = float(input("Enter second side of triangle "))
c = float(input("Enter third side of triangle "))
if a+b>c and b+c>a and a+c>b:
    print("Yes")

else:
    print("No")
