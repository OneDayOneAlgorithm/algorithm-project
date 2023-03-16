def solve(n):
    if len(n) == len(A):  # 입력값의 자릿수가 A와 일치하고
        if int(n) < B and n[0] != '0':  # B보다 크고 맨 앞자리 수가 0이 아니면
            lst.append(int(n))  # 이를 배열 lst에 추가하고
            return  # 함수 종료
        else:  # B보다 크거나 맨 앞자리 수가 0이면
            return  # 즉시 종료
    for i in range(len(A)):  # A의 인덱스번호를 가져와서
        if used[i] == 0:  # 사용하지 않은 인덱스 번호일 경우
            used[i] = 1  # # 사용 하고있음을 표시하고
            solve(n + A[i])  # 그 인덱스를 사용해 재귀를 돌린다.
            used[i] = 0  # 재귀에서 돌아오면 인덱스를 사용하지 않고있음을 표시한다.


A, B = map(int, input().split())  # 수열을 바꿀 수 A, 최대 값 기준이 될 수 B
A = str(A)  # A를 인덱스를 사용하기위해 문자열로 바꾼다.
used = [0] * len(A)  # 인덱스 재사용 방지를 위해 used 배열 생성
lst = []  # A의 수열을 바꿀 때마다 배열 lst에 저장
solve('')  # A의 수열들을 배열 lst에 저장할 함수 solve() 실행
if lst:  # 배열 리스트의 원소가 존재한다면
    print(max(lst))  # 리스트의 원소중 값이 가장 큰 원소를 출력한다.
else:  # 리스트가 비었을 경우에는 -1을 출력한다.
    print(-1)
