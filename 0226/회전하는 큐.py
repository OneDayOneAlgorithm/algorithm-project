N,M = map(int,input().split())
arr = list(map(int,input().split()))
q = [i for i in range(1,N+1)]
cnt = 0
while arr:
    if q[0] == arr[0]:
        q.pop(0)
        arr.pop(0)
    else:
        if (q.index(arr[0])) > len(q) // 2:
            while q[0] != arr[0]:
                q.insert(0,q.pop())
                cnt += 1
        else:
            while q[0] != arr[0]:
                q.append(q.pop(0))
                cnt += 1


print(cnt)

