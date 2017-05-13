def convert_base_two(num):
	highest_pow = 0
	temp_num = num
	binary_val = ''
	while 2**(highest_pow+1) <= num:
		highest_pow += 1
	for power in range(highest_pow,-1,-1):
		digit = temp_num//(2**power)
		binary_val += str(digit)
		temp_num = temp_num % (2**power)
	return(binary_val)

def test_palindrome(num_dec):
	str_num_dec = str(num_dec)
	rev_num_dec = str_num_dec[::-1]
	pal_base_ten = False
	pal_base_two = False
	super_pal = False
	if str_num_dec == rev_num_dec:
		pal_base_ten = True
		#print(str_num_dec + ' is a palindrome in base 10!')
	str_num_bin = str(convert_base_two(num_dec))
	rev_num_bin = str_num_bin[::-1]
	if str_num_bin == rev_num_bin:
		pal_base_two = True
		#print(str_num_bin + ' is equivalent to ' + str_num_dec + ' and is a palindrome in base 2!')
	if pal_base_two and pal_base_ten:
		super_pal = True
		print(str_num_dec + ' is a super pal!')
	return(super_pal)

start = 1
end = 10**6
total = 0
for value in range(start,end):
	if test_palindrome(value):
		total += value

print(total)
