def day_cal(month, day): 
    days_in_month = [31,28,31,30,31,30,31,31,30,31,30,31]  # 월별 일수 리스트
    cumulative_days = [0] * 12  # 각 월의 시작일까지의 누적 일수를 저장하는 리스트

    # 누적 일수 계산
    for i in range(1, len(days_in_month)):
        cumulative_days[i] = cumulative_days[i - 1] + days_in_month[i - 1]

    total_days = cumulative_days[month - 1] + day
    
    # 1월 1일이 월요일이라고 가정 (실제 연도에 따라 조정 가능)
    if total_days % 7 == 1:
        print('MON') 
    elif total_days % 7 == 2:
        print('TUE')
    elif total_days % 7 == 3:
        print('WED')
    elif total_days % 7 == 4:
        print('THU')
    elif total_days % 7 == 5:
        print('FRI')
    elif total_days % 7 == 6:
        print('SAT')
    else: 
        print('SUN')

month, day = map(int,input().split())
day_cal(month, day)