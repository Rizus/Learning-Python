"""

Множества(Set) — это набор уникальных данных. То есть элементы набора не могут повторяться.
В Python мы создаем Множества(Set), помещая все элементы в фигурные скобки {}, разделенные запятой.
В наборе может быть любое количество элементов, и они могут быть разных типов (целые числа, числа с плавающей запятой, Кортежи(tuple), строки и т. д.).
Но множество(Set) не может иметь в качестве своих элементов изменяемые элементы, такие как Списки(List), Множества(Set) или Словари(Dictionary).
Множества(Set) — это набор уникальных данных. То есть элементы набора не могут повторяться.
Множества(Set) не имеет определенного порядка.

"""

# create an empty set
empty_set = set()
print(type(empty_set))
# Output: <class 'set'>

# create an empty dictionary
empty_dictionary = {}
print(type(empty_dictionary))
# Output: <class 'dict'>

# В наборе нет повторяющихся элементов, поскольку Множества(Set) не может содержать дубликатов
numbers = {2, 4, 6, 6, 2, 8}
print(numbers)
# Output: {8, 2, 4, 6}

# create a set of integer type
student_id = {112, 114, 116, 118, 115}
print('Student ID:', student_id)
# Output: Student ID: {112, 114, 115, 116, 118}

# create a set of string type
vowel_letters = {'a', 'e', 'i', 'o', 'u'}
print('Vowel Letters:', vowel_letters)
# Output: Vowel Letters: {'o', 'e', 'a', 'u', 'i'}

# create a set of mixed data types
mixed_set = {'Hello', 101, -2, 'Bye'}
print('Set of mixed data types:', mixed_set)
# Output: Set of mixed data types: {'Hello', 'Bye', 101, -2}

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>#

# Добавить элементы в Множества(Set)
numbers = {21, 34, 54, 12}
print('Initial Set:', numbers)
# Output: Initial Set: {34, 12, 21, 54}

# using add() method
numbers.add(32)
print('Updated Set:', numbers)
# Output: Updated Set: {32, 34, 12, 21, 54}

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>#

# Обновить Множества(Set)
companies = {'Lacoste', 'Ralph Lauren'}
tech_companies = ['apple', 'google', 'apple']
companies.update(tech_companies)
print(companies)
# Output: {'Lacoste', 'google', 'apple', 'Ralph Lauren'}

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>#

# Удалить элемент из Множества(Set)
languages = {'Swift', 'Java', 'Python'}
print('Initial Set:', languages)
# Output: Initial Set: {'Java', 'Python', 'Swift'}

# remove 'Java' from a set
removedValue = languages.discard('Java')
print('Set after remove():', languages)
# Output: Set after remove(): {'Python', 'Swift'}

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>#

# Встроенные функции с Множеством(Set)
"""
all()         - Returns True if all elements of the set are true (or if the set is empty) ~> https://www.programiz.com/python-programming/methods/built-in/all
any()         - Returns True if any element of the set is true. If the set is empty, returns False ~> https://www.programiz.com/python-programming/methods/built-in/any
enumerate()   - Returns an enumerate object. It contains the index and value for all the items of the set as a pair ~> https://www.programiz.com/python-programming/methods/built-in/enumerate
len()         - Returns the length (the number of items) in the set ~> https://www.programiz.com/python-programming/methods/built-in/len
max()         - Returns the largest item in the set ~> https://www.programiz.com/python-programming/methods/built-in/max
min()         - Returns the smallest item in the set ~> https://www.programiz.com/python-programming/methods/built-in/min
sorted()      - Returns a new sorted list from elements in the set(does not sort the set itself) ~> https://www.programiz.com/python-programming/methods/built-in/sorted
sum()         - Returns the sum of all elements in the set ~> https://www.programiz.com/python-programming/methods/built-in/sum
"""

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>#

# Итерация по Множеству(Set)
fruits = {"Apple", "Peach", "Mango"}

# for loop to access each fruits
for fruit in fruits:
    print(fruit)
    # Output: Peach
    # Output: Apple
    # Output: Mango

    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>#

# Союз двух Множеств(Set)
# Мы используем | оператор или union() метод для выполнения операции set union
# first set
A = {1, 3, 5}
# second set
B = {0, 2, 4}
# perform union operation using |
print('Union using |:', A | B)
# Output: Union using |: {0, 1, 2, 3, 4, 5}

