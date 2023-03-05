import sys
sys.stdin = open('qqq.txt')

def solve(n):
    if n > N:
        return
    solve(n*2)
    solve(n*2 + 1)
    stack.append(tree[n])
    if stack[-1] == '-':
        stack.pop()
        b = int(stack.pop())
        c = int(stack.pop())
        d = c - b
        stack.append(d)
    elif stack[-1] == '+':
        stack.pop()
        b = int(stack.pop())
        c = int(stack.pop())
        d = c + b
        stack.append(d)
    elif stack[-1] == '*':
        stack.pop()
        b = int(stack.pop())
        c = int(stack.pop())
        d = c * b
        stack.append(d)
    elif stack[-1] == '/':
        stack.pop()
        b = int(stack.pop())
        c = int(stack.pop())
        d = c // b
        stack.append(d)


for tc in range(1,11):
    N = int(input())
    tree = [''] * (N+1)
    for i in range(1,N+1):
        arr = list(input().split())
        tree[i] = arr[1]
    stack = []
    solve(1)

    print(f'#{tc} {stack[0]}')
