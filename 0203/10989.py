import sys
input = sys.stdin.readline
N = int(input())
cnt = [0] * 10001
for i in range(N):
    # number = int(input())
    cnt[int(input())] += 1 # [0,2,2,2,1,2,1]
for i in range(10001):
    if cnt[i] != 0:
        for j in range(cnt[i]):
            print(i)
