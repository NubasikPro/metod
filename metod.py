import math

# функция
def f(x):
    return 10 - 0.5*x**2 - 2**(-x)

# производная для метода Ньютона
def df(x):
    return -x + (2**(-x))*math.log(2)

# ==============================
# 1. Метод половинного деления
# ==============================
def bisection(a, b, eps=1e-3):
    while (b - a)/2 > eps:
        c = (a + b)/2
        if f(a)*f(c) <= 0:
            b = c
        else:
            a = c
    return (a + b)/2

# ==============================
# 2. Метод итераций
# x = sqrt(20 - 2*2^(-x))
# ==============================
def phi(x):
    return math.sqrt(20 - 2*(2**(-x)))

def simple_iteration(x0, eps=1e-3):
    x1 = phi(x0)
    while abs(x1 - x0) > eps:
        x0 = x1
        x1 = phi(x0)
    return x1

# ==============================
# 3. Метод хорд
# ==============================
def secant(x0, x1, eps=1e-3):
    while abs(x1 - x0) > eps:
        x2 = x1 - f(x1)*(x1 - x0)/(f(x1) - f(x0))
        x0, x1 = x1, x2
    return x1

# ==============================
# 4. Метод Ньютона
# ==============================
def newton(x0, eps=1e-3):
    x1 = x0 - f(x0)/df(x0)
    while abs(x1 - x0) > eps:
        x0 = x1
        x1 = x0 - f(x0)/df(x0)
    return x1


# ==============================
# Запуск программы
# ==============================

print("Метод половинного деления:", bisection(4, 5))
print("Метод итераций:", simple_iteration(4.5))
print("Метод хорд:", secant(4, 5))
print("Метод Ньютона:", newton(4.5))