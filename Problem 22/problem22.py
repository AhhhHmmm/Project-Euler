import string

file = 'data.txt'

alphabet = list(string.ascii_uppercase)
print(alphabet)

name_list = []
with open(file) as f:
	for line in f:
		name_list = line.split('\",\"')
		name_list = sorted(name_list)

total = 0
entry_num = 1
for name in name_list:
	temp_sum = 0
	for letter in name:
		letter_num = alphabet.index(letter) + 1
		temp_sum += letter_num
	temp_total = temp_sum * entry_num
	total += temp_total
	entry_num += 1

print(total)