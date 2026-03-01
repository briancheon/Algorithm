import random

def miller_rabin(n, k=5):  # Number of tests
	if n <= 1:
		return False

	if n <= 3:
		return True
		
	if n % 2 == 0:
		return False
	
	# Step 1: Write n - 1 as 2^s * d
	s, d = 0, n - 1
	while d % 2 == 0:
		d //= 2
		s += 1
		
	# Step 2: Witness loop
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
			return False  # Composite
			
	return True  # Probably prime`