# perform union operation using union()
print('Union using union():', A.union(B))
# Output: Union using union(): {0, 1, 2, 3, 4, 5}

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>#

# Установить пересечение
# Мы используем & оператор или intersection() метод для выполнения заданной операции пересечения
# first set
A = {1, 3, 5}
# second set
B = {1, 2, 3}
# perform intersection operation using &
print('Intersection using &:', A & B)
# Output: Intersection using &: {1, 3}

# perform intersection operation using intersection()
print('Intersection using intersection():', A.intersection(B))
# Output: Intersection using intersection(): {1, 3}

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>#

# Разница между двумя Множествами(Set)
# Мы используем - оператор или difference() метод для выполнения разницы между двумя наборами
# first set
A = {2, 3, 5}
# second set
B = {1, 2, 6}
# perform difference operation using &
print('Difference using &:', A - B)
# Output: Difference using &: {3, 5}

# perform difference operation using difference()
print('Difference using difference():', A.difference(B))
# Output: Difference using difference(): {3, 5}

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>#

# Установить симметричную разницу
# Мы используем ^ оператор или symmetric_difference() метод для выполнения симметричной разницы между двумя наборами
# first set
A = {2, 3, 5}
# second set
B = {1, 2, 6}

# perform difference operation using &
print('using ^:', A ^ B)
# Output: using ^: {1, 3, 5, 6}

# using symmetric_difference()
print('using symmetric_difference():', A.symmetric_difference(B))
# Output: using symmetric_difference(): {1, 3, 5, 6}

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>#

# Проверить, равны ли два множества
# Мы можем использовать == оператор, чтобы проверить, равны ли два Множества(Set) или нет
# first set
A = {1, 3, 5}
# second set
B = {3, 5, 1}
# perform difference operation using &
if A == B:
    print('Set A and Set B are equal')
else:
    print('Set A and Set B are not equal')
    # Output: Set A and Set B are equal

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>#

# Другие методы Множества(Set)
"""
add()                           - Adds an element to the set ~> https://www.programiz.com/python-programming/methods/set/add
clear()                         - Removes all elements from the set ~> https://www.programiz.com/python-programming/methods/set/clear
copy()                          - Returns a copy of the set ~> https://www.programiz.com/python-programming/methods/set/copy
difference()                    - Returns the difference of two or more sets as a new set ~> https://www.programiz.com/python-programming/methods/set/difference
difference_update()             - Removes all elements of another set from this set ~> https://www.programiz.com/python-programming/methods/set/difference_update
discard()                       - Removes an element from the set if it is a member. (Do nothing if the element is not in set) ~> https://www.programiz.com/python-programming/methods/set/discard
intersection()                  - Returns the intersection of two sets as a new set ~> https://www.programiz.com/python-programming/methods/set/intersection
intersection_update()           - Updates the set with the intersection of itself and another ~> https://www.programiz.com/python-programming/methods/set/intersection_update
isdisjoint()                    - Returns True if two sets have a null intersection ~> https://www.programiz.com/python-programming/methods/set/isdisjoint
issubset()                      - Returns True if another set contains this set ~> https://www.programiz.com/python-programming/methods/set/issubset
issuperset()                    - Returns True if this set contains another set ~> https://www.programiz.com/python-programming/methods/set/issuperset
pop()                           - Removes and returns an arbitrary set element. Raises KeyError if the set is empty ~> https://www.programiz.com/python-programming/methods/set/pop
remove()                        - Removes an element from the set. If the element is not a member, raises a KeyError ~> https://www.programiz.com/python-programming/methods/set/remove
symmetric_difference()          - Returns the symmetric difference of two sets as a new set ~> https://www.programiz.com/python-programming/methods/set/symmetric_difference
symmetric_difference_update()   - Updates a set with the symmetric difference of itself and another ~> https://www.programiz.com/python-programming/methods/set/symmetric_difference_update
union()                         - Returns the union of sets in a new set ~> https://www.programiz.com/python-programming/methods/set/union
update()                        - Updates the set with the union of itself and others ~> https://www.programiz.com/python-programming/methods/set/update
"""
