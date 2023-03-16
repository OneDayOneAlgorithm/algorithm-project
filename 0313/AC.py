import sys

input = sys.stdin.readline  # 입력 속도 빠르게 하기
T = int(input())  # 테스트 케이스 입력
for _ in range(T):  # 테스트 케이스 만큼 반복
    p = input()  # R,D 입력
    N = int(input())  # 숫자 갯수 입력
    arr = input().rstrip()[1:-1].split(',')  # 괄호 [ ] 없애고 오른쪽 공백 없애고
    q = []  # queue만들기
    for i in range(N):
        q.append(arr[i])  # q에 숫자들 넣기
    status = 1  # 1일때는 앞의 숫자 제거 -1일 때는 뒤의 숫자제거
    flag = 1  # 1일때는 에러없이 정상출력 0일때는 에러출력
    for i in p:  # R과 D에 대해
        if i == 'R':  # R일 때
            if status == 1:  # status를 반대로한다
                status = -1
            else:
                status = 1
        elif i == 'D':  # D일 때
            if q:  # q 원소가 1개 이상일 때
                if status == 1:  # status가 1이면
                    q.pop(0)  # 앞의 원소를 제거하고
                else:  # status가 0이면
                    q.pop()  # 뒤의 원소를 제거한다.
            else:  # q의 원소가 없으면
                print('error')  # 에러출력하고
                flag = 0  # flag에 0을 넣는다.
                break
    if flag:  # flag가 1이면 아래와 같이 정상출력한다.
        if status == 1:
            print("[", end="")
            print(*q, sep=",", end="")
            print("]")
        else:
            q.reverse()
            print("[", end="")
            print(*q, sep=",", end="")
            print("]")
