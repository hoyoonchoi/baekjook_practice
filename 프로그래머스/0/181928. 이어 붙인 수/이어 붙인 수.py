def solution(num_list):
    # 홀수와 짝수를 분리하여 문자열로 이어 붙임
    odd_str = ''.join([str(num) for num in num_list if num % 2 != 0])
    even_str = ''.join([str(num) for num in num_list if num % 2 == 0])
    
    # 이어 붙인 문자열을 정수로 변환하여 더함
    return int(odd_str) + int(even_str)


