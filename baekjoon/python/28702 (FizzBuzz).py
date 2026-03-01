import sys

def FizzBuzz(n):
    fizzbuzz = ""
    if n % 3 == 0:
        fizzbuzz += "Fizz"
    if n % 5 == 0:
        fizzbuzz += "Buzz"

    return fizzbuzz if fizzbuzz else n

n1 = sys.stdin.readline().rstrip()
n2 = sys.stdin.readline().rstrip()
n3 = sys.stdin.readline().rstrip()

if n1.isnumeric():
    print(FizzBuzz(int(n1) + 3))

elif n2.isnumeric():
    print(FizzBuzz(int(n2) + 2))

else:
    print(FizzBuzz(int(n3) + 1))
