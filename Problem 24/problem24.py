import itertools

perm_num = 1000000

digits = [0,1,2,3,4,5,6,7,8,9]
# digits = [0,1,2]

perms = itertools.permutations(digits)

count = 1
for perm in perms:
	if count == perm_num:
		perm_string = ''
		for value in perm:
			perm_string += str(value)
		print(perm_string)
	count += 1
