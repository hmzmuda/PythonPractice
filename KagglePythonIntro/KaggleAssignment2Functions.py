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
#Default arguments, so bult in functions have default arguments, such as sep in the print function
print(1, 2, 3, sep = ' < ')
def greet(who = "Colin"):
    print("Hello, ", who)
greet()
greet(who = "Kaggle")
greet("world")
#Functions Applied to Functions
def multByFive(x):
    return 5 * x
def call(fn, arg):
    """Call fn on arg"""
    return fn(arg)
def squaredCall(fn, arg):
    """Call fn on the result of calling fn on arg"""
    return fn(fn(arg))
print(
    call(multByFive, 1),
    squaredCall(multByFive, 1),
    sep = '\n',
)
def mod5(x):
    """Return ther remainder of x after by 5"""
    return x % 5
print(
    'Which number is biggest?',
    max(100, 51, 14),
    'Which number is the biggest modulo 5?',
    max(100, 51, 14, key = mod5), #But if we pass in a function using the optional key argument, it returns the argument x that maximizes key(x) (aka the 'argmax')
    sep = '\n',
)
help(round)