start = 1
stop = 1000

ones_dict = {1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine'}
teens_dict = {10:'ten',11:'eleven',12:'twelve',13:'thirteen',14:'fourteen',15:'fifteen',16:'sixteen',17:'seventeen',18:'eighteen',19:'nineteen'}
tens_dict = {2:'twenty',3:'thirty',4:'forty',5:'fifty',6:'sixty',7:'seventy',8:'eighty',9:'ninety'}

def count_letters(num):
	letters = ''
	remaining = num
	if remaining // 1000 > 0:
		thou_dig = remaining // 1000
		letters += ones_dict[thou_dig]
		letters += 'thousand'
		remaining = remaining % 1000
	if remaining // 100 > 0:
		hund_dig = remaining // 100
		letters += ones_dict[hund_dig]
		letters += 'hundred'
		remaining = remaining % 100
	if remaining > 0 and letters:
		letters += 'and'
	if remaining in teens_dict.keys():
		letters += teens_dict[remaining]
		remaining = 0
	elif remaining // 10 > 0:
		tens_dig = remaining // 10
		letters += tens_dict[tens_dig]
		remaining = remaining % 10
	if remaining // 1 > 0:
		ones_dig = remaining // 1
		letters += ones_dict[ones_dig]
		remining = remaining % 1
	count = len(letters)
	return(letters,count)

# letters, count = count_letters(1000)
# print(str(letters) + ' has ' + str(count) + ' letters.')

current = start
total = 0
while current <= stop:
	letters, count = count_letters(current)
	# print(str(letters) + ' has ' + str(count) + ' letters.')
	total += count
	current += 1

print(total)