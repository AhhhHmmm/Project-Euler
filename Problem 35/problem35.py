import math

def isPrime(num):
	prime = True
	for value in range(2,int(round(num**0.5))+1):
		if num % value == 0:
			prime = False
			break
	return(prime)

start = 2
end = 10**6

def gen_cycles(num):
	list_digs = list(str(value))
	num_digs = len(list_digs)
	cycles = []
	for start_index in range(num_digs):
		temp_cycle = ''
		for plusser in range(num_digs):
			temp_cycle += list_digs[(start_index + plusser) % num_digs]
		cycles.append(int(temp_cycle))
	return(cycles)

all_primes_list = []
for value in range(start,end):
	if value % 100 == 0:
		print('We are up to ' + str(value))
	cycles = gen_cycles(value)
	for cycle in cycles:
		all_prime = True
		if isPrime(cycle) == False:
			#print(str(cycle) + ' is not all prime')
			all_prime = False
			break
	if all_prime:
		#print(str(value) + ' all prime')
		all_primes_list.append(value)

print(len(all_primes_list))
