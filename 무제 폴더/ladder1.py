import sys
sys.stdin =open("input.txt" , "r")

T = 3
# T = int(input())
for test_case in range(1, T+1):
    _=int(input())
    N = 100
    arr = [list(map(int,input().split())) for _ in range(N)]

    i,j = N-1, 9
    #[1] 목적지(출발지) arr[][] == 2
    for tj in range(N):
        if arr[i][tj] == 2:
            j = tj
            break
    while i > 0:
        if j>0 and arr[i][j-1]==1:            #왼쪽
            arr[i][j] == 0
            j-=1
        elif j <99 and arr[i][j+1]==1:      #오른쪽
            arr[i][j] == 0
            j+=1
        else :
            i-=1

    print(f'#{test_case} {j}')