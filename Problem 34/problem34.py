import math

start = 10
stop = 10**6

successes = []

for value in range(start,stop):
	list_digs = list(str(value))
	sum_of_facts = 0
	for digit in list_digs:
		digit = int(digit)
		sum_of_facts += math.factorial(digit)
		if sum_of_facts > value:
			break
	if sum_of_facts == value:
		successes.append(value)

print(successes)
print(sum(successes))