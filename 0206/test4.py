# 부분집합
arr = [3, 6, 7, 1, 5, 4]
n = len(arr)

for i in range(1 << n):  # n = 6이므로 6쉬프트 레프트
    for j in range(n):
        if i & (1 << j):  # i의 j번째 비트 확인
            print(arr[j], end=", ")

    print()
print()

# i가 60일 때 60의 0번째 비트 ~ 5번째 비트를 확인
# 010110010010 의 0번째 ~ 5번째 비트를 확인
# 비트가 1인게 2개다. 5, 6 출력
