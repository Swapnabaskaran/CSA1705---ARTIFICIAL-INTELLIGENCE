a = int(input("Enter capacity of Jug1: "))
b = int(input("Enter capacity of Jug2: "))
target = int(input("Enter target amount: "))

x = 0
y = 0

print("(0,0)")

while x != target and y != target:
    if x == 0:
        x = a
    elif y == b:
        y = 0
    else:
        t = min(x, b - y)
        x -= t
        y += t
    print((x, y))
