T = int(input())
for tc in range(1, T+1):
    arr = list(map(int, input().split()))
    A, B = [0]*10, [0]*10
    ans = 0
    for i in range(12):
        if ans:
            break
        if i % 2 == 0:
            A[arr[i]] += 1
            for j in range(10):
                if A[j] == 3:
                    ans = 1
            if len(A) >= 3:
                for k in range(len(A)-2):
                    if A[k] > 0 and A[k+1] > 0 and A[k+2] > 0:
                        ans = 1

        else:
            B[arr[i]] += 1
            for j in range(10):
                if B[j] == 3:
                    ans = 2
            if len(B) >= 3:
                for k in range(len(B)-2):
                    if B[k] > 0 and B[k+1] > 0 and B[k+2] > 0:
                        ans = 2
    print(A)
    print(B)
    print(f'#{tc} {ans}')
