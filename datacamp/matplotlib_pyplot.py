import matplotlib.pyplot as plt
import random

# year = [1950, 1970, 1990, 2010]
# pop = [2.519, 3.692, 5.263, 6.972]

# plt.plot(year, pop)
# plt.show()

# =>

# year = [1950, 1970, 1990, 2010]
# pop = [2.519, 3.692, 5.263, 6.972]

# plt.scatter(year, pop)
# # plt.xscale('log')
# plt.show()

# =>

#values = [0,0.6,1.4,1.6,2.2,2.5,2.6,3.2,3.5,3.9,4.2,6]
#plt.hist(values, bins=5)
#plt.show()
#plt.clf()

# =>

# Specify c and alpha inside plt.scatter()
# plt.scatter(x = gdp_cap, y = life_exp, s = np.array(pop) * 2, c = col, alpha=0.8)

year = [*range(1950, 2100,  1)]
list_size = len(year)
int_list = random.sample(range(250, 1000), list_size)
float_list = [x/100 for x in int_list]
pop = sorted(float_list)

year = [1800, 1850, 1900] + year
pop = [1.0, 1.262, 1.650] + pop

plt.plot(year, pop)
plt.xlabel('Year')
plt.ylabel('Population')
plt.title('World Population Projections')
plt.yticks([0, 2, 4, 6, 8, 10],
    ['0', '2B', '4B', '6B', '8B', '10B'])
plt.grid(True)

plt.show()











