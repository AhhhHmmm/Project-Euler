import math

power = 999

f1 = 1
f2 = 1
count = 2

while math.log(f2, 10) < power:
	count += 1
	f3 = f1 + f2
	f1 = f2
	f2 = f3

#print(str(f2) + ' is the first Fibonnaci number with more than ' + str(10**power) + ' digits.')
print('This number is the ' + str(count) + ' Fibonacci number')