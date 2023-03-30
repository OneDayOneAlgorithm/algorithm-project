N = int(input())
lst = []
for i in range(N):
    A, B = map(int, input().split())
    lst.append([A, B, i])
    lst.sort(key=lambda x: x[0], reverse=True)
stack = []
value = 0
for i in range(N):
    if not stack:
        value += 1
        lst[i].append(value)    # 몇등인지 입력한다
        stack.append(lst[i][1])  # 키를 스택에 넣는다
    elif lst[i][1] <= stack[-1]:  # 앞사람보다 키가 작거나 같으면 덩치가 작은 것이므로
        value += 1              # 등수를 낮추고
        lst[i].append(value)    # 그 등수를 배정한다.
        stack.pop()  # 그리고 스택을 초기화한다.
    else:   # 앞사람보다 키가 크면
        lst[i].append(value)    # 앞사람과 같은 등수를 배정한다.
print(lst)
