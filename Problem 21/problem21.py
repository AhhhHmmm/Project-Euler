start_val = 2
end_val = 10000

def find_divs(val):
	divs = []
	test_val = 1
	while test_val < val:
		if val % test_val == 0:
			divs.append(test_val)
		test_val += 1
	return(divs)

def test_amicable(val):
	count = 0
	divs = find_divs(val)
	prod_of_divs = 0
	for value in divs:
		prod_of_divs += value
	divs2 = find_divs(prod_of_divs)
	prod_of_divs2 = 0
	for value in divs2:
		prod_of_divs2 += value
	if prod_of_divs2 == val and val != prod_of_divs:
		print(str(val) + ' and ' + str(prod_of_divs) + ' are amicable nums!')
		count = val
	return(count)

count = 0
current_val = start_val
while current_val < end_val:
	count += test_amicable(current_val)
	current_val += 1

print('The sum of all amicable nums in range is ' + str(count))