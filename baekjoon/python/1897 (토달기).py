import sys

alphabets = "abcdefghijklmnopqrstuvwxyz"

d, teacher = sys.stdin.readline().split()
d = int(d)

dictionary = set(sys.stdin.readline().rstrip() for _ in range(d))

memo = {}

def longest_extension(word):
    if word in memo:
        return memo[word]
    
    best = word
    for pos in range(len(word) + 1):
        for ch in alphabets:
            new_word = word[:pos] + ch + word[pos:]
            if new_word in dictionary and len(new_word) == len(word) + 1:
                candidate = longest_extension(new_word)
                if len(candidate) > len(best):
                    best = candidate
    
    memo[word] = best
    return best

result = longest_extension(teacher)
print(result)