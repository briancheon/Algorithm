import sys

N = int(sys.stdin.readline())

S = sys.stdin.readline()

if N <= 25:
    print(S)
else:
    if "." not in S[11:-13]:
        print((S[:11], S[:10])[S[10] == "."] + "..." + S[-12:])
    else:
        print(S[:9] + "......" + S[-11:])
