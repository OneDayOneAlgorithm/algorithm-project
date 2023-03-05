T = int(input())
# T = 1
for tc in range(T):
    dict = {}
    for i in range(1,5001):
        dict[i] = 0
        # {1:0, 2:0, 3:0 ... 5000:0} 정류장번호:노선갯수
    N = int(input())
    # 몇개의 노선을 설치할거냐
    for i in range(N):
        A, B = map(int,input().split())
        for j in range(A, B + 1):
            dict[j] += 1
    P = int(input())
    # 몇개의 정류장을 볼거냐
    output = ''
    for i in range(P):
        output = output + ' ' + str(dict[int(input())])
    print(f'#{tc + 1}{output}')