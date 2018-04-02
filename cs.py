a = (5 ** 100) - 1
b = (5 ** 120) - 1
while a != 0 and b != 0:
    if a > b:
        a = a % b
    else:
        b = b % a

print(a + b)