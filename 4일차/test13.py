def calculate_daily_salary(monthly_salary, days_in_month):
    """
    월급과 월의 일수를 받아서 일당을 계산합니다.
    """
    daily_salary = monthly_salary / days_in_month
    return daily_salary

def main():
    # 사용자로부터 월급과 월의 일수를 입력받습니다.
    monthly_salary = float(input("월급을 입력하세요: "))
    days_in_month = 26  # 월의 일수

    # 일당을 계산합니다.
    daily_salary = calculate_daily_salary(monthly_salary, days_in_month)

    # 결과를 출력합니다.
    print(f"일당은 {daily_salary:.2f}원입니다.")

# 메인 함수 실행
if __name__ == "__main__":
    main()