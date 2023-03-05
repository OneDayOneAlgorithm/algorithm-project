import sys
sys.stdin = open('input1.txt')
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    cnt = [0] * 5001
    for i in range(N):
        A, B = map(int,input().split())
        for j in range(A,B + 1):
            cnt[j] += 1
    P = int(input())
    c = list()
    for i in range(P):
        c.append(cnt[int(input())])
    print(f'#{tc}', *c)
