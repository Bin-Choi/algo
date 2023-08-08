import sys
sys.stdin = open("input.txt", "r")


def small_sum(a):
    value = 0
    tmp = list(map(str, a.split("+")))
    for t in tmp:
        value += int(t)
    return value


lst = list(map(str, input().split("-")))
answer = 0

for i in range(len(lst)):
    s_sum = small_sum(lst[i])
    if i == 0:
        answer += s_sum
    else:
        answer -= s_sum

print(answer)