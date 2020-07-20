#This second part in the Kaggle Python course goes over functions
#Defining functions
def leastDifference (a, b, c):
    #Provide doc string in function
    """Return the smallest difference between any two numbers among a, b, and c.

    >>>leastDifference(1, 5, -5)
    4
    """
    diff1 = abs(a - b)
    diff2 = abs(b - c)
    diff3 = abs(a - c)
    return min(diff1, diff2, diff3)

print(
    leastDifference(1, 10, 100),
    leastDifference(1, 10, 10),
    leastDifference(5, 6, 7),
)
#help(leastDifference)
#function without retun prints None None None
