def merge_sort(arr,s,e):
    if s == e:
        return
    mid = (s+e) // 2
    merge_sort(arr,s,mid)
    merge_sort(arr,mid+1,e)
    merge(arr,s,mid,e)

def merge(arr,s,m,e):
    temp = []
    i = s       # 앞 인덱스
    j = m+1     # 뒤 인덱스
    while i <= m and j <= e:    # 인덱스가 아직 남아있다면
        if arr[i] < arr[j]:     # 앞 인덱스가 더 작으면
            temp.append(arr[i])  # 앞 인덱스를 temp에 추가
            i += 1              # 앞 인덱스 1 증가
        else:                       # 뒤 인덱스가 더크면
            temp.append(arr[j])     # 동일하게 시행
            j += 1
    while i <= m:
        temp.append(arr[i])
        i += 1
    while j <= e:
        temp.append(arr[j])
        j += 1
    x=0
    for i in range(s,e+1):
        arr[i] = temp[x]
        x+=1

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = list(map(int,input().split()))
    merge_sort(arr,0,len(arr)-1)
    print(f'#{tc} {arr[N//2]}')