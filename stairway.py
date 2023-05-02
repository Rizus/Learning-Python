import sys


num_steps = int(sys.argv[1])
for i in range(1, num_steps + 1):
    print("{0:>{1}}".format("#" * i, num_steps))
