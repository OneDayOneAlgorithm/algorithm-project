def solve():
    global N
    sum = ''
    while N != 1:
        N = N * 2
        sum += str(N)[0]
        if len(sum) > 12:
            return 'overflow'
        if N > 1:
            N = N - 1
    return sum

T = int(input())
for tc in range(1,T+1):
    N = float(input())
    print(f'#{tc} {solve()}')


