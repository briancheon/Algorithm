import sys

S = sys.stdin.readline().rstrip()

korea, yonsei = iter("KOREA"), iter("YONSEI")

ck, cy = next(korea), next(yonsei)

for s in S:
    if s == ck:
        ck = next(korea, None)
        if ck is None:
            print("KOREA")
            break

    if s == cy:
        cy = next(yonsei, None)
        if cy is None:
            print("YONSEI")
            break

