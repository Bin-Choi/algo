N = int(input())
towers = list(map(int, input().split()))
stack1 = []
stack2 = towers[::-1]
ans = []
for j in range(N):
    if len(stack1) == 0:
        stack1.append(stack2.pop())
        ans.append(0)
    else:
        stack1.append(stack2.pop())
        k = len(stack1)
        for i in range(k):
            if stack1[k-1] < stack1[k-1-i]:

                ans.append(k-i)
                break
        else:
            ans.append(0)


print(ans)

