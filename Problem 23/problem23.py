
start = 2
stop = 28124

def find_abunds(start,stop):
	abundant_nums = []
	current = start
	while current <= stop:
		test_val = 1
		divs = []
		while test_val < current:
			if current % test_val == 0:
				divs.append(test_val)
			test_val += 1
		sum_divs = sum(divs)
		#print(str(current) + ' has ' + str(sum_divs))
		if sum_divs > current:
			abundant_nums.append(current)
		current += 1
	return abundant_nums

def check_sum_of_abunds(start,stop,abundant_nums):
	current = start
	fail_nums = range(stop+1)
	while current <= stop:
		for value in abundant_nums:
			difference = current - value
			if difference in abundant_nums:
				fail_nums.remove(current)
				break
		current += 1
	return(fail_nums)

abundant_nums = find_abunds(start,stop)
fail_nums = check_sum_of_abunds(start,stop,abundant_nums)
print(sum(fail_nums))