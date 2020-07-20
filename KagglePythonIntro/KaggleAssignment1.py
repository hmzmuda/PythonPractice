#This is the notebook for Exercise 1 from Kaggle
spamAmount = 0 #variable Assignent
print(spamAmount) #Function call, print function to print out variable
#Ordering Spam, egg, Spam, Spam, bacon and SPam (4 more servings of Spam)
spamAmount = spamAmount + 4 #reassign variable
if spamAmount > 0: #colon at the end indicates a new "code block" is starting
    print("But I don't want ANY spam!")
vikingSong = "Spam" * spamAmount #no longer part of the if statement coding block can use string with multiplier operator
print(vikingSong)
#type is a built-in function to help decipher data type
print(type(spamAmount))
print(type(19.995))
print("True Division")
print(5/2)
print(6/2)
print("Floor Division")
print(5 // 2)
print(6 // 2)
#REMEMBER, Python follows PEMDAS (order of operation)
#Built-in functions: min and max
print("Built in functions: Min and Max")
print(min(1, 2, 3))
print(max(1, 2, 3))
#Changing data type using built-in functions
print("Built-in functions for changing data type")
print(float(10))
print(int(3.5456))
#They can even be called strings
print(int('807') + 1)
