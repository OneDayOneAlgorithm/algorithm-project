N = int(input())
lst = []
for i in range(N):
    a,b = map(int,input().split())
    lst.append((a,b))
for i in range(N-1):
    maxv = lst[i]
    for j in range(i+1,N):
        if lst[j][0] > lst[i][0]:
            maxv = lst[j]
    lst[i] = lst[j]
print(lst)

