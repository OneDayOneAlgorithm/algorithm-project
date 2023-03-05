# def f(i,k):     # 인덱스와 갯수
#     if i == k:
#         print(bit)
#     else:
#         bit[i] = 1
#         f(i+1, k)
#         bit[i] = 0
#         f(i+1,k)
#
# A = {1,2,3}
# N = len(A)
# bit = [0] * N
# f(0,N)

isp = {'*': 2, '/': 2, '+': 1, '-': 1,'(': 0 }
icp = {'*': 2, '/': 2, '+': 1, '-': 1,'(': 3 }
# (6+5*(2-8)/2)
# '2+3*4/5'  >> 234*5/+
# 2 3 4 5 / * +
data = input()
stack = []
#피연산자는 그냥 출력
#연산자는 우선순위에 따라서 stack넣거나, 빼고 넣기
#   stack의 top의 우선순위보다 token의 우선순위가 높으면 그냥 stack에 넣어주기
#   아니면...높거나 같은애들은 다빼고 낮은애가 나오면 push
# 닫히는 괄호나오면 여는 괄호나올때 까지 pop 하면서 출력하기
for i in range(len(data)):
    # data[i]
    if data[i] in '0123456789':
        print(data[i],end='')
    else: # 연산자
        if data[i] == ')':
            #여는 괄호가 나올때까지 pop하면서 연산자 출력
            while stack[-1] != '(':
                print(stack.pop(),end='')
            #여는 괄호 버리기
            stack.pop()
        elif not stack:   #스택이 비어있으면
            stack.append(data[i])
        else:   # 스택이 비어있지 않으면 우선순위를 따집시다.
            if isp[stack[-1]]< icp[data[i]]:
                stack.append(data[i])
            else:
                # 나보다 작은애가 나올때 까지 pop하면서 출력 + 스택이 비어있지 않으면서
                while stack and isp[stack[-1]] >= icp[data[i]]:
                    print(stack.pop(),end='')
                stack.append(data[i])
#수식을 다 읽었을 때 stack에 연산자가 남아 있으면 pop() 하면서 출력
while stack:
    print(stack.pop(),end='')
print()

# subset
arr = [1,2,3,4,5]
N = len(arr)
selected = [0] * N

# idx 에 해당하는 요소가 부분집합에 포함되는지 아닌지 결정
# 결정하고나서 다음 요소 포함여부 경정하러 ㄱㄱ
def subset(idx):
    # 완전탐색 : 내가 할 수 있는거 다 해보면 됩니다.
    if idx == N:
        #N - 1번 요소까지 결정이 끝난 상황
        print(selected)
        return
    selected[idx] = 1
    subset(idx+1)
    selected[idx] = 0
    subset(idx + 1)

# 순열
arr = [1,2,3]
N = len(arr)
perm_arr = [0] * N
# idx번째에 넣을 수 있는 숫자 다 넣기
used = [0] * N
def perm(idx):
    if idx == N:
        print(perm_arr)
        return
    for i in range(N):
        if not used[i]:
            perm[idx] = arr[i]
            used[i] = 1
            perm(idx+1)
            used[i] = 0
perm(0)

# 수열
arr = [1,2,3,4,5]
# idx 번째 요소를 조합에 포함할지 안 할지 결정
selected = [0] * N
# cnt = 여태까지 선택한 요소의 개수
def comb(idx,cnt):
    if idx == N:        # 마지막 인덱스까지 모두 결정했으니
        # 결과보기
        print(selected)
        for i in range(N):
            if selected[i]:
                print(arr[i], end=' ')
        print()
        return
    # 내가 할 수 있는 거 다 해보기
    for i in range(2):
        selected[idx] = i
        #요소를 선택하면 +1
        comb(idx+1, cnt + 1)
        selected[idx] = 0
    # selected[idx] = 1
    # comb(idx +1,cnt+1)
    # selected[idx] = 0
    # comb(idx+1,cnt)
    #N개 중에 K개 선택해라
comb(0)

# 미로찾기
stack = []
visited = [[0] * N for _ in range(N)]
visited[sr][sc] = 1

while stack:
    #갈 수 있는 경로를 발견하면 즉시 이동
    # 없으면 stack pop
    # 위를 계속 반복 >> stack이 비어있지 않으면
    dr = [-1,1,0,0]
    dc = [0,0,-1,1]
    cr,cc = stack[-1] # 커런트 r, 커런트c
    while stack:
        cr,cc = stack[-1]
        if arr[cr][cc] == 2:
            return 1
    # top에서 이동할 수 있는 모든 경로  살펴보기
    # for dr,dc in [(-1,0),(1,0),(0,-1),(0,1)]:
        for d in range(4):
            nr = cr+dr[d]
            nc = cc+dc[d]
            if 0<=nr<N and 0<= nc <N and arr[cr+dr[d]][cc+dc[d]] and not visited[nr][nc]: # 갈 수 있으면
                stack.append((nr,nc))
                visited[nr][nc] = 1
                break
        else:
            stack.pop()
    return 0
print(dfs(0,0))
    