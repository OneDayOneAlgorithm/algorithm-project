def partition(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr)//2
    left = partition(arr[:mid])
    right = partition(arr[mid:])
    return merge(left,right)

def merge(left,right):
    global cnt
    left_N = len(left)
    right_N = len(right)
    result = [0] * (left_N + right_N)
    left_i, right_i = 0, 0
    i = 0
    if left[-1] > right[-1]:
        cnt += 1

    while left_i<len(left) and right_i<len(right):
        if left_i < left_N and right_i < right_N:
            if left[left_i] <= right[right_i]:
                result[i] = left[left_i]
                i += 1
                left_i += 1
            else:
                result[i] = right[right_i]
                i += 1
                right_i += 1

        elif left_i < left_N:
            result[i] = left[left_i]
            i += 1
            left_i += 1
        elif right_i < right_N:
            result[i] = right[right_i]
            i += 1
            right_i += 1
            # print(result)
        return result




T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = list(map(int,input().split()))
    cnt = 0
    ans = partition(arr)
    print(f'#{tc} {ans[N//2]} {cnt}')


```
def partition(lst):

    if len(lst) <= 1:
        return lst
    mid = len(lst)//2
    left_lst = partition(lst[:mid])
    right_lst = partition(lst[mid:])
    return merge(left_lst, right_lst)


def merge(left_lst, right_lst):
    global cnt
    left_N = len(left_lst)
    right_N = len(right_lst)
    result = [0]*(left_N+right_N)
    left_i, right_i = 0, 0
    i = 0
    if left_lst[-1] > right_lst[-1]:
        cnt += 1

    while left_i < left_N or right_i < right_N:
        if left_i < left_N and right_i < right_N:
            if left_lst[left_i] <= right_lst[right_i]:
                result[i] = left_lst[left_i]
                i += 1
                left_i += 1
            else:
                result[i] = right_lst[right_i]
                i += 1
                right_i += 1

        elif left_i < left_N:
            result[i] = left_lst[left_i]
            i += 1
            left_i += 1
        elif right_i < right_N:
            result[i] = right_lst[right_i]
            i += 1
            right_i += 1
    #print(result)
    return result


T = int(input())

for test_case in range(1, T + 1):
    cnt = 0
    N = int(input())
    lst = list(map(int, input().split()))
    Data = partition(lst)

    print(f'#{test_case} {Data[N//2]} {cnt}')
```