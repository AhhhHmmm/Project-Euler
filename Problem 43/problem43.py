import itertools

total = 0
divisors = [2,3,5,7,11,13,17]
perms = itertools.permutations('0123456789',10)

def check_divisible(value):
	sub_string_divisible = True
	# if value[0] == 0:
	# 	sub_string_divisible = False
	for index in range(len(divisors)):
		sub_string = value[index+1:index+4]
		#print(sub_string)
		if int(sub_string) % divisors[index] != 0:
			sub_string_divisible = False
			break
	if sub_string_divisible:
		print(value + ' is substring divisible!')
	return(sub_string_divisible)

for value in perms:
	value = ''.join(list(value))
	sub_string_divisible = check_divisible(value)
	if sub_string_divisible:
		total += int(value)

print(total)