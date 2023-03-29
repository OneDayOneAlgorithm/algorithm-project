def dfs(n):
    global ans
    if n==N:
        ans = max(ans,int(''.join(map(str,lst))))
        return
    # L개에서 2개뽑는 모든 조합(둘을 교환)
    for i in range(L-1):
        for j in range(i+1,L):
            lst[i], lst[j] = lst[j], lst[i]
            chk = int(''.join(map(str,lst)))*10+n       # 가지치기
            if chk not in v:
                dfs(n+1)
                v.append(chk)                           # 가지치기
            lst[i],lst[j] = lst[j], lst[i]  # 원상복구
T = int(input())
for tc in range(1,T+1):
    st,t=input().split()
    N = int(t)
    lst=[]
    for ch in st:
        lst.append(int(ch))
    L = len(lst)
    ans = 0
    v = []
    dfs(0)
    print(f'#{tc} ')