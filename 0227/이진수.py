def solve():
    global sum
    dict = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
    for i in range(N):
        for j in dict:
            if arr[i] ==j:
                arr[i] = dict[j]
    for i in range(N):
        arr[i] = int(arr[i])
        sum_tmp = ''
        for j in range(4):
            sum_tmp += str(arr[i]%2)
            arr[i] = arr[i]//2
        sum += sum_tmp[::-1]
    return sum


T = int(input())
for tc in range(1,T+1):
    N,arr = map(str,input().split())
    N = int(N)
    arr = list(arr)
    sum = ''
    print(f'#{tc} {solve()}')

