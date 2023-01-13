# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# def sum_odd_index(lst):
#     s = 0
#     for i in range(len(lst)):
#         if i % 2 != 0:
#             s += lst[i]
#     print(f"Сумма равна: {s}")


# lst = [2, 3, 5, 9, 3]
# sum_odd_index(lst)
# lst = list(map(int, input("Введите числа через пробел:\n").split()))
# sum_odd_index(lst)

# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# def mult_lst(lst):
#     l = len(lst)//2 + 1 if len(lst) % 2 != 0 else len(lst)//2
#     new_lst = [lst[i]*lst[len(lst)-i-1] for i in range(l)]
#     print(new_lst)


# lst = [2, 3, 4, 5, 6]
# mult_lst(lst)
# lst = list(map(int, input("Введите числа через пробел:\n").split()))
# mult_lst(lst)


# Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# lst = list(map(float, input("Введите числа через пробел:\n").split()))
# new_lst = [round(i % 1, 2) for i in lst if i % 1 != 0]
# print(max(new_lst) - min(new_lst))

# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# s = ""
# n = int(input(
#     "Введите число для преобразовывания десятичного числа в двоичное:\n"))
# while n != 0:
#     s = str(n % 2) + s
#     n //= 2
# print(s)

# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# def findFib(index):
#     if index == 1:
#         return 0
#     elif index == 2:
#         return 1
#     return findFib(index-1) + findFib(index-2)


# n = int(input(
#     "Введите число для преобразовывания десятичного числа в двоичное:\n"))
# lst = [findFib(i) for i in range(1, n+2)]
# print(lst)
# lst = lst[::-1] + lst[1:]
# print(lst, '\n')

