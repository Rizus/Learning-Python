import random


def voting():
    if random.random() < 0.7:
        return "A"
    else:
        return "B"


precincts = [voting() for i in range(10000)]

count_voices = precincts.count("A")
percentage = count_voices / 10000 * 100
print(percentage)
print("The number of votes for A is {}.".format(count_voices))