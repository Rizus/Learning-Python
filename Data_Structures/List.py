"""
Список создается в Python путем размещения элементов внутри [], разделенных запятыми.
В списке может быть любое количество элементов, и они могут быть разных типов (целые числа, числа с плавающей запятой, строки и т. д.).
Каждый элемент в списке(List) имеет свой индекс. Первый элемент в Списке(List) начинается с индекса 0. [0, 1, 2,...]
Мы можем обращаться к элементам Списка(List) по индексу и управлять ими.
Если обратиться к не существующему индексу, мы получим ошибку: IndexError: list index out of range
Python допускает отрицательное индексирование своих последовательностей. Индекс -1 относится к последнему элементу, -2 к предпоследнему элементу и так далее.

"""

# A list with 3 integers
numbers = [1, 5, 3, 4]
print(numbers)
# Output: [1, 5, 3, 4]

# empty list
my_list = []
print(my_list)
# Output: []

# list with mixed data types
my_list = [1, "Hello", 3.4]
print(my_list)
# Output: [1, 'Hello', 3.4]

# list with type str
currencies = ['Dollar', 'Euro', 'Pound']
print(currencies)
# Output: ['Dollar', 'Euro', 'Pound']

# calling a list item by index
print(currencies[2])
# Output: Pound

# print(currencies[5])
# IndexError: list index out of range

# access item at index 0
languages = ["Python", "Swift", "C++"]
print(languages[-1])
# Output: C++

# Slicing of a Python List
my_list = ['p', 'r', 'o', 'g', 'r', 'a', 'm', 'm', 'i', 'z']
# items from index 2 to index 4
print(my_list[2:5])
# Output: ['o', 'g', 'r']

# items from index 5 to end
print(my_list[5:])
# Output: ['a', 'm', 'm', 'i', 'z']

# items beginning to end
print(my_list[:])
# Output: ['p', 'r', 'o', 'g', 'r', 'a', 'm', 'm', 'i', 'z']


#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>#
# Метод append() добавляет элемент в конец Cписка(List) > Эквивалентно a[len(a):] = [x]
my_list = [1, 2, 3, 4, 5, 6]
my_list[len(my_list):] = [5]
print(my_list)
# Output: [1, 2, 3, 4, 5, 6, 5]

# append 'Yen' to the list
currencies.append('Yen')
print(currencies)
# Output: ['Dollar', 'Euro', 'Pound', 'Yen']


# Метод extend() добавляет все элементы одного списка в другой > Эквивалентно a[len(a):] = iterable
prime_num = [2, 3, 5]
even_num = [4, 6, 8]
prime_num[len(prime_num):] = even_num
print(prime_num)
# Output: [2, 3, 5, 4, 6, 8]

# join two lists
prime_num.extend(even_num)
print("List after extend: ", prime_num)
# Output: [2, 3, 5, 4, 6, 8]