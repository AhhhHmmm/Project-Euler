
start = 2
stop = 100

num_list = []
for a in range(start,stop+1):
	for b in range(start,stop+1):
		num_list.append(a**b)

num_list = list(set(num_list))
num_list = sorted(num_list)
print(len(num_list))