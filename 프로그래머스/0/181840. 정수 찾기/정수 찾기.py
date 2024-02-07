def solution(num_list, n):
    answer =False
    for i in range(len(num_list)):
        if  num_list[i] == n :
            answer = True
    return int(answer)