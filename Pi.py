from math import acos
import sys
# Function that prints the
# value of pi upto N
# decimal places
def printValueOfPi(N) :

	# Find value of pi upto
	# using acos() function
	b = '{:.' + str(N) + 'f}'
	pi= b.format(2 * acos(0.0))
	
	
	# Print value of pi upto
	# N decimal places
	print(pi);

# Driver Code
if __name__ == "__main__" :

	for i in range(1,len(sys.argv)):
	    N = int(sys.argv[i])

	# Function that prints
	# the value of pi
printValueOfPi(N)
