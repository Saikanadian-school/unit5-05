from __future__ import division 
from numpy import random

def averagearray(array_numbers = []):
    arraysum = 0
    for row in array_numbers:
      for column in row:
        arraysum = arraysum + column
      
    averagenumbers = arraysum / (len(array_numbers) * len(array_numbers[0]))
    return averagenumbers


numrows = input('number of rows: ')
numcols = input('number of columns: ')

elements = []
for row in range(0,numrows):
    elements.append([])
    for col in range(0,numcols):
      elements[row].append(random.randint(1, 50))
print elements
print('the average value is ' + str(averagearray(elements)))
