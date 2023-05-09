"""

В Python лямбда-функция — это особый тип функции без имени функции
lambda argument(s) : expression

"""


# declare a lambda function
greet = lambda: print('Hello World')
# call the lambda
greet()
# Output: Hello World


# Лямбда-функция с аргументом
# lambda that accepts one argument
greet_user = lambda name: print('Hey there,', name)

# lambda call
greet_user('Pozdniakov')
# Output: Hey there, Pozdniakov

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>#

# Как использовать лямбда-функцию с filter()?
# Program to filter out only the even items from a list
my_list = [1, 5, 4, 6, 8, 11, 3, 12]

new_list = list(filter(lambda x: (x%2 == 0) , my_list))

print(new_list)

# Output: [4, 6, 8, 12]

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>#

# Как использовать лямбда-функцию с map()?
# Program to double each item in a list using map()
my_list = [1, 5, 4, 6, 8, 11, 3, 15]

new_list = list(map(lambda x: x * 2, my_list))

print(new_list)
# Output: [2, 10, 8, 12, 16, 22, 6, 30]
