import sys
sys.setrecursionlimit(10**6)
num_list = []   # 빈 리스트 만들기
while True: 
    try:
        num = int(input())  # 입력
        num_list.append(num)    # 입력값을 리스트에 추가
    except:
        break   # 입력받지 않으면 종료


def postorder(first, end):  # 함수생성
    if first > end: #
        return
    mid = end + 1  # 루트보다 큰 값이 존재하지 않을 경우를 대비
    for i in range(first + 1, end + 1): #루트 값보다 큰 값을 찾는다
        if num_list[first] < num_list[i]:   # 찾는다면
            mid = i # 그 인덱스를 미드로 둔다
            break   # 그리고 종료

    postorder(first + 1, mid - 1)   # 루트값보다 큰 값이 없다면 왼쪽으로 가서 재귀한다
    postorder(mid, end) # 그래도 못찾는다면 루트값 오른쪽으로 재귀한다
    print(num_list[first])


postorder(0, len(num_list) - 1) # 함수실행 시작값은 0번 인덱스, 도착값은 마지막 인덱스