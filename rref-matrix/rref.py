from numpy import *

m = input("How many rows in your matrix? ")
n = input("How many columns in your matrix? ")

mat = []

for i in range (0, m):
        userin = raw_input("Type all the numbers in row %d separated by spaces: " % (i+1))
        row = map(int, userin.split()) #split parses the input and separates by spaces; map converts them to integers
        mat.append(row)
        
newmat = asarray(mat) #turns into a numpy array

for i in range (0, m):
        if (sum(newmat[i]) != 0):
                print "they're not 0s"
