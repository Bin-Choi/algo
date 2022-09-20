for test_case in range(1, T+1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]
    old_st = []
    for st in arr:
        if st != old_st and st.count('1')!=0:
            old_st = st
            bst =''
            for ch in st:
                bst += dct1[ch]

            old = 0
            cnts = []
            for i in range(len(bst)):
                if bst[old] != bst[i]:
                    cnts.append(i-old)
                    old = i

            pwd = []
            for i in range(1, len(cnts), 4):
                mn = min(cnts[i:i+3])
                key = str(cnts[i]//mn)+str(cnts[i+1]//)
                pwd.append(dct3[key])

            ans = []
            for i in range(0, len(pwd), 8):

