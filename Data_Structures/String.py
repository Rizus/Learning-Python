"""

Строка представляет собой последовательность символов.
Например, "hello" это строка, содержащая последовательность символов 'h', 'e', 'l', 'l', и 'o'.
Мы используем одинарные или двойные кавычки для представления строки
В Python строки неизменяемые

"""

# create a string using double quotes
string1 = "Python programming"

# create a string using single quotes
string1 = 'Python programming'

# create string type variables
name = "Python"
print(name)
# Output: Python

message = "I love Python."
print(message)
# Output: I love Python.

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>#

# Доступ к строковым символам
# Индексирование: Один из способов — рассматривать строки как список и использовать значения индекса
greet = 'hello'
# access 1st index element
print(greet[1])
# Output: e

# Отрицательное индексирование. Подобно списку, Python допускает отрицательное индексирование своих строк
greet = 'hello'
# access 4th last element
print(greet[-4])
# Output: e

# Нарезка: доступ к диапазону символов в строке с помощью двоеточия оператора среза ":"
greet = 'Hello'
# access character from 1st index to 3rd index
print(greet[1:4])
# Output: ell

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>#

# Многострочная строка
# multiline string
message = """
Never gonna give you up
Never gonna let you down
"""

print(message)
# Output: Never gonna give you up
#           Never gonna let you down

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>#

# Строковые операции
# 1. Сравните две строки
str1 = "Hello, world!"
str2 = "I love Python."
str3 = "Hello, world!"

# compare str1 and str2
print(str1 == str2)
# Output: False

# compare str1 and str3
print(str1 == str3)
# Output: True

# 2. Соедините две или более строки
greet = "Hello, "
name = "Jack"

# using + operator
result = greet + name
print(result)
# Output: Hello, Jack

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>#

# Итерация через строку
greet = 'Hello'

# iterating through greet string
for letter in greet:
    print(letter)
    # Output: H
    # Output: e
    # Output: l
    # Output: l
    # Output: o

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>#

# Длина строки Python
greet = 'Hello'

# count length of greet string
print(len(greet))
# Output: 5

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>#

# Тест на принадлежность к строке
print('a' in 'program')
# Output: True
print('at' not in 'battle')
# Output: False

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>#

# Методы строки
# upper()           - converts the string to uppercase ~> https://www.programiz.com/python-programming/methods/string/upper
# lower()           - converts the string to lowercase ~> https://www.programiz.com/python-programming/methods/string/lower
# partition()       - returns a tuple ~> https://www.programiz.com/python-programming/methods/string/partition
# replace()         - replaces substring inside ~> https://www.programiz.com/python-programming/methods/string/replace
# find()            - returns the index of first occurrence of substring ~> 
# rstrip()          - removes trailing characters ~> https://www.programiz.com/python-programming/methods/string/find
# split()           - splits string from left ~> https://www.programiz.com/python-programming/methods/string/split
# startswith()      - checks if string starts with the specified string ~> https://www.programiz.com/python-programming/methods/string/startswith
# isnumeric()       - checks numeric characters ~> https://www.programiz.com/python-programming/methods/string/isnumeric
# index()           - returns index of substring ~> https://www.programiz.com/python-programming/methods/string/index

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>#

# Escape Sequences
# Управляющая последовательность используется для экранирования некоторых символов, присутствующих внутри строки, с помощью символа "\"
# escape double quotes
example = "He said, \"What's there?\""
# escape single quotes
example = 'He said, "What\'s there?"'

print(example)
# Output: He said, "What's there?"

# Список всех escape-последовательностей, поддерживаемых Python
# Escape Sequence
# \\    - Backslash
# \'    - Single quote
# \"    - Double quote
# \a    - ASCII Bell
# \b    - ASCII Backspace
# \f    - ASCII Formfeed
# \n    - ASCII Linefeed
# \r    - ASCII Carriage Return
# \t    - ASCII Horizontal Tab
# \v    - ASCII Vertical Tab
# \ooo  - Character with octal value ooo
# \xHH  - Character with hexadecimal value HH

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>#

# Форматирование строк Python (f-строки)
name = 'Cathy'
country = 'UK'

print(f'{name} is from {country}')
# Output: Cathy is from UK















