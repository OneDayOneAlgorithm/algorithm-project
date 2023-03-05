arr = [1,2,3,4,5]
N = len(arr)
selected = [0] * N

# idx 에 해당하는 요소가 부분집합에 포함되는지 아닌지 결정
# 결정하고나서 다음 요소 포함여부 결정하러 ㄱㄱ
def subset(idx):
    if idx == N:
        # N-1번 요소까지 결정이 끝난 상황
        print(selected)
        return 
    #완전탐색 : 내가 할 수 있는거 다 해보면 됩니다.
    selected[idx] = 1
    subset(idx + 1)
    selected[idx] = 0
    subset(idx + 1)


subset(0)
'''
'''
def f(i,k,key):
    if i ==k:
        s = 0
        for j in range(k):
            if bit[j]:
                s += A[j]
        if s == key:
            for j in range(k):
                if bit[i]:
                    print(A[j], end=' ')
                print()

    else:
        bit[i] = 1
        f(i+1,k,key)
        bit[i] = 0
        f(i+1,k,key)
A = [1,2,3,4,5,6,7,8,9,10]
N = len(A)
key = 10
bit = [0] * N
f(0,N,key)