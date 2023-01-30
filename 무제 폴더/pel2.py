import sys
sys.stdin =open("input.txt" , "r")

def check(lst):
    for i in range(len(lst)//2):
        if lst[i] != lst[-i-1]:
            return False
    return True

for test_case in range(1,11):
    T = int(input())
    arr = [list(input()) for _ in range(100)]
    arr2 = list(zip(*arr))
    maxlen = 1

    for length in range(100,1,-1):
        if maxlen >= length:
            break
        for idx in range(100-length+1):
            if maxlen == length:
                break
            for lst, lst2 in zip(arr,arr2):
                if check(lst[idx:idx+length]) or check(lst2[idx:idx+length]):
                    maxlen = length
                    break
    print('#{} {}'.format(test_case, maxlen))
