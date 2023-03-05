import sys
sys.stdin = open('input.txt')
for tc in range(10):
    T = int(input())
    lst = [list(map(int, input().split())) for _ in range(100)]

    max1 = []
    # 가로로 더한 값들을 리스트에 넣는다
    for i in range(100):
        sum = 0
        for j in range(100):
            sum += lst[i][j]
        max1.append(sum)
    # 세로로 더한 값들을 리스트에 넣는다
    for i in range(100):
        sum = 0
        for j in range(100):
            sum += lst[j][i]
        max1.append(sum)
    # 대각을 더한 값들을 리스트에 넣는다
    for i in range(100):
        sum = 0
        sum += lst[i][i]
        max1.append(sum)
    # 반대 대각을 더한 값들을 리스트에 넣는다
    for i in range(100):
        sum = 0
        sum += lst[i][-i-1]
        max1.append(sum)
    print(f'#{T} {max(max1)}')
