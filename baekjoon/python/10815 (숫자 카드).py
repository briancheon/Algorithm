import sys

N = int(sys.stdin.readline().rstrip())

cards = set(map(int, sys.stdin.readline().split()))
card_dict = dict.fromkeys(cards, 1)

M = int(sys.stdin.readline().rstrip())
check_cards = list(map(lambda x: card_dict.get(int(x), 0), sys.stdin.readline().split()))

print(*check_cards)