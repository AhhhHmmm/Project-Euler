import math

def isPrime(num):
	prime = True
	for value in range(2,int(round(num**0.5))+1):
		if num % value == 0:
			prime = False
			break
	return(prime)

# the 78498th prime number is the last prime less than 1 million

primes = []
count = 0

print('Gathering primes....')

num = 2
while count <= 78497:
	if isPrime(num):
		primes.append(num)
		count += 1
	num += 1

max_length = 0
start_index = 0

print('Primes gathered...beginning!')

# get the max sequence for each starting prime by adding all and then
while start_index < len(primes):
	if primes[start_index] > 10000:
		break
	# if start_index % 100 == 0:
	# 	print('Starting with the ' + str(start_index) + 'th prime: ' + str(primes[start_index]))
	end_index = len(primes)
	cur_len = 0
	cur_sum = sum(primes[start_index:end_index])
	while cur_sum > 1000000:
		cur_sum -= primes[end_index-1]
		cur_len = end_index - start_index
		end_index -= 1
	while cur_sum not in primes:
		# print('Current sum now less than 1 million!')
		cur_sum -= primes[end_index-1]
		cur_len = end_index - start_index
		end_index -= 1
	print('Max length with ' + str(primes[start_index]) + ' is: ' + str(cur_len) + ', resulting in ' + str(cur_sum) + '.')
	if cur_len > max_length:
		max_length = cur_len
		max_length_sum = cur_sum
	start_index += 1

print('Max length is: ' + str(max_length) + ' resulting in a sum of ' + str(max_length_sum))