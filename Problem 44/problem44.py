import itertools

def gen_pent(n):
	pent_num = n*(3*n-1)/2
	return(pent_num)

max_n = 10000
pent_nums = []
for value in range(1,max_n):
	pent_nums.append(gen_pent(value))

#print(pent_nums)

combos = itertools.combinations(pent_nums,2)
for combo in combos:
	list_combo = list(combo)
	list_combo.reverse()
	sum_of_pents = sum(list_combo)
	diff_of_pents = list_combo[0] - list_combo[1]
	if sum_of_pents in pent_nums and diff_of_pents in pent_nums:
		print(list_combo)
		print(diff_of_pents)
		print('\n')