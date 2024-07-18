import sys  


N= int(input())
first= list(map(int, sys.stdin.readline().split()))
second= list(map(int, sys.stdin.readline().split()))

first.sort()
second.sort(reverse=True)

answer=0
for i in range(N):
    answer+= int(first[i])*int(second[i])

print(answer)