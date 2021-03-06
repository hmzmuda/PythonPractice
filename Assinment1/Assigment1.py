#Assignment 1 in Python practice
#Tasks:
    #1 Program to accept user input
    #2 Program to accept and respond to user input
    #3 Program to take all info and write to a file
    #4 Program to read data from .csv file, do simple statistic, display data using mathplotlib
#git commit after task 3, continue with task 4
import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Script Begins

print("Assignment 1")
#Problem 1 and 2: Request User input and respond
print("Task 1")
name = input("Please enter your full name: ")
print("Hello", name)

#Problem 3: Take info and write to a file
data = input("Please enter an array of random numbers: ")
file = open("Assignment1.txt", "w+")
answer = input("Would you like to add array to Assignment1.txt? yes or no ")
if answer == "yes":
    file.write(" %s\r\n" % data)
    file.close
else:
    print("No data will be added")
    file.close

#Problem 4: read in a .csv file and manipulate data. Use mathplotlib to display data
#read in csv file using pandas module
fileTask4 = pd.read_csv("Assignment1Students.csv")
#Print the csv table
print(fileTask4)
#Statitics for the grades
print(fileTask4['Test Scores'].describe())
#Statistics for the Income
print(fileTask4['Family Income'].describe())
#Displaying data using matplotlib
x = fileTask4['Test Scores']
y = fileTask4['Family Income']
plt.scatter(x,y)
plt.xlabel('Test Scores (%)')
plt.ylabel('Family Income ($)')
plt.title('Test Scores from a class vs. Family Income')
plt.grid(color='black', linestyle='-', linewidth=0.5)
plt.show()


#Script Ends