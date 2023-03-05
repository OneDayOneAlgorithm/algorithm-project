T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = list(map(int,input().split()))
    cnt = 1
    max = 0
    for i in range(1,N):
        if arr[i] != arr[i-1] + 1:
            cnt = 0
        cnt += 1
        if max < cnt:
            max = cnt
        
    print(f'#{tc} {max}')