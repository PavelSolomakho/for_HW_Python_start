import sys
from datetime import datetime


def is_valid_date(date):
    """Проверяем, является ли дата корректной и реальной"""
    try:
        dt = datetime.strptime(date, "%d.%m.%Y")
        return dt.date() <= datetime.now().date()
    except ValueError:
        return False


if len(sys.argv) == 2:
    date = sys.argv[1]
    if is_valid_date(date):
        print("Дата", date, "является корректной и реальной.")
    else:
        print("Дата", date, "не является корректной или еще не наступила.")
else:
    print("Пожалуйста, введите дату в формате ДД.ММ.ГГГГ")
    date = input()
    if is_valid_date(date):
        print("Дата", date, "является корректной и реальной.")
    else:
        print("Дата", date, "не является корректной или еще не наступила.")
