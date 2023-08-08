import sys
sys.stdin = open("input.txt", "r")

N = int(input())
lst = []
for i in range(N):
    sm, sd, em, ed = map(int, input().split())
    sm *= 100
    em *= 100
    lst.append([sm+sd, em+ed])

lst.sort(key=lambda x: (x[0], x[1]))
cnt = 0
end = 0
start = 301

while lst:
    # 12/1일 넘어간 경우, 꽃의 공백이 생긴 경우
    if start > 1130 or start < lst[0][0]:
        break

    for _ in range(len(lst)):
        # 직전 꽃이 지는 시점 또는 지기 전에 피는 꽃인 경우(꽃의 공백이 없는 경우)
        if start >= lst[0][0]:
            # 직전 꽃 보다 늦게 지는 경우
            if end <= lst[0][1]:
                # 해당 꽃 심을게 ~~~~ (직전 꽃이 지기 전에 피면서 가장 늦게 지는 꽃을 찾는 과정)
                end = lst[0][1]
            # 심던지, 안 심던지 기간이 겹치는 꽃이면 제거~
            lst.remove(lst[0])

        # 직전 꽃이 지기 전에 피는 꽃이 없다
        else:
            break
    start = end
    cnt += 1

if start <= 1130:
    print(0)
else:
    print(cnt)

