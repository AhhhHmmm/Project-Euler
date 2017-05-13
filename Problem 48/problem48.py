
start_num = 1
last_num = 1000

current_num = start_num
total = 0
while current_num <= last_num:
	total += current_num**current_num
	current_num += 1

print(total)
print(str(total)[-10:])