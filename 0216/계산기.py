T = int(input())
for tc in range(1,T+1):
    data = input().split()
    data.pop()
    stack = []
    for i in range(len(data)):                  # data의 길이만큼 반복
        try:
            if data[i] not in ['+','-','*','/']:             # data의 i번 인덱스가 숫자이면
                stack.append(data[i])
            else:                                   # 연산자면
                if data[i] == '+':
                    a = int(stack.pop())
                    b = int(stack.pop())
                    c = b + a
                    stack.append(c)
                elif data[i] == '-':
                    a = int(stack.pop())
                    b = int(stack.pop())
                    c = b - a
                    stack.append(c)
                elif data[i] == '*':
                    a = int(stack.pop())
                    b = int(stack.pop())
                    c = b * a
                    stack.append(c)
                elif data[i] == '/':
                    a = int(stack.pop())
                    b = int(stack.pop())
                    c = b // a
                    stack.append(c)
        except:
            stack.append('error')
    print(f'#{tc} {stack[-1]}')