# https://www.geeksforgeeks.org/sieve-of-eratosthenes/

'''
Given a number n, print all primes smaller than or equal to n. It is also given that n is a small number

Input : n =10
Output : 2 3 5 7 

Input : n = 20 
Output: 2 3 5 7 11 13 17 19
'''
'''
n = 50
We create a list of all numbers from 2 to 50.  
According to the algorithm we will mark all the numbers which are divisible by 2 and are greater than or equal to the square of it. 
Now we move to our next unmarked number 3 and mark all the numbers which are multiples of 3 and are greater than or equal to the square of it.  
We move to our next unmarked number 5 and mark all multiples of 5 and are greater than or equal to the square of it.  
We continue this process
'''

def SieveOfEratosthenes(n):
	# Create a boolean array
	# "prime[0..n]" and initialize
	# all entries it as true.
	# A value in prime[i] will
	# finally be false if i is
	# Not a prime, else true.
	prime = [True for i in range(n+1)]
	p = 2
	while (p * p <= n):
		# If prime[p] is not
		# changed, then it is a prime
		if (prime[p] == True):
			# Update all multiples of p
			for i in range(p * p, n+1, p):
				prime[i] = False
		p += 1
	# Print all prime numbers
	for p in range(2, n+1):
		if prime[p]:
			print(p)

# Driver code
if __name__ == '__main__':
	n = 20
	print("Following are the prime numbers smaller"),
	print("than or equal to", n)
	SieveOfEratosthenes(n)

'''
Time Complexity: O(n*log(log(n)))
Auxiliary Space: O(n)
'''





# Python program for the above approach
Primes = [0] * 500001
def SieveOfEratosthenes(n) :
	Primes[0] = 1
	i = 3
	while(i*i <= n) :
		if (Primes[i // 2] == 0) :
			for j in range(3 * i, n+1, 2 * i) :
				Primes[j // 2] = 1
		i += 2
		
# Driver Code
if __name__ == "__main__":
	n = 100
	SieveOfEratosthenes(n)
	for i in range(1, n+1) :
		if (i == 2) :
			print( i, end = " ")
		elif (i % 2 == 1 and Primes[i // 2] == 0) :
			print( i, end = " ")
	
'''
Time Complexity: O(n*log(log(n)))
Auxiliary Space: O(1)
'''
  
  
  
# How is the time complexity of Sieve of Eratosthenes is n*log(log(n))?
# Solution: https://www.geeksforgeeks.org/how-is-the-time-complexity-of-sieve-of-eratosthenes-is-nloglogn/
  
