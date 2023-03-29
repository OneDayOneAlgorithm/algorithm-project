

def A():
    ans = sum(lst) / N
    return round(ans)
def B():
    return sorted_lst[N//2]
def C():
    visited = [0]*8001
    for i in lst:
        visited[i+2000] += 1
    return visited.index(max(visited))
def D():
    pass


N = int(input())
lst = []
for i in range(N):
    lst.append(int(input()))
sorted_lst = sorted(lst)
print(A())
print(B())
print(C())
# print(D())
