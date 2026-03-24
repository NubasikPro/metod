import math

def f(x):
    return math.log10(x) - math.cos(x)

a, b = 1.2, 1.4
eps = 0.0001

while (b - a) > eps:
    c = (a + b) / 2
    if f(a) * f(c) < 0:
        b = c
    else:
        a = c

print(f"Корень: { (a + b)/2 :.4f}")