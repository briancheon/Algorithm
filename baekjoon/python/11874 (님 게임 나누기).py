import sys

N = int(sys.stdin.readline().rstrip())
A = list(map(int, sys.stdin.readline().split()))

nim_sum = 0
for a in A:
	if a == 0:
		Ga = 0
	
	elif (a + 1) % 4 == 0:
		Ga = a + 1
		
	elif a % 4 == 0:
		Ga = a - 1
		
	else:
		Ga = a
		
	nim_sum ^= Ga
	
print("koosaga" if nim_sum else "cubelover")