import sys
try:
    x = int(input("X:"))
    y = int(input("y:"))
except ValueError:
    print("Error: Invalid Input")
    sys.exit(1)
try:
    z = x/y
except:
    print("Error: can't divide by zero")
    sys.exit(1)
print(f"{x}/{y} = {z}")
