
best = 0
len_longest = 0

def long_divide(numerator,denominator):
	remainder_list = []
	remainder = 0
	while numerator != 0 and remainder not in remainder_list[:-1]:
		quotient = numerator // denominator
		while quotient == 0:
			if remainder_list:
				remainder_list.append(0)
			numerator = 10 * numerator
			quotient = numerator // denominator
		quotient = numerator // denominator
		remainder = numerator % denominator
		numerator = 10*remainder
		remainder_list.append(remainder)
	if numerator == 0:
			return(0)
	#print(remainder_list)
	return(len(remainder_list)-1)

current = 2

while current < 1000:
	current_len_rep = long_divide(1,current)
	if current_len_rep > len_longest:
		len_longest = current_len_rep
		best = current
	current += 1

print('1/' + str(best) + ', gives a repeating pattern of ' + str(len_longest) + ' digits.')