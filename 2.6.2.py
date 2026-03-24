import math

def f(x):
    return x*x - 3.2*x - 1

x = 3.5  
eps = 0.0001

while True:
    x_next = math.sqrt(3.2*x + 1)
    if abs(x_next - x) < eps:
        break
    x = x_next

print(f"Корень: {x:.4f}") 