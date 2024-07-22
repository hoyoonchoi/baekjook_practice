N,K = map(int, input().split())
a = list(map(int,input().split()))

left=0
right=K
#수열의 합 구하는거 잘 기억해둘 것 
current_sum= sum(a[left:right])
max_sum =current_sum

while right< N: 
    current_sum += a[right]-a[left]
    if current_sum > max_sum:
        max_sum = current_sum
    left +=1
    right +=1

print(max_sum)
