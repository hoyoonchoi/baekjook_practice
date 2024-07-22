n,m = map(int, input().split())
a = list(map(int, input().split()))

sum = a[0] 
left = 0
right = 1
count = 0

while True:
    if sum < m:
        if right < n:
            sum += a[right]
            right += 1 
        else:
            break
    
    elif sum == m:
        count +=1
        sum -= a[left]
        left += 1
    else:
        sum -= a[left]
        left += 1 

print(count)