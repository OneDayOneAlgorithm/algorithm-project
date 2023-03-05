'''
Problem!!! 후위 표기법 계산
'''

'''
Idea!!! 후위 표기법
강의 자료 계산기에 있는 방법을 사용하자

기본 아이디어 :

문자열을 list로 받아서, 공백 제거

피연산자는 stack에 push,
연산자는 만나면 계산한다.
for c -> f
    if c no in operator:
        ~~
연산자는 문자로 받았기 때문에 각 경우 ['*', '-', '/', '+']를 모두 작성해야 한다.
    else
        if c == '.' : print(result)
        if c == '*' : push(n1*n2)
        ....

추가적인 두가지 조건 (error!)
만약, 끝이 났는데 stack에 남은 수의 개수가 2 이상인 경우
ex) 222+.
만약, 연산자를 만났는데 stack에 남은 수의 개수가 1개 
ex) 2+
'''

T = int(input())

for tc in range(1, T + 1):
    f = list(input().split())  # 글자는 리스트로 받는다. -> 공백은 제거 !
    stack = []  # 피연산자를 push할 sta- `ck
    operator = ['*', '-', '/', '+', '.']  # 연산자 모음 +'.'
    result = 'error'  # 결과, 출력할 값
    for c in f:  # 문자열 리스트를 하나씩 돌린다.
        if c not in operator:  # operator(연산자)모음에 없는 문자라면 피연산자임!
            stack.append(int(c))  # 정수형으로 바꿔서 push!
        else:  # operator 모음에 있는 문자인 경우
            if c == '.':  # '.'은 끝에서 만난다.
                if len(stack) == 1:  # 만약 이경우 남아있는 stack의 길이가 1이라면
                    result = stack[-1]  # 출력할 값 = 남아있는 수 ( 모든 계산이 끝난 값)
                    break  # 멈춤 밑에는 하지마
            else:  # '.'이 아닌 경우
                if len(stack) == 1:  # stack에 있는 수가 1개라면 오류 -> break해버림
                    break
            n2 = stack.pop()  # n2는 가장 위에 쌓여있는 수
            n1 = stack.pop()  # n1은 그 다음으로 쌓여있던 수
            if c == '*':  # 만약 이 문자라면, 계산해서 넣는다.
                stack.append(n1 * n2)
            elif c == '/':
                stack.append(n1 // n2)
            elif c == '+':
                stack.append(n1 + n2)
            elif c == '-':
                stack.append(n1 - n2)
    print(f'#{tc} {result}')