T = int(input())
for _ in range(T):
    N,ans = map(int,input().split())
    arr = list(map(int,input().split()))
    q = []
    cnt = 1
    for i in range(N):
        q.append((arr[i],i))    # q를 value 와 index로 정렬
    arr.sort(reverse=True)      # arr를 내림차순으로 정렬

    while q:
        if q[0][0] == arr[0]:   # q[0]과 arr[0]이 같을 시
            if q[0][1] == ans:  # q의 인덱스가 내가 찾는 값일 시
               print(cnt)       # 출력
               break
            q.pop(0),arr.pop(0) # 내가 찾는 값이 아니면 둘다 팝하고
            cnt += 1            # 카운트
        else:
            q.append(q.pop(0))  # q[0]과 arr[0]이 다를시 q[0]을 맨 뒤로 보낸다


