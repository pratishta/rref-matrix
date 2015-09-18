from numpy import *

m = input("How many rows in your matrix? ")
n = input("How many columns in your matrix? ")

mat = []
for i in range (0, m):
    userin = raw_input("Type all the numbers in row %d separated by spaces: " % (i+1))
    row = map(float, userin.split()) # split parses the input and separates by spaces; map converts them to integers
    mat.append(row)

newmat = asarray(mat) # turns into a numpy array
print newmat
print "\n\n"
lc = 0
i = 0
for i in range (0, m):
    if (sum(newmat[i]) != 0): # makes sure row isn't all 0s 
        first = newmat[i] 
        for j in range (0, n):
            if (newmat[i][j] != 0):
                lc = newmat[i][j]
                print ("the leading coefficient is %d" %lc)
                newmat[i] = first/(lc) # dividing the i'th row by the leading coefficient 
                for k in range (0, m):
                    if ((newmat[k][j] != 0) and (k!=i)):
                        newmat[k] = newmat[k] - (newmat[i] * newmat[k][j])
                print newmat
                print "\n"
                break  
              
print newmat
