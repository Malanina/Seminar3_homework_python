# Задача 16:
# Требуется вычислить, сколько раз встречается некоторое число X в массиве
# A[1..N].
# Пользователь вводит натуральное число N – количество элементов в массиве
# и число, которое необходимо проверить - X.
# Заполните массив случайными натуральными числами от 1 до N/2.
# Выведите, сколько раз X встречается в массиве.

# Ввод: 5
# Ввод: 1
# 1 2 1 2 2
# Вывод: 2

import random
N = int(input("Введите количество элементов в массиве: "))
X = int(input("Введите число, которое необходимо проверить в массиве: "))
Array = []
for i in range(N):
    Array.append(random.randint(1, N//2))
print(Array)

res = 0
for i in Array:
    if i == X:
        res += 1       
print(f"{res} раза/раз встречается число {X} в массиве")
