def isPrime(num):
	prime = True
	if num == 1:
			prime = False
	for value in range(2,int(round(num**0.5))+1):
		if num % value == 0:
			prime = False
			break
	return(prime)

def left_to_right(num):
	temp_num = str(num)
	all_prime = True
	while temp_num and all_prime:
		all_prime = isPrime(int(temp_num))
		temp_num = temp_num[:-1]
	return(all_prime)

def right_to_left(num):
	temp_num = str(num)
	all_prime = True
	while temp_num and all_prime:
		all_prime = isPrime(int(temp_num))
		temp_num = temp_num[1:]
	return(all_prime)

def truncatable(num):
	truncatably_prime = False
	forwards = left_to_right(num)
	backwards = right_to_left(num)
	if forwards and backwards:
		truncatably_prime = True
		print(str(num) + ' is truncatably prime!')
	return(truncatably_prime)

start = 10
end = 10**6
total = 0
for value in range(start,end):
	if truncatable(value):
		total += value

print(total)

