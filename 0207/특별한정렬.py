
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    a = list(map(int, input().split()))
    # 선택 정렬로 내림차순을 만든다.
    for i in range(N - 1): 
        max_idx = i

        for j in range(i + 1, N):  
            if a[max_idx] < a[j]:
                max_idx = j

        a[i], a[max_idx] = a[max_idx], a[i]
    # 선택정렬로 사이사이 끼워 넣는다.
    for i in range(1, N, 2):
        min_idx = i

        for j in range(i + 1, N):  
            if a[min_idx] > a[j]:
                min_idx = j
        a.insert(i, a[min_idx])
    # 10개만 빈 리스트에 추가한다            
    lst = []
    for i in range(10):
        lst.append(a[i])
    print(f'#{tc}', *lst)
