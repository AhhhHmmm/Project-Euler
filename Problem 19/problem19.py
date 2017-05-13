count = 0
start_year = 1901
final_year = 2000

year = start_year
first_day_of_month = (1+365) % 7 #january 1, 1900 was monday, but we are starting in 1901
month = 1
while year < 2001:
	if year % 4 == 0:
		print(year)
		leap = 29
	else:
		leap = 28
	day_dict = {1:31,2:leap,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
	while month < 13:
		if year == 2000:
			print('\t' + str(month))
		first_day_of_month = (first_day_of_month + day_dict[month]) % 7
		if first_day_of_month == 0:
			count += 1
		month += 1
	month = 1
	year += 1

print('\n\n')
print(count)