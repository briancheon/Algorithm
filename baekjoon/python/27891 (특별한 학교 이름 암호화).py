import sys

names = {
    "northlondo": "NLCS",
    "branksomeh": "BHA",
    "koreainter": "KIS",
    "stjohnsbur": "SJA"
}

alphabet = "abcdefghijklmnopqrstuvwxyz"
cipher = list(sys.stdin.readline().rstrip())
while ''.join(cipher) not in names.keys():
    for i in range(10):
        cipher[i] = alphabet[(ord(cipher[i]) - 97 + 1) % 26]

print(names[''.join(cipher)])


