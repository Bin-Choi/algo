import sys
sys.stdin = open("input.txt", "r")

# T = int(input())
# for test_case in range(1, T+1):
#     N = int(input())
#     X = -1
#     for i in range(1, int(N*0.5)):
#         if i*i*i == N:
#             X = i
#     print(f'#{test_case} {X}')

num = [0] * (10**6 + 1)
for i in range(1, 10**6+1):
    num[i] = i**3

T = int(input())
for test_case in range(1, T+1):
    N = int(input())

    try:
        print(f'#{test_case} {num.index(N)}')

    except:
        print(f'#{test_case}' ' -1')

