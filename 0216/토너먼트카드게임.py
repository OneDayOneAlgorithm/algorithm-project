def func(start, end):                           # 함수 정의
    if start == end:                            # 시작점과 마지막 점이 같으면
        return start                            # 나vs나 중복이므로 부전승하게 된다
    a = func(start, (start + end) // 2)         # 시작점은 그대로 마지막 점은 절반지점
    b = func((start + end) // 2 + 1, end)       # 시작점은 절반지점 + 1, 마지막 점은 그대로
    if arr[a] == 1:                             # 만약 왼쪽 사람이 가위를 내면
        if arr[b] == 1:                         # 오른쪽 사람이 가위를 내면
            return a                            # 왼쪽 사람 리턴
        elif arr[b] == 2:                       # 오른쪽 사람이 묵을 내면
            return b                            # 왼쪽 사람 리턴
        elif arr[b] == 3:                       # 오른쪽 사람이 보를 내면
            return a                            # 왼쪽 사람 리턴
    if arr[a] == 2:
        if arr[b] == 2:
            return a
        elif arr[b] == 3:
            return b
        elif arr[b] == 1:
            return a
    if arr[a] == 3:
        if arr[b] == 3:
            return a
        elif arr[b] == 1:
            return b
        elif arr[b] == 2:
            return a
T = int(input())                                # 테스트 케이스 입력
for tc in range(1,T+1):                         # 테스트 케이스 반복
    N = int(input())                            # 총 대결하는 사람 숫자ㅓ
    arr = [0] + list(map(int,input().split()))  # 낸 데이터를 쭉 나열. 이 때 맨 앞에 0을 넣어 인덱스에러 방지
    print(f'#{tc} {func(1,N)}')                 # 출력


