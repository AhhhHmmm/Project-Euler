tot = 1
last = 5

for dim in range(3,last,2):
	for value in range(0,4):
		tot += value*2*(dim-1)
		print(tot)

print(tot)