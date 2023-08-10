import sys
sys.stdin = open("input.txt", "r")

N = int(input())

m_list = []
p_list = []
o_list = []
ans = 0

for i in range(N):
    n = int(input())
    if n > 1:
        p_list.append(n)
    elif n == 1:
        o_list.append(n)
    else:
        m_list.append(n)

p_list.sort(reverse=True)
m_list.sort()

if len(p_list) % 2 == 1:
    ans += p_list[len(p_list)-1]
    for j in range(0, len(p_list)-1, 2):
        ans += p_list[j] * p_list[j+1]
else:
    for j in range(0, len(p_list), 2):
        ans += p_list[j] * p_list[j+1]

if len(m_list) % 2 == 1:
    ans += m_list[len(m_list)-1]
    for j in range(0, len(m_list)-1, 2):
        ans += m_list[j] * m_list[j+1]
else:
    for j in range(0, len(m_list), 2):
        ans += m_list[j] * m_list[j+1]

for j in range(len(o_list)):
    ans += o_list[j]

print(ans)



