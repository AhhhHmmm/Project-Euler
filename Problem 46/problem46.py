
def isPrime(num):
	prime = True
	for value in range(2,int(round(num**0.5))+1):
		if num % value == 0:
			prime = False
			break
	return(prime)

goldbach = True
value = 1
while goldbach:
	goldbach = False
	root = 1
	if isPrime(value):
		goldbach = True
	else:
		while root**2 < value:
			test_prime = value - 2*(root**2)
			if test_prime < 0:
				pass
			elif isPrime(test_prime):
				goldbach = True
			root += 1
	if goldbach:
		value += 2	

print(value)
