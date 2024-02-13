import numpy as np

# NumPy Creating Arrays
my_array1 = np.array([[1, 2, 3],
                      [3, 4, 5],
                      [48, 4, 4]])

print(type(my_array1))
print(my_array1)
# NumPy Arrays provides the ndim attribute that returns an integer that tells us how many dimensions the array have.

a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

print("a = ", a.ndim)
print("b = ", b.ndim)
print("c = ", c.ndim)
print("d = ", d.ndim)
print("my_array1 = ", my_array1.ndim)

my_array2 = np.array([1, 2, 3, 4], ndmin=5)
print(my_array2)
print('number of dimensions: ', my_array2.ndim)


# NumPy Array Indexing
my_array3 = np.array([1, 2, 3])
print(my_array3[0])
print(my_array3[0] + my_array3[2])

arr = np.array([[1, 2, 3, 4],
                [5, 6, 7, 8]])
print('2nd element on 1st row: ', arr[0, 1])

print(arr[0:, 0:])


# house list of lists
house = [["hallway", 11.25],
         ["kitchen", 18.0],
         ["living room", 20.0],
         ["bedroom", 10.75],
         ["bathroom", 9.50]]

# Build a for loop from scratch
for room in house:
    print(f'{room[0]} is {room[1]} sqm')


np_height = np.array([1.73, 1.68, 1.71, 1.89, 1.79])
np_weight = np.array([64.4, 59.2, 63.6, 88.4, 68.7])
meas = np.array([np_height, np_weight])
for val in np.nditer(meas):
    print(val)


# Random generators
x = np.random.rand() # Pseudo-random numbers
np.random.seed(123) # Same seed: same random numbers!
y = np.random.rand() # Ensures "reproducibility"
c = np.random.rand()
print(x)
print(y)
print(c)

# game.py
import numpy as np

np.random.seed(123)
coin = np.random.randint(0, 2) # Randomly generate 0 or 1
print(coin)

if coin == 0:
    print("heads")
else:
    print("tails")


# NumPy is imported, seed is set

# Starting step
step = 50

# Roll the dice
dice = np.random.randint(1, 7)

# Finish the control construct
if dice <= 2 :
    step -= 1
elif dice > 2 and dice <= 5 :
    step += 1
else :
    step = step + np.random.randint(1,7)

# Print out dice and step
print(dice, step)

# Heads or Tails
# headtails.py
np.random.seed(123)
outcomes = []
for x in range(10):
    coin = np.random.randint(0, 2)
    if coin == 0:
        outcomes.append("heads")
    else:
        outcomes.append("tails")
print(outcomes)


# Heads or Tails: Random Walk
tails = [0]
for x in range(10):
    coin = np.random.randint(0, 2)
    tails.append(tails[x] + coin)
print(tails)


# NumPy is imported, seed is set

# Initialize random_walk
random_walk = [0]

# Complete the ___
for x in range(100) :
    # Set step: last element in random_walk
    step = random_walk[-1]

    # Roll the dice
    dice = np.random.randint(1,7)

    # Determine next step
    if dice <= 2:
        step = max(0, step - 1)
    elif dice <= 5:
        step = step + 1
    else:
        step = step + np.random.randint(1,7)

    # append next_step to random_walk
    random_walk.append(step)

# Print random_walk
print(random_walk)





# numpy and matplotlib imported, seed set.

# initialize and populate all_walks
all_walks = []
for i in range(5) :
    random_walk = [0]
    for x in range(100) :
        step = random_walk[-1]
        dice = np.random.randint(1,7)
        if dice <= 2:
            step = max(0, step - 1)
        elif dice <= 5:
            step = step + 1
        else:
            step = step + np.random.randint(1,7)
        random_walk.append(step)
    all_walks.append(random_walk)

# Convert all_walks to NumPy array: np_aw
np_aw = np.array(all_walks)

# Plot np_aw and show
plt.plot(np_aw)
plt.show()
# Clear the figure
plt.clf()

# Transpose np_aw: np_aw_t
np_aw_t = np.transpose(np_aw)

# Plot np_aw_t and show
plt.plot(np_aw_t)
plt.show()



# numpy and matplotlib imported, seed set

# clear the plot so it doesn't get cluttered if you run this many times
plt.clf()

# Simulate random walk 20 times
all_walks = []
for i in range(20) :
    random_walk = [0]
    for x in range(100) :
        step = random_walk[-1]
        dice = np.random.randint(1,7)
        if dice <= 2:
            step = max(0, step - 1)
        elif dice <= 5:
            step = step + 1
        else:
            step = step + np.random.randint(1,7)

        # Implement clumsiness
        if np.random.rand() <= 0.005 :
            step = 0

        random_walk.append(step)
    all_walks.append(random_walk)

# Create and plot np_aw_t
np_aw_t = np.transpose(np.array(all_walks))
plt.plot(np_aw_t)
plt.show()