#분해합 구하기

def d_sum(number, len_num):

    nm = str(number)
    s_sum = number
    for i in range(len_num):
        s_sum += int(nm[i])
    return s_sum


N = int(input())
ans = 0
min = 1000000
l = len(str(N))
s = N - (9*l)
if s < 1:
    s = 1

# 수의 범위에 대한 분해합 검정
for num in range(s, N+1):
    s_um = d_sum(num, len(str(num)))
    if s_um == N and num <= min:
        min = num

if min != 1000000:
    ans = min
print(ans)