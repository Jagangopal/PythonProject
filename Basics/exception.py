x=input("Enter Number 1: ")
y=input("Enter Number 2: ")
try:
    z=int(x)/int(y)
except ZeroDivisionError as e:
    print("Division By Zero")
    z=None
except TypeError as e:
    print("Type Error Exception")
    z=None
print("Division is ",z)