def solve():
    c = 0  # c(current) 현재 값을 0으로 둔다 0에서 시작하기 때문
    cnt = 0  # 0에서 1로 또는 1에서 0으로 몇번 바뀌는지 cnt로 센다
    for i in range(len(arr)):  # i가 0이라고 가정할 때
        if arr[i] != c:  # 문자열의 첫번째 값이 0이 아니면
            c = not c  # c를 1로 바꾸고
            cnt += 1  # 카운트한다
    return cnt  # 몇번 카운트 했는지 반환한다


T = int(input())
for tc in range(1, T + 1):
    arr = list(map(int, input()))  # 숫자로 이루어진 리스트를 만든다
    ans = solve()
    print(f'#{tc} {ans}')
