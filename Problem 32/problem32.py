import itertools

numbers = ['9','8','7','6','5','4','3','2','1']
products = []

combos = itertools.permutations(numbers)
for value in combos:
	for location in range(1,len(value)-1):
		temp_value = list(value)
		temp_value.insert(location,'*')
		for equals_location in range(location+2,len(temp_value)):
			new_temp_value = temp_value
			new_temp_value.insert(equals_location,'==')
			string_ver = ''.join(new_temp_value)
			is_pandigital_prod = eval(string_ver)
			if(is_pandigital_prod):
				product = int(string_ver.split('==')[1])
				products.append(int(product))
				print(string_ver)
			new_temp_value.pop(equals_location)

products = set(products)
print(products)
print(sum(products))