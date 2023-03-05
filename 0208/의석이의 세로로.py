T = int(input())
for tc in range(1, T + 1):
    arr = [list(input()) for _ in range(5)]  # 2중배열만들기
    N = len(arr[0])
    for i in range(5):
        if N < len(arr[i]):
            N = len(arr[i])  # 가장 긴 리스트의 길이
    for i in range(5):
        while len(arr[i]) < N:  # 가장 긴 리스트의 길이보다 짧으면 공백'' 추가
            arr[i].append('')

    word = ''  # 변수 word를 ''로 초기화(나중에 문자 더할거임)
    for i in range(N):
        for j in range(5):
            word += arr[j][i]  # word에 왼쪽 문자부터 순서대로 더함
    for row in arr:
        print(len(row))
    print(f'#{tc} {word}')
