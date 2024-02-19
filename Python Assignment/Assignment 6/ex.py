import statistics

def calculate_standard_deviation(data):
    """
    주어진 데이터의 표준 편차를 계산하는 함수
    :param data: 숫자들의 리스트
    :return: 표준 편차 값
    """
    try:
        std_dev = statistics.stdev(data)
        return std_dev
    except statistics.StatisticsError as e:
        print(f"통계적 에러: {e}")
        return None
    

data1 = [88.0, 88.3, 89.05, 89.91, 87.01, 91.01]
data2 = [90.1, 83.03, 88.01, 90.08, 89.65, 86.03]
data3 = [101.26, 101.05, 100.5, 100.7, 100.95,101.21]
print(calculate_standard_deviation(data1))
print(calculate_standard_deviation(data2))
print(calculate_standard_deviation(data3))


print(88.88-88.48 + 1.88*(((1.43**2)/6 + (2.82**2)/6)**(1/2)))
print(88.88-88.48 - 1.88*(((1.43**2)/6 + (2.82**2)/6)**(1/2)))