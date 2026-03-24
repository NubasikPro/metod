import math

def f(x):
    return x * math.sin(x) - 1

print("введите a, b, eps")
a = float(input("a = "))
b = float(input("b = "))
eps = float(input("eps = "))

while (b - a) > eps:
    c = (a + b) / 2
    if f(a) * f(c) < 0:
        b = c
    else:
        a = c

x = (a + b) / 2
print(f"x = {x:.6f}")