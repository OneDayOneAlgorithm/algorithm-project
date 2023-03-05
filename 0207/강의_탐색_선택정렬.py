'''
<검색>
-저장되어 있는 자료 중에서 원하는 항목을 찾는 작업
-목적하는 탐색 키를 가진 항목을 찾는 것
탐색키 : 자료를 구별하여 인식할 수 있는 키
-검색의 종류)
1. 순차 검색
2. 이진 검색
3. 해쉬

1. 일렬로 되어 있는 자료를 순서대로 검색하는 방법
-가장 간단하고 직관적인 검색 방법
-배열이나 연결 리스트 등 순차구조로 구현된 자료구조에서
원하는 항목을 찾을 때 유용함
-알고리즘이 단순하여 구현이 쉽지만, 검색 대상의 수가 많은 경우에는
수행시간이 급격히 증가하여 비효율적임

1.1 2가지 경우
-정렬되어 있지 않은 경우
-정렬되어 있는경우

1.2 검색 과정
-첫 번째 원소부터 순서대로 검색 대상과 키 값이 같은 원소가 있는지
비교하며 찾는다
-키 값이 동일한 원소를 찾으면 그 원소의 인덱스를 반환한다
-자료구조의 마지막에 이를 때까지 검색 대상을 찾지 못하면 검색 실패

1.3 찾고자 하는 원소의 순서에 따라 비교회수가 결정됨
-첫 번째 원소를 찾을 때는 1번 비교, 두 번째 원소를 찾을 때는 2번비교.
-정렬되지 않은 자료에서의 순차 검색의 평균 비교 회수
(1/n)*(1+2+3+..+n) = (n+1)/2
-시간 복잡도 : O(n)
'''

# 순차검색 (문자열 등의 배열, 원소의 갯수, 찾는 원소값)


def sequentialSearch(a, n, key):
    i = 0
    while i < n and a[i] != key:
        i += 1
    if i < n:
        return i
    else:
        return -1


print(sequentialSearch('abcd', 4, 'c'))

'''
1.4 검색 과정
-자료가 오름차순으로 정렬된 상태에서 검색을 실시한다고 가정하자.
-자료를 순차적으로 검색하면서 키 값을 비교하여, 원소의 키 값이
검색대상의 키 값보다 크면 찾는 원소가 없다는 것이므로 더 이상
검색하지 않고 검색을 종료한다.

2. 이진 검색
-자료의 가운데에 있는 항목의 키 값과 비교하여
다음 검색의 위치를 결정하고 검색을 계속 진행하는 방법
-목적 키를 찾을 때까지 이진 검색을 순환적으로 반복 수행함으로써
검색 범위를 반으로 줄여가면서 보다 빠르게 검색을 수행함
-이진 검색을 하기 위해서는 자료가 정렬된 상태여야 한다.

2.1 검색 과정
-자료의 중앙에 있는 원소를 고른다.
-중앙 원소의 값과 찾고자 하는 목표 값을 비교한다.
-목표 값이 중앙 원소의 값보다 작으면 자료의 왼쪽 반에 대해서
새로 검색을 수행하고, 크다면 자료의 오른쪽 반에 대해서 새로 검색을 수행한다.
-찾고자하는 값을 찾을때까지 계속 반복한다.

2.2 구현
-검색 범위의 시작점과 종료점을 이용하여 검색을 반복 수행한다.
-이진 검색의 경우, 자료에 삽입이나 삭제가 발생했을 때
배열의 상태를 항상 정렬 상태로 유지하는 추가 작업이 필요하다.
'''

# 이진 검색


def Binary_Search(arr, n, key):
    start = 0
    end = n - 1
    while start <= end:
        middle = (start + end) // 2
        if arr[middle] == key:
            return middle
        elif arr[middle] > key:
            end = middle - 1
        else:
            start = middle + 1
    return False


arr = 'abcedfg'

print(Binary_Search(arr, 7, 'g'))


'''
3. 인덱스
-인덱스라는 용어는 Database에서 유래했으며, 테이블에 대한 동작 속도를
높여주는 자료구조를 일컫는다. Database분야가 아닌 곳에서는
Look up table등의 용어를 사용하기도 한다.
-인덱스를 저장하는데 필요한 디스크 공간은 보통 테이블을 저장하는데 필요한
디스크 공간보다 작다. 왜냐하면 보통 인덱스는 키-필드만 갖고 있고,
테이블의 다른 세부 항목들은 갖고 있지 않기 때문이다.
-배열을 사용한 인덱스 : 대량의 데이터를 매번 정렬하면,
프로그램의 반응은 느려질 수 밖에 없다.
성능 저하 문제를 해결하기 위해 배열 인덱스를 사용할 수 있다.

4. 선택정렬
4.1 주어진 자료들 중 가장 작은 값의 원소부터 차례대로 선택하여 
위치를 교환하는 방식.
-앞서 살펴본 셀렉션 알고리즘을 전체 자료에 적용한 것이다.

4.2 정렬 과정
-주어진 리스트 중에서 최소값을 찾는다.
-그 값을 리스트의 맨 앞에 위치한 값과 교환한다.
-맨 처음 위치를 제외한 나머지 리스트를 대상으로 위의 과정을 반복한다.
-시간 복잡도 : O(n2)
'''

# 선택정렬


def select_Sort(arr, n):
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


arr = [22, 25, 64, 10, 11]
print(select_Sort(arr, 5))


def homework():
    T = 10
    for _ in range(T):
        tc = int(input())
        result = -0xffffffff
        # 리스트안에 100개 짜리 리스트 100개
        board = [list(map(int, input().split())) for _ in range(100)]
        for i in range(100):
            sum_row = 0
            for j in range(100):
                sum_row += board[i][j]
            if sum_row > result:
                result = sum_row

        for j in range(100):
            sum_col = 0
            for i in range(100):
                sum_col += board[i][j]
            if sum_col < result:
                result = sum_col

        sum_dia1 = 0
        sum_dia2 = 0
        for i in range(100):
            for j in range(100):
                if i == j:
                    sum_dia1 += board[i][j]
                if i + j == 99:
                    sum_dia2 += board[i][j]

        for e in (sum_dia1, sum_dia2):
            if e > result:
                result = e
        result = result if result > sum_dia1 else sum_dia1
        result = result if result > sum_dia2 else sum_dia2

        print(f'{tc} {result}')
