import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**3 + 3*x**2 - 24*x + 1

def f_prime(x):
    return 3*x**2 + 6*x - 24

def chord_method(f, a, b, tol=1e-6):
    """Метод хорд"""
    while abs(b - a) > tol:
        c = a - f(a) * (b - a) / (f(b) - f(a))
        if f(a) * f(c) <= 0:
            b = c
        else:
            a = c
    return (a + b) / 2

def tangent_method(f, f_prime, x0, tol=1e-6, max_iter=100):
    """Метод касательных (Ньютона)"""
    for _ in range(max_iter):
        x1 = x0 - f(x0) / f_prime(x0)
        if abs(x1 - x0) < tol:
            return x1
        x0 = x1
    return x0

def combined_method(f, f_prime, a, b, tol=1e-6):
    """Комбинированный метод хорд и касательных"""
    while abs(b - a) > tol:
        x_chord = a - f(a) * (b - a) / (f(b) - f(a))
        x_tangent = b - f(b) / f_prime(b)
        if f(a) * f(x_chord) <= 0:
            b = x_tangent
            a = x_chord
        else:
            a = x_tangent
            b = x_chord
    return (a + b) / 2

# Решение уравнения
a, b = 0, 1
tol = 1e-6

print("=" * 50)
print("Решение уравнения x^3 + 3x^2 - 24x + 1 = 0 на [0, 1]")
print("=" * 50)

root_chord = chord_method(f, a, b, tol)
print(f"Метод хорд:          x = {root_chord:.10f}")

root_tangent = tangent_method(f, f_prime, 0.5, tol)
print(f"Метод касательных:   x = {root_tangent:.10f}")

root_combined = combined_method(f, f_prime, a, b, tol)
print(f"Комбинированный метод: x = {root_combined:.10f}")

# Проверка
print(f"\nПроверка: f({root_combined:.10f}) = {f(root_combined):.2e}")
