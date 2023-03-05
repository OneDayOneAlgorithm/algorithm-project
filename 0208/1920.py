N = int(input())
standard = list(map(int, input().split()))
M = int(input())
arr = list(map(int, input().split()))
standard.sort()  # 정렬
for i in range(M):  # 밑의 줄 젤 왼쪽 숫자가
    start = 0
    end = N - 1
    isExist = False
    while start <= end:  # 위의 줄에 있는지 찾기
        mid = (start + end) // 2
        if standard[mid] == arr[i]:
            isExist = True
            print(1)
            break
        elif standard[mid] < arr[i]:
            start = mid + 1
        else:
            end = mid - 1
    if not isExist:
        print(0)
