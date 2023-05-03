"""

Список создается в Python путем размещения элементов внутри [], разделенных запятыми.
В списке может быть любое количество элементов, и они могут быть разных типов (целые числа, числа с плавающей запятой, строки и т. д.).
Каждый элемент в списке(List) имеет свой индекс. Первый элемент в Списке(List) начинается с индекса 0. [0, 1, 2,...]
Мы можем обращаться к элементам Списка(List) по индексу и управлять ими.
Если обратиться к не существующему индексу, мы получим ошибку: IndexError: list index out of range
Python допускает отрицательное индексирование своих последовательностей. Индекс -1 относится к последнему элементу, -2 к предпоследнему элементу и так далее.
!~Списки Python изменяемы. Списки значений могут быть изменены. И мы можем изменить элементы списка, назначив новые значения, используя = оператор.

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

# сalling the missing index
try:
    print(currencies[5])
except IndexError:
    print("IndexError: list index out of range")
# Output: IndexError: list index out of range

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

# Метод append(x) добавляет элемент в конец Cписка(List) > Эквивалентно a[len(a):] = [x]
my_list = [1, 2, 3, 4, 5, 6]
my_list[len(my_list):] = [5]
print(my_list)
# Output: [1, 2, 3, 4, 5, 6, 5]

# append 'Yen' to the list
currencies.append('Yen')
print(currencies)
# Output: ['Dollar', 'Euro', 'Pound', 'Yen']

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>#

# Метод extend(iterable) добавляет все элементы одного списка в другой > Эквивалентно a[len(a):] = iterable
prime_num = [2, 3, 5]
even_num = [4, 6, 8]
prime_num[len(prime_num):] = even_num
print(prime_num)
# Output: [2, 3, 5, 4, 6, 8]

# join two lists
prime_num.extend(even_num)
print("List after extend: ", prime_num)
# Output: [2, 3, 5, 4, 6, 8]

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>#

# Important: The list is mutable
languages = ['Python', 'Sift', 'C++']
# changing the third item to 'C'
languages[2] = 'C'
print(languages)
# Output: ['Python', 'Sift', 'C']

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>#

# Удалить элемент из списка
# 1. Using del
languages = ['Python', 'Swift', 'C++', 'C', 'Java', 'Rust', 'R']
print(languages)
# Output: ['Python', 'Swift', 'C++', 'C', 'Java', 'Rust', 'R']

# deleting the second item
del languages[1]
print(languages)
# Output: ['Python', 'C++', 'C', 'Java', 'Rust', 'R']

# deleting the last item
del languages[-1]
print(languages)
# Output: ['Python', 'C++', 'C', 'Java', 'Rust']

# deleting first two items
del languages[0:2]
print(languages)
# Output: ['C', 'Java', 'Rust']

# 2. Using remove(x)
languages = ['Python', 'Swift', 'C++', 'C', 'Java', 'Rust', 'R']

# remove 'Python' from the list
languages.remove('Python')

print(languages)
# Output: ['Swift', 'C++', 'C', 'Java', 'Rust', 'R']

# remove 'Ruby' from the list
try:
    languages.remove('Ruby')
except ValueError:
    print("ValueError: list.remove(x): x not in list")
else:
    print(languages)
# Output: ValueError: list.remove(x): x not in list

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>#

# Метод insert(i, x) вставляет элемент в список по указанному индексу
# create a list of vowels
vowel = ['a', 'e', 'i', 'u']
# 'o' is inserted at index 3 (4th position)
vowel.insert(3, 'o')
print('List:', vowel)
# Output: List: ['a', 'e', 'i', 'o', 'u']

# one more example
# a.insert(len(a), x) is equivalent to a.append(x)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>#

# Метод pop([x]) удаляет элемент с заданным индексом из списка и возвращает удаленный элемент
# Аргумент - необязателен. По умолчанию -1 (индекс последнего элемента)

# create a list of prime numbers
prime_numbers = [2, 3, 5, 7]

# remove the element at index 2
removed_element = prime_numbers.pop(2)
print('Removed Element:', removed_element)
print('Updated List:', prime_numbers)
# Output:
# Removed Element: 5
# Updated List: [2, 3, 7]

# Если индекс, переданный методу, не находится в диапазоне, он выдает IndexError: pop index out of range
try:
    removed_element = prime_numbers.pop(5)
except IndexError:
    print("IndexError: pop index out of range")
# Output: IndexError: pop index out of range

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>#

# Метод clear() удаляет все элементы из списка

prime_numbers = [2, 3, 5, 7, 9, 11]
print(prime_numbers)
# remove all elements
prime_numbers.clear()
# Updated prime_numbers List
print('List after clear():', prime_numbers)
# Output: List after clear(): []

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>#

# Метод index(x[, start[, end]]) возвращает индекс указанного элемента в списке

animals = ['cat', 'dog', 'rabbit', 'horse']
# get the index of 'dog'
index = animals.index('dog')
print(index)
# Output: 1

# Если переданный индекс отсутствует он выдает ошибку ValueError: 'x' is not in list
# vowels list
vowels = ['a', 'e', 'i', 'o', 'u']
# index of 'p' is vowels
try:
    index = vowels.index('p')
except ValueError:
    print("ValueError: 'p' is not in list")
# Output: ValueError: 'p' is not in list

# Работа index() с параметрами Start и End
# alphabets list
alphabets = ['a', 'e', 'i', 'o', 'g', 'l', 'i', 'u']

# index of 'i' in alphabets
index = alphabets.index('e')
print('The index of e:', index)
# Output: The index of e: 1

# 'i' after the 4th index is searched
index = alphabets.index('i', 4)
print('The index of i:', index)
# Output: The index of e: 6

# 'i' between 3rd and 5th index is searched
try:
    index = alphabets.index('i', 3, 5)
except ValueError:
    print("ValueError: 'i' is not in list")
# Output: ValueError: 'i' is not in list

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>#

# Метод count(x) возвращает количество раз, когда указанный элемент появляется в списке

# create a list
numbers = [2, 3, 5, 2, 11, 2, 7]
# check the count of 2
count = numbers.count(2)
print('Count of 2:', count)
# Output: Count of 2: 3

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>#

# Метод sort(*, key=None, reverse=False) сортирует элементы списка в порядке возрастания или убывания
#Примечание. Самое простое различие между sort()и sorted()является:
# sort()изменяет список напрямую и не возвращает никакого значения, а sorted()не изменяет список и возвращает отсортированный список.

prime_numbers = [11, 3, 7, 5, 2]
# sorting the list in ascending order
prime_numbers.sort()
print(prime_numbers)
# Output: [2, 3, 5, 7, 11]

#Сортировка списка по ключу
# take second element for sort
def takeSecond(elem):
    return elem[1]

# random list
random = [(2, 2), (3, 4), (4, 1), (1, 3)]
# sort list with key
random.sort(key=takeSecond)
# print list
print('Sorted list:', random)
# Output: Sorted list: [(4, 1), (2, 2), (1, 3), (3, 4)]

# Сортировка списка по ключу
# sorting using custom key
employees = [
    {'Name': 'Alan Turing', 'age': 25, 'salary': 10000},
    {'Name': 'Sharon Lin', 'age': 30, 'salary': 8000},
    {'Name': 'John Hopkins', 'age': 18, 'salary': 1000},
    {'Name': 'Mikhail Tal', 'age': 40, 'salary': 15000},
]

# custom functions to get employee info
def get_name(employee):
    return employee.get('Name')


def get_age(employee):
    return employee.get('age')


def get_salary(employee):
    return employee.get('salary')


# sort by name (Ascending order)
employees.sort(key=get_name)
print(employees, end='\n\n')

# sort by Age (Ascending order)
employees.sort(key=get_age)
print(employees, end='\n\n')

# sort by salary (Descending order)
employees.sort(key=get_salary, reverse=True)
print(employees, end='\n\n')

# Хорошей практикой является использование лямбда-функции, когда функция может быть описана в одной строке
# sorting using custom key
employees = [
    {'Name': 'Alan Turing', 'age': 25, 'salary': 10000},
    {'Name': 'Sharon Lin', 'age': 30, 'salary': 8000},
    {'Name': 'John Hopkins', 'age': 18, 'salary': 1000},
    {'Name': 'Mikhail Tal', 'age': 40, 'salary': 15000},
]

# sort by name (Ascending order)
employees.sort(key=lambda x: x.get('Name'))
print(employees, end='\n\n')

# sort by Age (Ascending order)
employees.sort(key=lambda x: x.get('age'))
print(employees, end='\n\n')

# sort by salary (Descending order)
employees.sort(key=lambda x: x.get('salary'), reverse=True)
print(employees, end='\n\n')

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>#

# Метод reverse() переворачивает элементы списка

# create a list of prime numbers
prime_numbers = [2, 3, 5, 7]
# reverse the order of list elements
prime_numbers.reverse()
print('Reversed List:', prime_numbers)
# Output: Reversed List: [7, 5, 3, 2]

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>#

# Метод copy() возвращает неглубокую копию списка
# Метод возвращает новый список. Он не изменяет исходный список

# mixed list
prime_numbers = [2, 3, 5]
# copying a list
numbers = prime_numbers.copy()
print('Copied List:', numbers)
# Output: Copied List: [2, 3, 5]