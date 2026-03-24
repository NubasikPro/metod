import math

def f(x):
    return 4*x - 3*math.log(x) - 4

x = 3.5
eps = 0.0001

while True:
    x_next = 1 + 0.75 * math.log(x)
    if abs(x_next - x) < eps:
        break
    x = x_next

print(f"Корень: {x:.4f}")  