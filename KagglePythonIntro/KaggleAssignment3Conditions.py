#This section of Kaggle review in Python goes over conditional statements
#Booleans
x = True
print(x)
print(type(x))
#Comparion Operations
def CanRunForPres(age):
    """Can someone of teh given age for president in the UnitedStates"""
    return age >= 35

print("Can a 19-year-old run for president?", CanRunForPres(19))
print("Can a 45-year-old run for president?", CanRunForPres(45))

def isOdd(n):
    return (n % 2) == 1

print("Is 100 odd?", isOdd(100))
print("Is -1 odd?", isOdd(-1))

#combining boolean values
def CanRunForPresComb(age, natBorn):
    """Can someone of the given age and citizenship status run for president in the US?"""
    return natBorn and (age >= 35)

print(CanRunForPresComb(19, True))
print(CanRunForPresComb(55, False))
print(CanRunForPresComb(55, True))

#Conditionals
def inspect(x):
    if x == 0:
        print(x, "is zero")
    elif x > 0:
        print(x, "is positive")
    elif x < 0:
        print(x, "is negative")
    else:
        print(x, "is unlike anything I've ever seen...")

inspect(0)
inspect(-15)


