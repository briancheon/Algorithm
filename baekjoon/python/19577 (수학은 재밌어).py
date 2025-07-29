import sys
import random

def miller_rabin(n, k=5):
	if n <= 1:
		return False

	if n <= 3:
		return True
		
	if n % 2 == 0:
		return False
	
	s, d = 0, n - 1
	while d % 2 == 0:
		d //= 2
		s += 1
		
	for _ in range(k):
		a = random.randrange(2, n - 1)
		x = pow(a, d, n)
		if x == 1 or x == n - 1:
			continue
		
		for _ in range(s - 1):
			x = pow(x, 2, n)
			if x == n - 1:
				break
				
		else:
			return False
			
	return True

def gcd(a, b):
    if a < b: 
        a, b = b, a
    
    while b:
        a, b = b, a % b
    
    return a

def rho(n):
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
			return rho(n)

	if miller_rabin(d):
		return d

	return rho(d)

def factorize(n):
    if n == 1:
        return []
    
    if miller_rabin(n):
        return [n]
    
    factor = rho(n)
    return factorize(factor) + factorize(n // factor)

def euler_phi(n):
    if n == 0:
        return 0
    factors = set(factorize(n))
    result = n
    for p in factors:
        result -= result // p
    return result

def get_factors(n):
    factors = set()
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            factors.add(i)
            factors.add(n // i)
    return sorted(factors)

N = int(sys.stdin.readline().rstrip())

if N == 1:
    print(1)

else:
    factors = get_factors(N)

    for k in factors:
        if k * euler_phi(k) == N:
            print(k)
            break
    else:
        print(-1)