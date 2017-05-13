import collections

max_perim = 1001
perims = []

for a in range(1,max_perim):
	for b in range (a,max_perim-a):
		c = (a**2+b**2)**(0.5)
		if float(c).is_integer() and (a + b + c) < max_perim:
			perims.append(int(a+b+c))

print(perims)
print('*'*20)
most_common_perim = collections.Counter(perims).most_common(1)
print(most_common_perim)