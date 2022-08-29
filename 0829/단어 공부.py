import sys
sys.stdin = open("input.txt", "r")

Word = input()
Word = Word.upper()

cnt = [0] * 92
mx = idx = 0
err = 0
for w in range(len(Word)):
    cnt[ord(Word[w])] += 1

for i in range(65, 91):
    if cnt[i] > mx:
        mx = cnt[i]
        idx = i

for j in range(65, 91):
    if cnt[j] == mx:
        err += 1

if err == 1:
    print(chr(idx))
else:
    print('?')