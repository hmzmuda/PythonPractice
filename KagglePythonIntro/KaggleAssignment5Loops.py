#This tutorial focuses on loops
planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
for planet in planets:
    print(planet, end = ' ')

multiplicands = (2, 2, 2, 3, 3, 5)
product = 1
for mult in multiplicands:
    product = product * mult
print(product)

s = 'stegangrapHy is the practicE of conceaLing, a file, a mess, an age, image, or video within another fiLe, message, image, Or video.'
msg = ''
for char in s:
    if char.isupper():
        print(char, end = '')
print('\n')

#while Loops
i = 0
while i < 10:
    print(i, end = ' ')
    i += 1
print('\n')

#List Comprehensions also know as an each item for loop
#Here is the basic syntax for list comprehensions:
#newList = [expression for_loop_one_or_more conditions]
squares = [n**2 for n in range(10)]
print(squares)

short_planets = [planet for planet in planets if len(planet) < 6]
print(short_planets)

#applying if conditional and applying some transform to the loop variable
loudShortPlanets = [planet.upper() + '!' for planet in planets if len(planet) < 6]
print(loudShortPlanets)

print([32 for planet in planets])

#List Comptehensions are helpful for comppressing function returns
def countNegatives(nums):
    """Returns the number of negative numbers in a list"""
    return len([num for num in nums if num < 0])
num = [1, 4, 6, -2, 9, -3, -20]
print(countNegatives(num))

nums = []
print(len(nums))

#Prime example of each element for loop. No indexing requried
def elementwise_greater_than(L, thresh):
    """Return a list with the same length as L, where the value at index i is 
    True if L[i] is greater than thresh, and False otherwise.
    
    >>> elementwise_greater_than([1, 2, 3, 4], 2)
    [False, False, True, True]
    """
    return [i > thresh for i in L]
print(elementwise_greater_than([1, 2, 3, 4], 2))