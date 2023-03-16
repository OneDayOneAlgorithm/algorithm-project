def solve(n):
    global cnt, ans,sumv    
    if cnt == N:        # 자릿수가 N과 같을시
        if sumv not in lst:     # 원소의 합이 중복되지 않도록 한다.
            lst.append(sumv)
            ans += 1
        return
    for i in range(n,4):
        cnt += 1
        sumv += arr[i]
        solve(i)
        sumv -= arr[i]
        cnt -= 1
N = int(input())    # 로마 숫자 N개 입력
arr=[1,5,10,50] # 로마숫자 배열
cnt = 0 # 함수 solve에서 자릿수가 증가할때마다 cnt를 세다가 cnt==N일 때
lst = []    # 배열 lst에 넣을 예정
sumv = 0 # 그런데 중복되는 값이 있을시엔 lst에 저장 안한다.
ans = 0 # 만들 수 있는 서로 다른 수의 개수 ans
solve(0)    # ans을 세는 함수 solve 실행
print(ans)  # 만들 수 있는 서로 다른 수의 개수 출력