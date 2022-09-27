import sys
sys.stdin = open("input.txt", "r")

def mergesort(lst):
    global cnt
    if len(lst)<2:
        return lst
    m = len(lst)//2
    left = mergesort(lst[:m])
    right = mergesort(lst[m:])

    if left[-1] > right[-1]:
        cnt += 1

    ret = []
    l = r = 0
    while l<len(left) and r < len(right):
        if left[l] < right[r]:
            ret.append(left[l])
            l += 1
        else:
            ret.append(right[r])
            r += 1
    ret += left[l:] + right[r]
    return ret


T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))
    cnt = 0
    lst = mergesort(lst)
    print(f'#{test_case} {lst[N//2]} {cnt}')