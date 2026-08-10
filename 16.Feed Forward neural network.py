x1 = int(input("Enter Input 1 (0/1): "))
x2 = int(input("Enter Input 2 (0/1): "))

w1 = 1
w2 = 1
threshold = 1

output = x1 * w1 + x2 * w2

if output >= threshold:
    print("Output: 1")
else:
    print("Output: 0")
