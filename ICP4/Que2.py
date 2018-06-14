"""
trying with lists
import random

x=0
a=[]
b=[]
max1=[]
min1=[]
for i in range(0,10):
    for j in range(0,10):
        x = random.randint(0,100)
        b.append(x)
    print(b)
    max1.append(max(b))
    min1.append(min(b))
    a.append(b)
    b=[]


print()


print("maximum value:")
print(max1)
print()
print("minimum value:")
print(min1)
"""
import numpy
#imported for different numpy

x=numpy.random.randint(25,size=(10, 10))
#it is used for generation of a random 10X10 matrix with range of 25
print(x)




xmin = x.min(axis=1) # minimum value for the row
xmax =x.max(axis=1) # max for the line
print()
print(xmin)
print()
print(xmax)