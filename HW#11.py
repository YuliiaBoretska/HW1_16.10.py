# Модифікувати калькулятор таким чином, щоб він працював доти, доки користувач цього хоче
# Тобто, потрібно робити запит до користувача на продовження роботи калькулятора після кожного обчислення
# - якщо користувач ввів yes (можна просто y), то нове обчислення, інакше - закінчення роботи.

cont = 'y'
while cont == 'y':
    x1 = float(input("enter the number 1>>"))
    d = input("enter operation >>")
    x2 = float(input("enter the number 2>>"))
    if d == "+":
        res = x1 + x2
        print("there is a result:", res)
    elif d == "-":
        res = x1 - x2
        print("there is a result:", res)
    elif d == "*":
        res = x1 * x2
        print("there is a result:", res)
    elif d == "/" and bool(x2):
        res = x1 / x2
        print("there is a result:", res)
    elif d == "/" and not bool(x2):
        print("you can not divide by zero")
    else:
        print("there is no such action")
    cont = input("Wenn Sie weitermachen möchten, drüken Sie \"у\" wenn nein drüken etwas anderes ")
print("Auf Wiedersehen")
