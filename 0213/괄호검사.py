def check_bracket(data):
    stack = []                                  # 빈 리스트를 만든다
    for c in data:                              # data의 각 문자들에 대하여
        if c == '(':                            # 만약 문자가 열린 괄호면
            stack.append(c)                     # 리스트에 열린 괄호를 넣는다.
        elif c == ')':                          # 만약 문자가 닫힌괄호라면
            if not stack:                       # 만약 스택이 비어 있으면
                return 0                        # 0을 반환하고
            elif stack[-1] == '(':              # 리스트 마지막 원소가 열린 괄호라면
                stack.pop()                     # 그렇지 않으면 마지막 원소를 삭제한다
            else:
                return 0
        elif c == '{':                          # 만약 문자가 열린 중괄호라면
            stack.append(c)                     # 이를 리스트에 추가한다
        elif c == '}':                          # 만약 문자가 닫힌 중괄호라면
            if not stack:                       # 만약 스택이 비어 있으면
                return 0                        # 0을 반환하고
            elif stack[-1] == '{':              # 마지막 원소가 열린 중괄호라면
                stack.pop()                     # 그렇지 않으면 마지막 원소를 삭제한다
            else:
                return 0                        # 0을 반환한다
    if stack:                                   # 만약 리스트에 원소가 있으면
        return 0                                # 0을 반환하고
    return 1                                    # 빈 리스트가 되었다면 1을 반환한다

T = int(input())
for tc in range(1, T + 1):
    data = input()
    result = check_bracket(data)
    print(f'#{tc} {result}')
