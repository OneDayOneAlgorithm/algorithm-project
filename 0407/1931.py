import sys
input = sys.stdin.readline

N = int(input())    # 전체 회의의 갯수
lst = []
for i in range(N):
    a,b = map(int,input().split())  # 각각에 회의에 대한 시작시간과 종료시
    lst.append((a,b))
lst.sort(key=lambda x:x[0]) # 시작시간에 대해서 오름차순으로 정렬
lst.sort(key=lambda x:x[1]) # 종료시간에 대해서 오름차순으로 정렬
end = lst[0][1] # 초기값을 설정
cnt = 1
for i in range(1,N):
    if lst[i][0] >= end:    # 두번째 회의(다음 회의)를 결정
        end = lst[i][1]
        cnt += 1
print(cnt)