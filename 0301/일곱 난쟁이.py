lst = []
for i in range(9):
    lst.append(int(input()))
over_value = sum(lst) - 100 # 나쁜놈의 합 찾기
lst.sort()  # 전체를 정렬한다 오름차순으로
t = 0
for i in range(8):  # 01 02 03 04 05 06 07 08 12 13 14 15 16 17 18 23 24 25 26 27 28
    for j in range(i+1,9):  # i번째랑
        if lst[i]+lst[j] == over_value:
            lst[i] = 0
            lst[j] = 0
            t = 1
            break
    if t == 1:
        break

for i in lst:
    if i != 0:
        print(i)
