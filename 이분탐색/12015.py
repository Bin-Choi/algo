import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

LIS = [A[0]]


def find(e):
    start = 0
    end = len(LIS) - 1

    while start <= end:
        mid = (start + end) // 2

        if LIS[mid] == e:
            return mid
        elif LIS[mid] < e:
            start = mid + 1
        else:
            end = mid - 1

    return start


for num in A:
    if LIS[-1] < num:
        LIS.append(num)
    else:
        idx = find(num)
        LIS[idx] = num


print(len(LIS))
