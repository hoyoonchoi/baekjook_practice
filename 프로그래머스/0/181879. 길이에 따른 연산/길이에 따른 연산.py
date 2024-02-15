def solution(num_list):
    a= 0 
    b =1
    if len(num_list)>10: 
        for i in range(len(num_list)):
            a=a + num_list[i]
        return a 
            
    else:
        for i in range(len(num_list)):
            b= b * num_list[i]
        return b
