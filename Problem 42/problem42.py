import string

alphabet = string.ascii_uppercase

def get_sum(word):
	total = 0
	for letter in word:
		letter_pos = alphabet.index(letter) + 1
		total += letter_pos
	return(total)

def check_triangle_num(total):
	triangle = False
	solution = (-1+(1+8*total)**0.5)/2
	if float(solution).is_integer():
		triangle = True
	return(triangle)

count = 0
file = 'p042_words.txt'
with open(file, 'r') as f:
	for line in f:
		line = line[1:-1]
		words = line.split('\",\"')
		print(words)

for word in words:
	word_sum = get_sum(word)
	triangle = check_triangle_num(word_sum)
	if triangle:
		count += 1

print(count)