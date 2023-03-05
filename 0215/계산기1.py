for tc in range(1,11):
    N = int(input())
    arr = list(map(int,input().split('+')))
    print(f'#{tc} {sum(arr)}')