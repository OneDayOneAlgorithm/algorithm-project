def binary_search(arr,key,s,e):
    turn = 0
    while s<=e:
        mid = (s+e) // 2
        if arr[mid] == key:
            return True
        elif arr[mid] > key:
            e = mid - 1
            if turn == 1:
                break
            turn =1
        else:
            s = mid + 1
            if turn == -1:
                break
            turn =-1
    return False

T = int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    A.sort()
    cnt = 0
    for i in B:
        if binary_search(A,i,0,len(A)-1):
            cnt += 1
    print(f'#{tc} {cnt}')