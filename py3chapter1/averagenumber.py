# average numbers

import sys
import random
from pdb import set_trace as db

numbers=[]
indexes=[]
total=0
lowest=None
highest=None

while True:
	try:
		line = input("enter number: ")
		if not line:
			break
		indexes.append(len(numbers))
		number= int(line)
		numbers.append(number)
		total += number
		if lowest is None or lowest > number:
			lowest = number
		if highest is None or highest < number:
			highest = number
	except ValueError as err:
		print(err)

swapped = True
while swapped:
	swapped = False
	for index in indexes:
		if index +1 == len(numbers):
			break
		if numbers[index] > numbers[index+1]:
			temp = numbers[index]
			numbers[index] = numbers[index+1]
			numbers[index+1]=temp
			swapped=True

if numbers:
	index = int(len(numbers)/2)
	median = numbers[index]
	if index and index*2 == len(numbers):
		median = (median + numbers[index-1])/2

print("numbers: ", numbers)
if numbers:
	print("count= ",len(numbers),"total= ",total,
		  "lowest= ",lowest,"highest= ",highest,
		  "mean= ",total/len(numbers), "median= ",median)
