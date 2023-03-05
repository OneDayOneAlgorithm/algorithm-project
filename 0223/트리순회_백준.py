def func1(N):
    if N != '.':
        print(N,end = '')
        func1(tree[N][0])
        func1(tree[N][1])
def func2(N):
    if N != '.':
        func2(tree[N][0])
        print(N, end='')
        func2(tree[N][1])
def func3(N):
    if N != '.':
        func3(tree[N][0])
        func3(tree[N][1])
        print(N, end='')
N = int(input())
tree = {}
for _ in range(N):
    node,left,right = input().split()
    tree[node] = [left,right]
func1('A')
print()
func2('A')
print()
func3('A')
print()

