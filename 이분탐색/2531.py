N, d, k, c = map(int, input().split())
belt = []
for i in range(N):
    belt.append(int(input()))

max_s = 0

for i in range(N):
    eat_s = 1
    check = [0] * (d+1)
    check[c] = 1
    for j in range(i, i+k):
        sushi = belt[j % N]

        if not check[sushi]:
            eat_s += 1
        check[sushi] += 1

    max_s = max(max_s, eat_s)

print(max_s)
