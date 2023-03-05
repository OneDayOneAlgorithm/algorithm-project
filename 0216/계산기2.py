import sys
sys.stdin = open('계산기2.txt')
def change(arr):                                # 후위 뭐시기로 만드는 함수
    stack = []
    sum_v = ''
    for i in arr:
        if i in '0123456789':
            sum_v += i
        elif i == '*':
            while stack and stack[-1] == '*':
                sum_v += stack.pop()
            stack.append(i)
        elif i =='+':
            while stack:
                sum_v += stack.pop()
            stack.append(i)
    while stack:
        sum_v += stack.pop()
    return cal(sum_v)                           # 중요! cal 함수가 리턴한 값을 리턴해야함
def cal(sum_v):                                 # 후위 표기식을 계산하는 함수
    stack = []
    for i in sum_v:
        if i in '0123456789':
            stack.append(i)
        elif i == '*':
            a = stack.pop()
            b = stack.pop()
            c = int(b) * int(a)
            stack.append(c)
        elif i == '+':
            a = stack.pop()
            b = stack.pop()
            c = int(b) + int(a)
            stack.append(c)
    return stack[0]                              # 계산값을 리턴해준다
for tc in range(1,11):
    T = int(input())
    arr = input()
    print(f'#{tc} {change(arr)}')