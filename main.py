import datetime
import calendar
import sys

def count_workdays(start_date, end_date):
    workdays_total = 0
    current_date = start_date

    while current_date <= end_date:
        if current_date.weekday() < 5:  # Понедельник–Пятница
            workdays_total += 1
        current_date += datetime.timedelta(days=1)
    
    return workdays_total

def print_progress_bar(current, total, bar_length=30):
    percent = current / total if total != 0 else 1
    filled_length = int(bar_length * percent)
    bar = '█' * filled_length + '-' * (bar_length - filled_length)
    print(f"\rПрогресс: |{bar}| {int(percent * 100)}% ({current}/{total} рабочих дней)", end='')

def get_start_date():
    user_input = input("Введите дату начала (ГГГГ-ММ-ДД) или нажмите Enter для использования сегодняшней: ").strip()
    if user_input == "":
        return datetime.date.today()
    try:
        return datetime.datetime.strptime(user_input, "%Y-%m-%d").date()
    except ValueError:
        print("Неверный формат даты. Используется сегодняшняя дата.")
        return datetime.date.today()

# --- Основная логика ---
start_date = get_start_date()
end_date = datetime.date(2025, 7, 6)  # Можно заменить на любую дату

# Обеспечим корректный порядок дат
true_start = min(start_date, end_date)
true_end = max(start_date, end_date)
today = datetime.date.today()

total_workdays = count_workdays(true_start, true_end)
# Определяем, сколько рабочих дней прошло
past_workdays = count_workdays(true_start, today - datetime.timedelta(days=1)) if today > true_start else 0

# Выводим прогресс-бар
print_progress_bar(past_workdays, total_workdays)
print()  # переход на новую строку после прогресс-бара
