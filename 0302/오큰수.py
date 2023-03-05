import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
stack = []  # 맨 뒤에서 부터 세며 그때마다 숫자를 넣는다
ans = []  # 답을 넣을 리스트
for i in range(N - 1, -1, -1):  # 맨뒤에서 부터 센다
    while stack and arr[i] >= stack[-1]:  # 스택의 숫자가 현재숫자보다 작으면
        stack.pop()  # 스택의 숫자를 버린다. 이걸 계속 반복한다.
    if not stack:  # 스택이 만약에 비었으면
        ans.append(-1)  # -1을 답안 리스트에 넣는다.
    else:
        ans.append(stack[-1])  # 스택이 안비었으면 스택 맨뒤 숫자를 답안 리스트에 넣는다.
    stack.append(arr[i])  # 현재숫자를 스택에 넣는다.
ans.reverse()  # 답안 리스트를 반대로 한다.
print(*ans)  # 출력한다.
