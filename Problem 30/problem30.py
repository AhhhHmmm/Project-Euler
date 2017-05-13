
start = 2
end = 355000


totaltotal = 0
index = start
while index < end:
	total = 0
	str_index = str(index)
	while str_index:
		total += int(str_index[0])**5
		str_index = str_index[1:]
	if index == total:
			print(index)
			totaltotal += index
	index += 1

print(totaltotal)