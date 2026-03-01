import random

# Assume it is implemented
def gcd(a, b):
	...

# Assume it is implemented
def miller_rabin(n):
	...

def pollard_rho(n):
	def f(x, c):
		return (x * x % n + c) % n
	
	if n == 1:
		return 1

	if miller_rabin(n):
		return n

	if n % 2 == 0:
		return 2

	for p in [3, 5, 7, 11, 13, 17, 19, 23, 29, 31]:
		if n % p == 0:
			return p

	x = random.randrange(2, n)
	c = random.randrange(1, n)
	y = x
	d = 1

	while d == 1:
		x = f(x, c)
		y = f(f(y, c), c)
		
		d = gcd(abs(x - y), n)
		if d == n:
			return pollard_rho(n)

	if miller_rabin(d):
		return d

	return pollard_rho(d)