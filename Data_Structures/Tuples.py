"""

Кортеж(Tuple) создается в Python путем размещения элементов внутри (), разделенных запятыми.
Кортеж(Tuple) в Python похож на Список(List). Разница между ними заключается в том,
что мы не можем изменить элементы Кортежа(Tuple) после его назначения, тогда как мы можем изменить элементы Списка(List).
Для создания Кортежа(Tuple) с одним элементом, обязательно необходима запятая в конце.

"""

# Different types of tuples
# empty tuple
my_tuple = ()  # or my_tuple = tuple()
print(my_tuple)
# Output: ()

# create a tuple with one element
my_tuple = (1,)
print(my_tuple)
# Output: (1,)

# tuple having integers
my_tuple = (1, 2, 3)
print(my_tuple)
# Output: (1, 2, 3)

# tuple with mixed datatypes
my_tuple = (1, "Hello", 3.4)
print(my_tuple)
# Output: (1, 'Hello', 3.4)

#  nested tuple
my_tuple = ("mouse", [8, 4, 6], (1, 2, 3))
print(my_tuple)
# Output: ('mouse', [8, 4, 6], (1, 2, 3))

# accessing tuple elements using indexing
letters = ("p", "r", "o", "g", "r", "a", "m", "i", "z")
print(letters[0])
# Output: p

print(letters[-5])
# Output: r

# accessing tuple elements using slicing
my_tuple = ('p', 'r', 'o', 'g', 'r', 'a', 'm', 'i', 'z')

# elements 2nd to 4th index
print(my_tuple[1:4])
# Output: ('r', 'o', 'g')

# elements beginning to 2nd
print(my_tuple[:-7])
# Output: ('p', 'r')

# elements 8th to end
print(my_tuple[7:])
# Output: ('i', 'z')

# elements beginning to end
print(my_tuple[:])
# Output: ('p', 'r', 'o', 'g', 'r', 'a', 'm', 'i', 'z')

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>#

# Методы кортежей Python. Доступны только следующие два метода.
my_tuple = ('a', 'p', 'p', 'l', 'e',)
print(my_tuple.count('p'))
# Output: 2
print(my_tuple.index('l'))
# Output: 3

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>#

# Мы можем использовать цикл for для перебора элементов кортежа.
languages = ('Python', 'Swift', 'C++')
# iterating through the tuple
for language in languages:
    print(language)
    # Output: Python
    # Output: Swift
    # Output: C++

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>#

# Мы можем проверить существует ли элемент в кортеже или нет
print('C' in languages)
# Output: False
print('Python' in languages)
# Output: True
print('Ruby' not in languages)
# Output: True
