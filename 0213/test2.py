S = '(afds(aa)asdf)'
stack = [0] * len(S)    # 스택 만들기
top = -1                # top 초기화
for c in S:             # 문자 하나씩 반복
    if c == '(':        # 열릴 괄호일 경우
        top += 1        # top 1증가시키고
        stack[top] = c  # 그 인덱스에 문자 할당
    elif c == ')':      # 닫힌 괄호인 경우
        top -= 1        # top 1감소시키는데
        if top < -1:    # 만약 top 이 -1 보다 작으면
            raise Indexerror('가득 차있습니다.')   # 에러발생시킴
if top == -1:           # 만약 top이 -1 이면
    print(True)         # 괄호의 짝이 맞다
else:                   # 아니면
    print(False)        # 짝이 맞지 않다

