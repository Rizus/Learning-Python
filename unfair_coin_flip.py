import random


def coin_flip(probability_of_tails):
    if random.random() < probability_of_tails:
        return "tails"
    else:
        return "heads"


def unfair_coin_flip_test():
    heads_tally = 0
    tails_tally = 0
    for trial in range(10_000):
        if coin_flip(.7) == "heads":
            heads_tally = heads_tally + 1
        else:
            tails_tally = tails_tally + 1
    ratio = heads_tally / tails_tally
    return print(f"The ratio of heads to tails is {ratio}")


print(unfair_coin_flip_test())
