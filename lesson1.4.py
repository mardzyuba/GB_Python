# 4.Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

a = int(input("Введите число >>>"))
b = a % 10
a = a // 10
while a > b:
    if a % 10 > b:
        b = a % 10
        a //= 10
    else:
        print(b)
        break
