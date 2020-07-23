#This Kaggle lesson looks into Strings and Dictionary data ypes in python
print('Pluto\'s a planet')
planet = 'Pluto'
print(planet[0])
print(planet[-3:])
print([char + '!' for char in planet])

#String methods
#python has different functions to manipulate strings
normMsg = "Pluto is a planet!"
upperMsg = normMsg.upper()
lowerMsg = normMsg.lower()
indexMsg = normMsg.index('plan')
print(upperMsg)
print(lowerMsg)
print(indexMsg)
#can also use .startswith and .endswith and return a boolean

#Goint between strings and lists
splitMsg = normMsg.split()
print(splitMsg)
print(' :) '.join([each.upper() for each in splitMsg]))

#Building strings with formats
#Python lets us concatenate strings with the plus operator
print(planet + ', we miss you.')
#Use format to make sure everything is a str type and not any other data type
position = 9
"{}, you'll always be the {}th planet to me.".format(planet,position)
s = """Pluto's a {0}.
No, it's a {1}.
{0}!
{1}!""".format('planet', 'dwarf planet')
print(s)

#Dictionaries: built-in Python data structure for mapping keys to values
numbers = {'one':1, 'two':2, 'three':3}
print(numbers['one'])
planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
planetsInital = {planet: planet[0] for planet in planets}
print(planetsInital)

def word_search(doc_list, keyword):
    """
    Takes a list of documents (each document is a string) and a keyword. 
    Returns list of the index values into the original list for all documents 
    containing the keyword.

    Example:
    doc_list = ["The Learn Python Challenge Casino.", "They bought a car", "Casinoville"]
    >>> word_search(doc_list, 'casino')
    >>> [0]
    """
    output = []
    for index, title in enumerate(doc_list):
        newTitle = title.split()
        normalized = [word.rstrip(',.').lower() for word in newTitle]
        if keyword.lower() in normalized:
            output.append(index)
    return output

doc_list = ["The Learn Python Challenge Casino.", "They bought a car", "Casinoville"]
word_search(doc_list,"casino")