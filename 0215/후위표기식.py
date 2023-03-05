isp = {'*': 2, '/': 2, '+': 1, '-': 1,'(': 0 }
icp = {'*': 2, '/': 2, '+': 1, '-': 1,'(': 3 }
# (6+5*(2-8)/2)
# '2+3*4/5'  >> 234*5/+
# 2 3 4 5 / * +
data = input()
stack = []
#피연산자는 그냥 출력
#연산자는 우선순위에 따라서 stack넣거나, 빼고 넣기
#   stack의 top의 우선순위보다 token의 우선순위가 높으면 그냥 stack에 넣어주기
#   아니면...높거나 같은애들은 다빼고 낮은애가 나오면 push
# 닫히는 괄호나오면 여는 괄호나올때 까지 pop 하면서 출력하기
for i in range(len(data)):
    # data[i]
    if data[i] in '0123456789':
        print(data[i],end='')
    else: # 연산자
        if data[i] == ')':
            #여는 괄호가 나올때까지 pop하면서 연산자 출력
            while stack[-1] != '(':
                print(stack.pop(),end='')
            #여는 괄호 버리기
            stack.pop()
        elif not stack:   #스택이 비어있으면
            stack.append(data[i])
        else:   # 스택이 비어있지 않으면 우선순위를 따집시다.
            if isp[stack[-1]]< icp[data[i]]:
                stack.append(data[i])
            else:
                # 나보다 작은애가 나올때 까지 pop하면서 출력 + 스택이 비어있지 않으면서
                while stack and isp[stack[-1]] >= icp[data[i]]:
                    print(stack.pop(),end='')
                stack.append(data[i])
#수식을 다 읽었을 때 stack에 연산자가 남아 있으면 pop() 하면서 출력
while stack:
    print(stack.pop(),end='')
print()
