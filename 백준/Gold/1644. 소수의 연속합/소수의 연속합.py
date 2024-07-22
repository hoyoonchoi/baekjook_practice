'''import math
N = int(input())


#시간 초과 

def is_primnum(x):
    for i in range(2,int(math.sqrt(x)+1)):
        if x% i == 0:
            return False
    return True
sosu=[]
for i in range(2,N+1):
    if is_primnum(i) == True:
        sosu.append(i)
sum = sosu[0]
left =0
right =1
count =0

while right <= len(sosu) and left < len(sosu):
    if sum < N:
        if right < len(sosu):
            sum += sosu[right]
            right +=1
        else:
            break
    
    elif sum == N :
        count +=1 
        sum -= sosu[left]
        left +=1

    else:
        sum -= sosu[left]
        left +=1

print(count)        
'''

import sys, math
input = sys.stdin.readline

N = int(input())

# 에라토스테네스의 채
arr = [True]*(N+1)
arr[0] = False
arr[1] = False

for num in range(2, int(math.sqrt(N))+1):
    if arr[num]:
        for mul in range(num*2, N+1, num):
            arr[mul] = False

arr = [i for i in range(2, N+1) if arr[i]] + [0]


# 투 포인터(두 포인터 모두 왼쪽에서 시작)
i = 0
j = 0
subtotal = arr[i]
count = 0

while j < len(arr)-1:
    # 연속합이 N과 같으면 카운팅해주고
    # 왼쪽, 오른쪽 포인터 둘 다 한칸 진행
    # 왼쪽만 옮겼을 때, 연속합이 감소하므로
    # 반드시 N보다 작아진다. 즉, 오른쪽 포인
    # 터도 같이 한 칸 옮겨준다.
    if subtotal == N:
        count += 1
        subtotal -= arr[i]
        i += 1
        j += 1
        subtotal += arr[j]
    # 연속합이 N보다 작으면 값을 키워줘야하므로
    # 오른쪽 포인터를 진행
    elif subtotal < N:
        j += 1
        subtotal += arr[j]
    # 연속합이 N보다 크면 줄여줘야하므로
    # 왼쪽 포인터 진행
    else:
        subtotal -= arr[i]
        i += 1
        
print(count)