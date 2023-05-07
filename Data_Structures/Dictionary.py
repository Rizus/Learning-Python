"""

Словарь(Dictionary) — это упорядоченная коллекция (начиная с Python 3.7) элементов.
Он хранит элементы в парах ключ/значение. Здесь ключи — это уникальные идентификаторы, связанные с каждым значением

"""

# Create empty dictionary
my_dict = {}
print(my_dict)
# Output: {}

# Create a dictionary
capital_city = {"Nepal": "Kathmandu", "Italy": "Rome", "England": "London"}
print(capital_city)
# Output: {'Nepal': 'Kathmandu', 'Italy': 'Rome', 'England': 'London'}

# dictionary with keys and values of different data types
numbers = {1: "One", 2: "Two", 3: "Three"}
print(numbers)
# Output: {1: 'One', 2: 'Two', 3: 'Three'}

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>#

#Добавить элементы в Словарь(Dictionary)
# Мы можем добавлять элементы в Словарь(Dictionary), используя имя словаря с помощью []
capital_city = {"Nepal": "Kathmandu", "England": "London"}
print("Initial Dictionary: ",capital_city)
# Output: Initial Dictionary:  {'Nepal': 'Kathmandu', 'England': 'London'}

capital_city["Japan"] = "Tokyo"
print("Updated Dictionary: ",capital_city)
# Output: Updated Dictionary:  {'Nepal': 'Kathmandu', 'England': 'London', 'Japan': 'Tokyo'}

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>#

# Изменить значение Словаря(Dictionary)
# Мы также можем использовать [] для изменения значения, связанного с конкретным ключом
student_id = {111: "Eric", 112: "Kyle", 113: "Butters"}
print("Initial Dictionary: ", student_id)
# Output: Initial Dictionary:  {111: 'Eric', 112: 'Kyle', 113: 'Butters'}

student_id[112] = "Stan"
print("Updated Dictionary: ", student_id)
# Output: Updated Dictionary:  {111: 'Eric', 112: 'Stan', 113: 'Butters'}

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>#

# Доступ к элементам из Словаря(Dictionary)
student_id = {111: "Eric", 112: "Kyle", 113: "Butters"}
print(student_id[111])
# Output: Eric
print(student_id[113])
# Output: Butters

student_id = {111: "Eric", 112: "Kyle", 113: "Butters"}
try:
    print(student_id[211])
except KeyError:
    print("KeyError: 211")
    # Output: KeyError: 211

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>#

# Удаление элементов из Словаря(Dictionary)
# Мы используем del Оператор для удаления элемента из Словаря(Dictionary)
student_id = {111: "Eric", 112: "Kyle", 113: "Butters"}
print("Initial Dictionary: ", student_id)
# Output: Initial Dictionary:  {111: 'Eric', 112: 'Kyle', 113: 'Butters'}

del student_id[111]

print("Updated Dictionary ", student_id)
# Output: Updated Dictionary  {112: 'Kyle', 113: 'Butters'}

# Мы также можем удалить весь словарь, используя del заявление
student_id = {111: "Eric", 112: "Kyle", 113: "Butters"}
# delete student_id dictionary
del student_id
try:
    print(student_id)
except NameError:
    print("NameError: name 'student_id' is not defined")
    # Output: NameError: name 'student_id' is not defined

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>#

# Методы Словаря(Dictionary)
"""
all()       - Return True if all keys of the dictionary are True (or if the dictionary is empty) ~> https://www.programiz.com/python-programming/methods/built-in/all
any()       - Return True if any key of the dictionary is true. If the dictionary is empty, return False ~> https://www.programiz.com/python-programming/methods/built-in/any
len()       - Return the length (the number of items) in the dictionary ~> https://www.programiz.com/python-programming/methods/built-in/len
sorted()    - Return a new sorted list of keys in the dictionary ~> https://www.programiz.com/python-programming/methods/built-in/sorted
clear()     - Removes all items from the dictionary ~> https://www.programiz.com/python-programming/methods/dictionary/clear
keys()      - Returns a new object of the dictionary's keys ~> https://www.programiz.com/python-programming/methods/dictionary/keys
values()    - Returns a new object of the dictionary's values ~> https://www.programiz.com/python-programming/methods/dictionary/values
"""

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>#

# Тест на членство в словаре
# Мы можем проверить, находится ли ключ в словаре или нет, используя ключевое слово «in».
# Обратите внимание, что проверка принадлежности предназначена только для ключей, а не для значений.
# Membership Test for Dictionary Keys
squares = {1: 1, 3: 9, 5: 25, 7: 49, 9: 81}

# Output: True
print(1 in squares) # prints True
# Output: True
print(2 not in squares) # prints True
# Output: True
# membership tests for key only not value
print(49 in squares) # prints false
# Output: False

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>#

# Итерация по словарю
# Iterating through a Dictionary
squares = {1: 1, 3: 9, 5: 25, 7: 49, 9: 81}
for i in squares:
    print(squares[i])
    # Output: 1
    # Output: 9
    # Output: 25
    # Output: 49
    # Output: 81

















