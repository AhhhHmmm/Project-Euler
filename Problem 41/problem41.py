import math
import itertools

def isPrime(num):
	prime = True
	for value in range(2,int(round(num**0.5))+1):
		if num % value == 0:
			prime = False
			break
	return(prime)


import itertools

for num_digs in range(2,10):
	numbers = range(1,num_digs)
	perms = itertools.permutations(numbers)
	for perm in perms:
		list_perm = list(perm)
		string_perm = ''
		for value in list_perm:
			string_perm += str(value)
		if isPrime(eval(string_perm)):
			print(string_perm)
		# print(string_perm)

print(isPrime(7652413))