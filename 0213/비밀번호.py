import sys
sys.stdin = open('비밀번호.txt')
T = 10
for tc in range(1,T+1):
    N, arr = input().split()    # 입력나누기
    lst = []                    # 빈리스트 만들기
    for i in arr:               # 어레이반복
        if lst:                 # 빈리스트가아니면
            if lst[-1] == i:    # 마지막단어와 현재단어가 같으면
                lst.pop()       # 마지막 단어 삭제
            else:
                lst.append(i)   # 다르다면 현재단어를추가
        else:
            lst.append(i)       # 빈리스트면 현재단어 추가
    result = ''.join(lst)       # 리스트를 문자열로만들기
    print(f'#{tc} {result}')    # 출력
