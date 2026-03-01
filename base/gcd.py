# Implementation of the Eucledian Algorithm
def gcd(a, b):
    while b:
        a, b = b, a % b

    return a