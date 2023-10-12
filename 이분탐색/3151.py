from bisect import bisect_left
import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N = int(input())
students = list(map(int, input().split()))
students.sort()

answer = 0
for i in range(len(students)-2):
    left, right = i+1, N-1
    while left < right:
        result = students[i] + students[left] + students[right]
        if result > 0:
            right -= 1
        else:
            if result == 0:
                if students[left] == students[right]:
                    answer += (right-left)
                else:
                    idx = bisect_left(students, students[right])
                    answer += (right-idx+1)
            left += 1

print(answer)