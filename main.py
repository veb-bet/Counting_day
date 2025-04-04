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

def get_date(prompt, use_today_if_empty=True):
    user_input = input(prompt).strip()
    if user_input == "":
        if use_today_if_empty:
            return datetime.date.today()
        else:
            return None
    try:
        return datetime.datetime.strptime(user_input, "%Y-%m-%d").date()
    except ValueError:
        print("Неверный формат даты. Используется сегодняшняя дата.")
        return datetime.date.today()

def main():
    while True:
        print("\n=== Расчёт оставшихся рабочих дней ===")
        
        start_date = get_date("Введите дату начала (ГГГГ-ММ-ДД) или Enter для сегодняшней: ")
        end_date = get_date("Введите дату окончания (ГГГГ-ММ-ДД) или Enter для 2025-07-06: ", use_today_if_empty=False)
        if end_date is None:
            end_date = datetime.date(2025, 7, 6)

        true_start = min(start_date, end_date)
        true_end = max(start_date, end_date)
        today = datetime.date.today()

        total_workdays = count_workdays(true_start, true_end)
        past_workdays = count_workdays(true_start, today - datetime.timedelta(days=1)) if today > true_start else 0

        print_progress_bar(past_workdays, total_workdays)
        print()  # перенос строки

        exit_choice = input("Хотите выйти? (да/нет): ").strip().lower()
        if exit_choice in ("да", "д", "y", "yes"):
            print("Выход из программы. Пока!")
            break

# Точка входа
if __name__ == "__main__":
    main()
