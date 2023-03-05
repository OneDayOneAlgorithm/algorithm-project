arr = [1,2,3]
N = len(arr)
used = [0] * N
arr_prt = [0] * N
def solve(idx):
    if idx ==N:
        print(arr_prt)
        return
    for i in range(N):
        if not used[i]:
            arr_prt[idx] = arr[i]
            used[i] = 1
            solve(idx+1)
            used[i] = 0
solve(0)