def f(i, N):
    if i == N:              #순열 완성
        print(P)
    else:
        for j in range(i, N):
            P[i], P[j] = P[j]
            f(i+1, N)
            P[i], P[j] = P[j]

P = [1,2,3]
f(0, 3)

