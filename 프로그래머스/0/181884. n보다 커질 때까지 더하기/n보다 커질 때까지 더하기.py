def solution(numbers, n):
    sum = 0
    for i in range(len(numbers)):
        if sum <= n:
            sum = sum + numbers[i]
        else: 
            return sum 
    return sum  