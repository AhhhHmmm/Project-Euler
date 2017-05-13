import math

input_val = 100

def solve_problem(input_val):
	total_val = 0
	fact_str = str(math.factorial(input_val))
	while fact_str:
		current_val = fact_str[0]
		total_val += int(current_val)
		fact_str = fact_str[1:]
	return(total_val)

print(solve_problem(input_val))
