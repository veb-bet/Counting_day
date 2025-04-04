import datetime
import pytz
import calendar
import sys

# Список официальных праздников (можно расширять вручную или загружать из API)
HOLIDAYS = [
    datetime.date(2025, 1, 1),   # Новый год
    datetime.date(2025, 1, 2),   # Новогодние каникулы
    datetime.date(2025, 1, 3),
    datetime.date(2025, 1, 4),
    datetime.date(2025, 1, 5),
    datetime.date(2025, 1, 6),
    datetime.date(2025, 1, 7),   # Рождество Христово
    datetime.date(2025, 1, 8),   # Новогодние каникулы
    datetime.date(2025, 2, 23),  # День защитника Отечества
    datetime.date(2025, 3, 8),   # Международный женский день
    datetime.date(2025, 5, 1),   # Праздник Весны и Труда
    datetime.date(2025, 5, 9),   # День Победы
    datetime.date(2025, 6, 12),  # День России
    datetime.date(2025, 11, 4),  # День народного единства

    # Дополнительные переносы/выходные (по производственному календарю могут добавляться)
    # datetime.date(2025, X, Y),
]

def count_workdays(start_date, end_date, holidays=None):
    workdays_total = 0
    current_date = start_date
    holidays = holidays or []

    while current_date <= end_date:
        if current_date.weekday() < 5 and current_date not in holidays:
            workdays_total += 1
        current_date += datetime.timedelta(days=1)
    
    return workdays_total

def print_progress_bar(current, total, bar_length=30):
    percent = current / total if total != 0 else 1
    filled_length = int(bar_length * percent)
    bar = '█' * filled_length + '-' * (bar_length - filled_length)
    print(f"\rПрогресс: |{bar}| {int(percent * 100)}% ({current}/{total} рабочих дней)", end='')

def get_date(prompt, use_today_if_empty=True, tz=None):
    user_input = input(prompt).strip()
    if user_input == "":
        if use_today_if_empty:
            return datetime.datetime.now(tz).date()
        else:
            return None
    try:
        return datetime.datetime.strptime(user_input, "%Y-%m-%d").date()
    except ValueError:
        print("Неверный формат даты. Используется сегодняшняя дата.")
        return datetime.datetime.now(tz).date()

def select_timezone():
    print("Выберите временную зону (например, Europe/Moscow или America/New_York).")
    tz_input = input("Введите временную зону или нажмите Enter для Europe/Moscow: ").strip()
    try:
        return pytz.timezone(tz_input) if tz_input else pytz.timezone("Europe/Moscow")
    except pytz.UnknownTimeZoneError:
        print("Неизвестная временная зона. Используется Europe/Moscow.")
        return pytz.timezone("Europe/Moscow")

def main():
    while True:
        print("\n=== Расчёт оставшихся рабочих дней ===")
        
        tz = select_timezone()
        
        start_date = get_date("Введите дату начала (ГГГГ-ММ-ДД) или Enter для сегодняшней: ", tz=tz)
        end_date = get_date("Введите дату окончания (ГГГГ-ММ-ДД) или Enter для 2025-07-06: ", use_today_if_empty=False, tz=tz)
        if end_date is None:
            end_date = datetime.date(2025, 7, 6)

        true_start = min(start_date, end_date)
        true_end = max(start_date, end_date)
        today = datetime.datetime.now(tz).date()

        total_workdays = count_workdays(true_start, true_end, holidays=HOLIDAYS)
        past_workdays = count_workdays(true_start, today - datetime.timedelta(days=1), holidays=HOLIDAYS) if today > true_start else 0

        print_progress_bar(past_workdays, total_workdays)
        print()  # перенос строки

        exit_choice = input("Хотите выйти? (да/нет): ").strip().lower()
        if exit_choice in ("да", "д", "y", "yes"):
            print("Выход из программы. Пока!")
            break

# Точка входа
if __name__ == "__main__":
    main()
