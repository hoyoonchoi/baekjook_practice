import sys

N = int(input())
list =[]
for i in range(N):
    list.append(int(input()))

list.sort(reverse=True)
result = []

for j in range(N):
    result.append(list[j]*(j+1))

print(max(result))