
x1 = float(input("enter the number 1>>"))
d = input("enter operation >>")
x2 = float(input("enter the number 2>>"))
if d == "+":
    res = x1 + x2
    print("there is a result:", res)

if d == "-":
    res = x1 - x2
    print("there is a result:", res)

if d == "*":
    res = x1 * x2
    print("there is a result:", res)

if d == "/" and bool(x2):
    res = x1 / x2
    print("there is a result:", res)
if d == "/" and not bool(x2):
     print("you can not divide by zero")
else:
    print("there is no such action")
