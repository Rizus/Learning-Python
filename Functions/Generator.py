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
