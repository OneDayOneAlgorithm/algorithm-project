import string  # A부터 Z를 받아온다

T = int(input())  # 테스트케이스입력 후
for tc in range(1, T + 1):  # 반복한다.
    N = int(input())  # 제목의 갯수를 입력받고
    lst = []  # 제목의 앞글자만 넣을 빈 리스트를 만든다
    for i in range(N):
        lst.append(input()[0])  # 빈 리스트에 제목으 앞글자만 넣고
    lst = set(lst)  # 셋으로 바꿔 중복된 글자들을 없애고
    lst = list(lst)  # 다시 리스트로 만들고
    lst.sort()  # 오름차순으로 정렬한다.
    q = [i for i in string.ascii_uppercase]  # q에는 A부터 Z까지의 값을 넣는다.
    cnt = 0  # 연속된 알파벳이 몇개 있는지 카운트하는 변수를 만든다.
    for i in range(len(q)):  # A부터Z까지 순서대로 비교한다.
        if lst[i] == q[i]:  # 글자가 같으면
            cnt += 1  # 카운트하고
        else:  # 글자가 다르면
            break  # 즉시 종료하고
    print(f'#{tc} {cnt}')  # 카운트 값을 출력한다.
