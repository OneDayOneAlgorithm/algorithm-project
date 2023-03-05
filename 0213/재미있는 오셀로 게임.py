import sys
sys.stdin = open('오셀로.txt')
T = int(input())
for tc in range(T):
    N,M = map(int,input().split())
    board = [[0] * N in range(N)]
    for i in range(M):
