"""

В Python генератор — это функция , которая возвращает итератор , который создает последовательность значений при повторении.
Генераторы полезны, когда мы хотим создать большую последовательность значений, но не хотим хранить их все в памяти сразу.

"""


def my_generator(n):
    # initialize counter
    value = 0
    # loop until counter is less than n
    while value < n:
        # produce the current value of the counter
        yield value
        # increment the counter
        value += 1


# iterate over the generator object produced by my_generator
for value in my_generator(3):
    # print each value produced by generator
    print(value)

generator = my_generator(3)
print(next(generator))  # Output: 0
print(next(generator))  # Output: 1
print(next(generator))  # Output: 2


#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>#

# create the generator object
squares_generator = (i * i for i in range(5))

# iterate over the generator and print the values
for i in squares_generator:
    print(i)
# Output: 0
# Output: 1
# Output: 4
# Output: 9
# Output: 16

# Простота реализации генератора:


class PowTwo:
    def __init__(self, max=0):
        self.n = 0
        self.max = max

    def __iter__(self):
        return self

    def __nexr__(self):
        if self.n > self.max:
            raise StopIteration

        result = 2 ** self.n
        self.n += 1
        return result

# Тоже самое что написано выше, но более лаконичнее:


def PowTwoGen(max=0):
    n = 0
    while n < max:
        yield 2 ** n
        n += 1

# Генераторы — отличные средства для представления бесконечного потока данных
# Следующая функция генератора может генерировать все четные числа (по крайней мере, теоретически)


def all_even():
    n = 0
    while True:
        yield n
        n += 2


#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>#

# Конвейерные генераторы

def fibonacci_numbers(nums):
    x, y = 0, 1
    for _ in range(nums):
        x, y = y, x + y
        yield x


def square(nums):
    for num in nums:
        yield num ** 2


print(sum(square(fibonacci_numbers(10))))
# Output: 4895
