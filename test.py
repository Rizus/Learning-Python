# map, filter, lambda
def squarify(a):
    return a ** 2


print(list(map(squarify, range(5))))
# Output: [0, 1, 4, 9, 16]