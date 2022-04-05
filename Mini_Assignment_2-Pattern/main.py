# Print Pascal's Triangle in Python
from math import factorial

# input n
n = int(input('Enter the number of rows: '))

for i in range(n):
	for j in range(n):

		# nCr = n!/((n-r)!*r!)
		if(j>i):
			print('0',end="")
		else:
			print(factorial(i)//(factorial(j)*factorial(i-j)), end="")
	print("")

