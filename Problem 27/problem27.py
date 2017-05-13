import math

def isPrime(num):
	prime = True
	for value in range(2,int(round(num**0.5))+1):
		if num % value == 0:
			prime = False
			break
	return(prime)

def f(a,b,x):
	return(x**2+a*x+b)

best_streak = 0

for a in range(-1000,1000):
	for b in range(-1000,1000):
		streak = 0
		x = 0
		while f(a,b,x) > 0 and isPrime(f(a,b,x)):
			streak += 1
			x += 1
		if streak > best_streak:
			best_a = a
			best_b = b
			best_streak = streak
			print('x^2+' + str(a) + 'x+' + str(b))

print(best_a*best_b)