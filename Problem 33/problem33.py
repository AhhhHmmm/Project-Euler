import itertools

numbers = range(1,10)

perms = itertools.permutations(numbers,3)

num_prod = 1
denom_prod = 1

for perm in perms:
	rep_number, top_num, bottom_num = list(perm)
	rep_number = str(rep_number)
	top_num = str(top_num)
	bottom_num = str(bottom_num)
	frac = bottom_num + rep_number  + '.0/' + rep_number + top_num
	bad_frac = bottom_num + '.0/' +  top_num
	if eval(frac) == eval(bad_frac):
		frac = bottom_num + rep_number  + '/' + rep_number + top_num
		bad_frac = bottom_num + '/' +  top_num
		num, denom = bad_frac.split('/')
		num_prod *= int(num)
		denom_prod *= int(denom)

print(num_prod)
print(denom_prod)