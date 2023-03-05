import string
N = int(input())
word = input()
lst = []
sum = 0
for i in word:
    for j in range(len(string.ascii_lowercase)):
        if i == string.ascii_lowercase[j]:
            lst.append(j + 1)
for i in range(N):
    sum += lst[i] * (31 ** i)
print(sum % 1234567891)

