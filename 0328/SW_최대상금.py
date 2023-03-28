def solve(n):
    global sum_v
    if n == change:
        tmp = int(''.join(arr))
        if arr < tmp:
            arr = tmp
        return
    for i in range(N):
        for j in range(i+1, N):
            arr[i], arr[j] = arr[j], arr[i]
            changed_arr = ''.join(arr)
            if visited[]


T = int(input())
for tc in range(1, T+1):
    arr, change = input().split()
    arr = list(arr)
    change = int(change)
    N = len(arr)
    sum_v = 0
    visited = [0]*N
    solve(change)
