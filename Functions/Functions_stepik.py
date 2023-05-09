# Передача функций в другие функции - Функции это теже обьекты
# Функция которая может принимать другую функцию


from functools import reduce, partial


def caller(func, params):
    return func(*params)

# Функция которая выводит строку


def printer(name, origin):
    print('I\'m {} of {}!'.format(name, origin))


# Вызываем функцию caller в которую передаем функцию printer со списком параметров
caller(printer, ["Moana", "Motunui"])
# Output: I'm Moana of Motunui!


#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>#

# Создаем функцию внутри другой функции
def get_multiplier():
    def inner(a, b):
        return a * b
    return inner


multiplier = get_multiplier()
print(multiplier(10, 11))
# Output: 110

print(multiplier.__name__)
# Output: inner

# Еще пример


def get_multiplier(number):
    def inner(a):
        return a * number
    return inner


multiplier_by_2 = get_multiplier(2)
print(multiplier_by_2(10))
# Output: 20

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>#

# Функции map, filter, lambda
# map


def squarify(a):
    return a ** 2


print(list(map(squarify, range(5))))
# Output: [0, 1, 4, 9, 16]

# Функция map в чистом Python
squared_list = []

for number in range(5):
    squared_list.append(squarify(number))

print(squared_list)
# Output: [0, 1, 4, 9, 16]

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>#

# filter


def is_positive(a):
    return a > 0


print(list(filter(is_positive, range(-2, 3))))
# Output: [1, 2]

# Функция filter в чистом Python
positive_list = []

for number in range(-2, 3):
    if is_positive(number):
        positive_list.append(number)

print(positive_list)
# Output: [1, 2]

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>#

# lambda


print(list(map(lambda x: x ** 2, range(5))))
# Output: [0, 1, 4, 9, 16]

print(list(filter(lambda x: x > 0, range(-2, 3))))
# Output: [1, 2]

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>#

# Функция которая превращает список чисел в список строк


def stringify_list(num_list):
    return list(map(str, num_list))


print(stringify_list(range(10)))
# Output: ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>#

# from functools import reduce


def multiply(a, b):
    return a * b


print(reduce(multiply, [1, 2, 3, 4, 5]))
# Output: 120

# тоже самое через lambda
reduce(lambda x, y: x * y, range(1, 6))
# Output: 120

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>#

# from functools import partial


def greeter(person, greeting):
    return '{}, {}!'.format(greeting, person)


hier = partial(greeter, greeting='Hi')
helloer = partial(greeter, greeting='Hallo')

print(hier('brother'))
print(helloer('sir'))
# Output: Hi, brother!
# Output: Hallo, sir!

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>#

# Списочные выражения
# Список квадратов на чистом Python
square_list = []
for number in range(10):
    square_list.append(number ** 2)

print(square_list)
# Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# можно написать намного проще:
square_list = [number ** 2 for number in range(10)]
print(square_list)
# Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# Еще пример списочных выражений с условием if
even_list = []
for number in range(10):
    if number % 2 == 0:
        even_list.append(number)

print(even_list)
# Output: [0, 2, 4, 6, 8]

# можно написать намного проще:\
even_list = [num for num in range(10) if num % 2 == 0]
print(even_list)
# Output: [0, 2, 4, 6, 8]


# Так же можно работать и с dict
square_map = {number: number ** 2 for number in range(5)}
print(square_map)
# Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}


# Так же можно работать и с set
reminder_set = {num % 10 for num in range(100)}
print(reminder_set)
# Output: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>#

# zip
num_list = range(7)
print(list(num_list))
# Output: [0, 1, 2, 3, 4, 5, 6]

squared_list = [x ** 2 for x in num_list]
print(list(squared_list))
# Output: [0, 1, 4, 9, 16, 25, 36]
print(list(zip(num_list, squared_list)))
# Output: [(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25), (6, 36)]
