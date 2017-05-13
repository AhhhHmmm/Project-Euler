import matplotlib as mpl
import matplotlib.pyplot as plt

def collatz_count(num):
	count = 1
	while num != 1:
		if num % 2 == 0:
			num = num / 2
		else:
			num = 3*num+1
		count += 1
	return(count)

current_max = 0
best_val = 0
current_value = 1
highest_val = 10000

x_vals = []
y_vals = []

while current_value < highest_val:
	collatz_val = collatz_count(current_value)
	x_vals.append(current_value)
	y_vals.append(collatz_val)
	if collatz_val > current_max:
		current_max = collatz_val
		best_val = current_value
	current_value += 1

print(best_val)

plt.figure(1)

# scatter
plt.subplot(121)
plt.plot(x_vals,y_vals,'o',markersize = 3)
plt.title('Start Value vs. Termination Time')

# histogram
plt.subplot(122)
plt.hist(y_vals,bins=50,rwidth=0.8)
plt.title('Histogram')

plt.show()
