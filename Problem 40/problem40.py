big_dec = ''

for value in range(1,10**6):
	big_dec += str(value)

prod = 1
for value in range(0,7):
	prod *= int(big_dec[10**value - 1])

print(prod)

# print(len(big_dec))