import sys
sys.stdin = open("input.txt", "r")

n, m = map(int, input().split())  # n개의 회의실, m개의 예약된 회의
rooms = {}

for _ in range(n):
    room = input()  # 회의실 이름 입력
    rooms[room] = [0] * 18 + [1]  # 예약시간 초기화

for i in range(m):
    r, s, t = input().split()  # 회의실이름, 시작시각, 종료시각 입력
    s = int(s)
    t = int(t)
    for i in range(s, t):
        rooms[r][i] = 1

# 회의실 이름 오름차순으로 회의실 정보 출력
rooms = dict(sorted(rooms.items()))

for index, room in enumerate(rooms):
    print(f'Room {room}:')
    times = []
    current = 1
    for i in range(9, 19):
        if current == 1 and rooms[room][i] == 0:
            start = i
            current = 0
        elif current == 0 and rooms[room][i] == 1:
            end = i
            current = 1
            times.append([start, end])
    # if current == 0:
    #     times.append([start,18])

    if len(times) == 0:
        print('Not available')
    else:
        print(f'{len(times)} available:')
        for x in times:
            print(f'{x[0]:02d}-{x[1]}')

    # 구분선
    if index != len(rooms) - 1:
        print('-----')


# 내가 만든 마지막 시간 계산 & 출력부분 (테스트 케이스 부분 실패)

# check3 = list([] for _ in range(N))
# for i in range(n):
#     stk = []
#     for j in range(9, 19):
#         if rooms[i][j] == 0:
#             if stk:
#                 if stk[-1][1] == j:
#                     stk[-1][1] = j+1
#                 else:
#                     stk.append([j, j+1])
#             else:
#                 stk.append([j, j+1])
#     if stk:
#         for time in stk:
#             s = str(time[0])
#             if time[0] == 9:
#                 s = '09'
#             e = str(time[1])
#             check3[i].append(s+'-'+e)
#
# for i in range(N):
#     print('Room' + ' ' + Rooms[i]+':')
#     cnt = str(len(check3[i]))
#     if cnt == '0':
#         print('NOT available')
#         print('-----')
#         continue
#
#     print(cnt+' '+'available:')
#     for book in check3[i]:
#         print(book)
#     if i != N-1:
#         print('-----')
