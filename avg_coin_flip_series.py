import random
import time

start = time.time()
def coin_flip(trials=10):
    attempt = 0
    series = {}
    sum = 0
    for trial in range(1, trials + 1):
        series.update({trial: None})
        side = set()  # сторона
        while True:
            attempt += 1
            if random.randint(0, 1) == 1:
                series.update({trial: attempt})
                side.add("heads")
            else:
                series.update({trial: attempt})
                side.add("tails")
            if len(side) == 2:
                attempt = 0
                break
    for i in series.values():
        sum = sum + i
        average = sum / trials

    return print(f"The average number of flips per trial is {average}.")


print(coin_flip(10000))
end = time.time() - start
print(end)
