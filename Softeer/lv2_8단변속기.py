import sys
sys.stdin = open("input.txt", "r")
gear = list(map(int, input().split()))

gear_a = sorted(gear)
gear_b = sorted(gear, reverse=True)

if gear == gear_a:
    print("ascending")
elif gear == gear_b:
    print("descending")
else:
    print("mixed")