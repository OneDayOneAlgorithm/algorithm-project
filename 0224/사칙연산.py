import sys
sys.stdin = open('사직연산.txt')

def solve(V):
    if type(tree[V][0]) == int:
        return tree[V][0]
    left_result = solve(tree[V][1])
    right_result = solve(tree[V][2])
    if tree[V][0] == '+':
        return left_result + right_result
    elif tree[V][0] == '-':
        return left_result - right_result
    elif tree[V][0] == '*':
        return left_result * right_result
    elif tree[V][0] == '/':
        return left_result // right_result



for tc in range(1,11):
    N = int(input())
    tree = [[0]*3 for _ in range(N+1)]
    for _ in range(N):
        data = input().split()
        #4개 아니면 2개
        idx = int(data[0])
        if len(data) == 4:
            # 0 : 노드번호 1 : value 2: 왼쪽자식 3: 오른쪽 자식
            tree[idx][0] = data[1]
            tree[idx][1] = int(data[2])
            tree[idx][2] = int(data[3])

        else:
            tree[idx][0] = int(data[1])
    result = solve(1)
    print(f'#{tc} {int(result)}')