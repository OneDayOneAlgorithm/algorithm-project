def partition(lst): 

    if len(lst) <= 1:   # 배열의 길이가 1이되면
        return lst      # 쪼개기를 끝낸다.
    mid = len(lst)//2   # 배열의 길이가 1이 아닐 시 더 쪼개기 위해 mid 를 구한다.
    left_lst = partition(lst[:mid]) # 그리고 mid를 기준으로 쪼갠다.
    right_lst = partition(lst[mid:])
    return merge(left_lst, right_lst)   # 쪼갠 두 배열을 정렬한다. 처음엔 1개짜리배열... 그다음 2개짜리배열...


def merge(left_lst, right_lst): # 쪼갠 두 배열을 정렬하는 함수
    global cnt  
    left_N = len(left_lst)      # 쪼개고난 왼쪽 배열의 길이
    right_N = len(right_lst)    # 쪼개고난 오른쪽 배열의 길이
    result = [0]*(left_N+right_N)   # 정렬할 전체 배열의 길이만큼 0으로 채운다.
    left_i, right_i = 0, 0          # 인덱스를 0으로 초기화한다.
    i = 0
    if left_lst[-1] > right_lst[-1]:    # 문제에서 요구하는 가장 오른쪽 값을 비교해여 왼쪽 배열의 크기가 클때를 센다.
        cnt += 1

    while left_i < left_N or right_i < right_N:         # 이제 왼쪽배열과 오른쪽 배열을 정렬한다.
        if left_i < left_N and right_i < right_N:         # 왼쪽 배열과 오른쪽 배열에 원소가 둘 다 남아있으면
            if left_lst[left_i] <= right_lst[right_i]:      # 왼쪽 배열이 작을 시
                result[i] = left_lst[left_i]                # 왼쪽배열을 결과값에 넣고
                i += 1                                      # 전체 인덱스와
                left_i += 1                                 # 왼쪽 배열 인덱스를 증가시킨다.
            else:                                          # 오른쪽 배열이 작을 시 (이하 생략)
                result[i] = right_lst[right_i]
                i += 1
                right_i += 1

        elif left_i < left_N:                 # 왼쪽 배열에 원소가 남아있으면
            result[i] = left_lst[left_i]      # 결과값에 왼쪽 배열 원소들를 모두 추가한다.
            i += 1
            left_i += 1
        elif right_i < right_N:                 # 오른쪽 배열에 원소가 남아있으면 (이하생략)
            result[i] = right_lst[right_i]
            i += 1
            right_i += 1
    #print(result)
    return result                           # 결과값을 출력한다.


T = int(input())

for tc in range(1, T + 1):
    cnt = 0
    N = int(input())
    lst = list(map(int, input().split()))
    Data = partition(lst)   # 재병합 결과 배열을 Data에 저장한다.

    print(f'#{tc} {Data[N//2]} {cnt}')  # Data의 중간의 값과 cnt를 출력한다.
