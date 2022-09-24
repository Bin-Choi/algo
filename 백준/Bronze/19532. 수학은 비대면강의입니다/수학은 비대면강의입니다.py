a, b, c, d, e, f = map(int, input().split())

X = ((b*f) - (c*e)) // ((b*d) - (a*e))
Y = (c*d - a*f) // ((b*d) - (a*e))

print(X, Y)