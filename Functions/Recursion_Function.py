"""

Рекурсивная функция - функция, которая вызывает сама себя
Рекурсия — это процесс определения чего-либо в терминах самого себя
Примером физического мира может быть размещение двух параллельных зеркал друг против друга.
Любой объект между ними будет рекурсивно отражаться.

"""


# Пример рекурсивной функции
def factorial(x):
    """This is a recursive function
    to find the factorial of an integer"""

    if x == 1:
        return 1
    else:
        return (x * factorial(x-1))


num = 3
print("The factorial of", num, "is", factorial(num))
# Output: The factorial of 3 is 6
