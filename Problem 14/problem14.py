
def collatz_count(num):
	count = 1
	while num != 1:
		if num % 2 == 0:
			num = num / 2
		else:
			num = 3*num+1
		count += 1
	return(count)

current_max = 0
best_val = 0
current_value = 1
highest_val = 1000000

while current_value < highest_val:
	collatz_val = collatz_count(current_value)
	if collatz_val > current_max:
		current_max = collatz_val
		best_val = current_value
	current_value += 1

print(best_val)