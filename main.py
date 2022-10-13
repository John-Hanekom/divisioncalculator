# Created by: John Hanekom
# Date: October 13th, 2022
# 
# This program divides two inputted numbers through repeated subtraction.

def main():
	remainder = 0
	calc = int(input('input the divident/numerator: '))
	divident = int(input('input the divisor/denominator: '))
	divisor = calc
	while calc >= divident:
		calc -= divident
		remainder += 1
		print(divisor," divided by: ",divident," is equal to:")
		print(remainder," with a remainder of: ",calc,".")
	main()
main()