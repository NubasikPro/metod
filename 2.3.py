import math

def f(x):
    return x * math.sin(x) - 1

def phi(x):
    return 1 / math.sin(x)

print("введите x, eps, q")
x = float(input("x = "))
eps = float(input("eps = "))
q = float(input("q = "))

a = eps * (1 - q) / q

n = 0
while True:
    y = phi(x)
    p = x - y
    x = y
    n += 1
    if abs(p) <= a:
        break

print(f"x = {x:.6e}")
print(f"n = {n}")