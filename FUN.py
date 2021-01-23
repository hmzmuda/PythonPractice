print("Hello World")

my_array = [1,2,3,4]
print(my_array)

#Import libraries
import pandas as pd
import numpy as np
import random
import matplotlib.pyplot as plt

def roll_die():
    return random.randint(1,6)
#number of rolls
N = 100
out = []
result = 0
for i in range(N):
    result = roll_die()
    out.append(result)
    plt.plot(out)
    plt.axhline(y=0.5, color='r', linestyle='-')
    plt.xlabel("Iterations")
    plt.ylabel("Value")

plt.show()

