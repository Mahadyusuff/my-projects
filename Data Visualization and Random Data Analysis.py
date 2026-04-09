import math
import random
import matplotlib.pyplot as plt

x = [i for i in range(101)]
y = [math.sqrt(i) for i in x]

plt.plot(x, y)
plt.title("y = sqrt(x)")
plt.show()

x_rand = [random.randint(0, 100) for _ in range(20)]
y_rand = [random.randint(0, 100) for _ in range(20)]

plt.scatter(x_rand, y_rand)
plt.title("Random Scatter Plot")
plt.show()

rolls = [random.randint(1, 6) for _ in range(100)]

plt.hist(rolls, bins=6)
plt.title("Histogram of Dice Rolls")
plt.show()
