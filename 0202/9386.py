T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    number = list(map(int,input())) # [0,0,1,1,0,0,1,1,1,0]
    count = 0
    lst = []
    for i in range(0, N):
        if number[i] == 1:
            count += 1
            lst.append(count) 
        else:
            count = 0
    # lst = [1,2,1,2,3]
    # max함수 대신 사용
    max = lst[0]
    for i in lst:
        if max < i:
            max = i
    print(f'#{tc} {max}')