#Kaggle Assignment 4 Lists
#list/array of numbers
primes = [2, 3, 5, 7]
#list of strings
planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
#List of lists, can be written as a matrix with indents or on one line
hands = [
    ['J', 'Q', 'K'],
    ['2', '2', '2'],
    ['6', 'A', 'K'],#This comma at the end of the list is OPTIONAL
]
#indexing
print(planets[0])
#which planet is furthest from the sun?
print(planets[-1])
#slicing
#what are the first three planets?
print(planets[0:3])#or can write planets[:3]
print(planets[3:])
#Changing Lists
planets[3] = 'Malacandra'
print(planets)
#List Functions
#len gives the length of a list
len(planets)
#sorted returns a sorted version of a list places the list in alphabetical order
sorted(planets)
print(sum(primes))
max(primes)
#Interlude objects
#variables can carry various parts, such as imaginary numbers. To access this you can use the . 
x = 12
print(x.imag)#imaginary = 0
c = 12 + 3j
print(c.imag) #imaginary number = 3
print(x.bit_length())
#list methods
planets.append('Pluto')
print(planets)
planets.pop()#need () at the end of .pop for the function to work. pop removes last element of teh list
print(planets)
planets.index('Earth')
"Earth" in planets
"Calbefraques" in planets
#Tuples: tuples are like lists but in () instead of square brackets and they are IMMUTABLE
name = 'Hannah'
print(name, "is fashionable late")