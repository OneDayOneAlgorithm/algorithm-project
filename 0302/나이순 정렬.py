import sys
N = int(sys.stdin.readline())
lst = []
for i in range(N):
    a,b = input().split()
    a = int(a)
    lst.append((a,b))
lst.sort(key=lambda x : x[0])
for i in lst:
    print(*i)