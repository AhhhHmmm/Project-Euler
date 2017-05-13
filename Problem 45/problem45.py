import math

def is_integer(num):
	if int(num) == num:
		return(True)
	else:
		return(False)

value = 286
all_Three = False

while not all_Three:
	value += 1
	triang_num = value*(value+1)/2.0
	pent_sol = (1+math.sqrt(1-4*3*(-2*triang_num)))/6.0
	hex_sol = (1+math.sqrt(1+4*2*triang_num))/4.0
	pent_sol_is_int = is_integer(pent_sol)
	hex_sol_is_int = is_integer(hex_sol)
	if pent_sol_is_int and hex_sol_is_int:
		all_Three = True
		print(int(triang_num))
	