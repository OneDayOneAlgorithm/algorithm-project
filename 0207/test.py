def binarySearch(a, N, key):
    start = 0
    end = N - 1
    while start <= end:
        mid = (start + end) // 2
        if a[mid] == key:
            return mid
        elif a[mid] < key:
            start = mid + 1
        else:
            end = mid - 1
    return -1


arr = [1, 5, 8, 17, 20, 25, 35, 44]
print(binarySearch(arr, 8, 35))
