# * Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N

# num_n = int(input('Enter the number of elements: '))


# lst_fact = []

# for i in range(num_n):
#     if i:
#         new_el = 1

#         for j in range(i + 1):
#             new_el *= j + 1

#         lst_fact.append(new_el)
#     else:
#         lst_fact.append(i + 1)
# print(*lst_fact)

# * Требуется найти наименьший натуральный делитель целого числа N, отличный от 1

# num_n = int(input('Enter the number: '))

# i = 1

# while i <= abs(num_n):
#     i = i + 1

#     if not num_n % i:
#         break
# else:
#     i = abs(num_n)

# print(f'The smallest divisor for {num_n} is {i}')

# num_n = int(input('Enter the number: '))

# lst_nums = list(range(-abs(num_n), abs(num_n) + 1))

# if num_n < 0:
#     lst_nums.reverse()

# number_els = 5
# lst_i = [randint(0, len(lst_nums) - 1) for _ in range(number_els)]

# print('Generated list:', lst_nums, sep='\n', end='\n\n')
# print('Indexes for multiplication:', lst_i, sep='\n', end='\n\n')

# result = 1

# for indx in lst_i:
#     result *= lst_nums[indx]

# print(f'Result: {result}')

# * Требуется посчитать сумму чётных чисел, расположенных между числами 1 и N включительно

# num_n = int(input('Enter the number: '))

# lst_nums = list(range(0, num_n + 1, 2))

# print('Sum of even numbers:', sum(lst_nums))