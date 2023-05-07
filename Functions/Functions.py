"""

Функция — это блок кода, выполняющий определенную задачу
Разделение сложной задачи на более мелкие части делает нашу программу простой для понимания и повторного использования
Есть два типа функций:
    ~> Стандартные библиотечные функции — это встроенные в Python функции, доступные для использования
    ~> Пользовательские функции . Мы можем создавать собственные функции на основе наших требований

"""

# Объявление функции


def function_name(arguments):
    # function body

    return


# Вызов функции
def greet():
    print('Hello World!')


# call the function
greet()
# Output: Hello World!

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>#

# Аргументы функции
# function with two arguments


def sum_numbers(num1, num2):
    sum = num1 + num2
    print('Sum: ', sum)

# function with no argument


def empy_func():
    pass


# function call with two values
sum_numbers(5, 4)
# Output: Sum:  9

# function call with no value
empy_func()

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>#

# Функция Python с произвольными аргументами
# program to find sum of multiple numbers


def find_sum(*number):
    result = 0
    for num in number:
        result = result + num
    print("Sum = ", result)


# function call with 3 arguments
find_sum(1, 2, 3)
# Output: Sum =  6

# function call with 2 arguments
find_sum(4, 9)
# Output: Sum =  13

# function call with 10 arguments
find_sum(1, 4, 9, 5, 3, 6, 7, 7, 3, 2)
# Output: Sum =  47
