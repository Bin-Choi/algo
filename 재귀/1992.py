import sys
sys.stdin = open("input.txt", "r")

n = int(input())
arr = [list(map(int, input())) for _ in range(n)]
ans = []


def quad(n, r, c):

    # 더이상 나눌 수 없을 때,
    if n == 1:
        ans.append(str(arr[r][c]))
        return

    # 압축 가능 체크
    flag = int(0)

    for i in range(n):
        for j in range(n):
            if arr[r][c] != arr[r+i][c+j]:
                flag = 1
                break
        if flag == 1:
            break

    # 압축 가능
    if flag == 0:
        ans.append(str(arr[r][c]))
        return
    # 불가능 -> 4분할
    else:
        n = int(n/2)
        ans.append("(")
        for i in range(2):
            for j in range(2):
                quad(n, r+(n*i), c+(n*j))
        ans.append(")")


quad(n, 0, 0)
print(''.join(ans))
