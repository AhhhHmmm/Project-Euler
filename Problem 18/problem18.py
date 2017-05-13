
file = 'bigdata.txt'
all_rows = []


with open(file,'r') as f:
	for row in f:
		row=row.strip()
		row_list = row.split()
		for index in range(len(row_list)):
			row_list[index] = int(row_list[index])
		all_rows.append(row_list)

while len(all_rows) > 1:
	current_row = all_rows.pop()
	row_before = all_rows[-1]
	length = len(row_before)
	index = 0
	while index < length:
		max_of_pair = max(current_row[index],current_row[index+1])
		row_before[index] = row_before[index] + max_of_pair
		index += 1

print(all_rows)

