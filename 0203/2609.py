A, B = map(int,input().split())
def func(A, B):
    while B > 0:
        A, B = B, A % B
    return A
def func2(A, B):
    return A * B // func(A, B)
print(func(A, B))
print(func2(A, B))