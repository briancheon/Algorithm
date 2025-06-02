N, A = map(int, input().split())

add_inverse = N - A

try:
    mul_inverse = pow(A, -1, N)

except ValueError:
    mul_inverse = -1

print(add_inverse, mul_inverse)

