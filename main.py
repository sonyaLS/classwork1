from calculator import *
from calculator1 import *
print('Привет! Этот калькулятор ты можешь использовать для сложения, вычитания, деления и умножения.')

while True:
    op = input("Введи операцию (сложение, вычитание, деление и умножение) или 'стоп' для остановки: ")
    if op == 'стоп':
        break
    a = int(input("Введи первое число: "))
    b = int(input("Введи второе число: "))
    if op == 'сложение':
        print(summ(a, b))
    elif op == 'вычитание':
        print(diff(a, b))
    elif op == 'деление':
        print(delenie(a, b))
    elif op == 'умножение':
        print(umnogenie(a, b))


