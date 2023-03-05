def solve():
    lst = [i for i in range(1,N+1)]
    for i in range(len(lst)):
        cnt = 0
        for j in str(lst[i]):
            if j in ('3','6','9'):
                cnt += 1
        if cnt >0:
            lst[i] = '-'*cnt
    return lst

N = int(input())
print(*solve())