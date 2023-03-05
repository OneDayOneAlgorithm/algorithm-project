T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = list(input().split())
    first = arr[:(N+1) // 2]
    second = arr[(N+1) // 2:]
    lst = []
    for i in range(N//2):
        lst.append(first.pop(0))
        lst.append(second.pop(0))
    if first:
        lst.append((first.pop()))
    print(f'#{tc}', *lst)
