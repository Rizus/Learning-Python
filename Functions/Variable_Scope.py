"""

Мы можем объявлять переменные в трех разных областях: локальной, глобальной и нелокальной
1. Локальные переменные:
    Когда мы объявляем переменные внутри функции, эти переменные будут иметь локальную область видимости (внутри функции).
        Мы не можем получить к ним доступ вне функции.
2. Глобальные переменные
    В Python переменная, объявленная вне функции или в глобальной области видимости, называется глобальной переменной.
        Это означает, что глобальная переменная может быть доступна внутри или вне функции.
3. Нелокальные переменные
    В Python нелокальные переменные используются во вложенных функциях, локальная область видимости которых не определена.
        Это означает, что переменная не может находиться ни в локальной, ни в глобальной области видимости.

"""

# 1. Локальные переменные


def greet():

    # local variable
    message = 'Hello World'

    print('Local', message)


greet()
# Output: Local Hello World
# try to access message variable
# outside greet() function
# print(message)
# Output: NameError: name 'message' is not defined

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>#

# 2. Глобальные переменные
# declare global variable
message = 'Hello'


def greet():
    # declare local variable
    print('Local', message)


greet()
print('Global', message)
# Output: Local Hello
# Output: Global Hello

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>#

# 3. Нелокальные переменные
# outside function


def outer():
    message = 'local'

    # nested function
    def inner():

        # declare nonlocal variable
        nonlocal message

        message = 'nonlocal'
        print("inner:", message)

    inner()
    print("outer:", message)


outer()
# Output: inner: nonlocal
# Output: outer: nonlocal
