#practice Monte Carlo in Python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random

#Coin flip function
def coin_flip():
    return random.randint(0,1)

#main monte carlo function
list1 = []

def monte_carlo(n):
    results = 0
    for i in range(n):
        flip_result = coin_flip()
        results = results + flip_result

        prob_value = results/(i+1)
        list1.append(prob_value)

        plt.plot(list1)
        plt.axhline(y=0.5, color='r', linestyle='-')
        plt.xlabel("Iterations")
        plt.ylabel("Probability")
        
    return results/n

answer = monte_carlo(1000)

print("Final Value:", answer)
plt.show()

