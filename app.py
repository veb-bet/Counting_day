import datetime
import pytz
import calendar
import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar

# Список праздников
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

def calculate_workdays():
    start_date = cal_start.selection_get()
    end_date = cal_end.selection_get()
    true_start = min(start_date, end_date)
    true_end = max(start_date, end_date)
    today = datetime.datetime.now().date()

    total = count_workdays(true_start, true_end, HOLIDAYS)
    passed = count_workdays(true_start, today - datetime.timedelta(days=1), HOLIDAYS) if today > true_start else 0

    if total > 0:
        percent = passed / total
    else:
        percent = 1

    progress_var.set(percent)
    label_result.config(text=f"Рабочих дней всего: {total}\nПрошло: {passed}")
    progress_label.config(text=f"{int(percent * 100)}%")

# --- Интерфейс ---
root = tk.Tk()
root.title("Рабочие дни между датами")

# Календарь начала
ttk.Label(root, text="Дата начала:").grid(row=0, column=0, padx=10, pady=5)
cal_start = Calendar(root, selectmode='day', date_pattern='yyyy-mm-dd')
cal_start.grid(row=1, column=0, padx=10, pady=5)

# Календарь окончания
ttk.Label(root, text="Дата окончания:").grid(row=0, column=1, padx=10, pady=5)
cal_end = Calendar(root, selectmode='day', date_pattern='yyyy-mm-dd')
cal_end.grid(row=1, column=1, padx=10, pady=5)

# Кнопка расчета
ttk.Button(root, text="Рассчитать", command=calculate_workdays).grid(row=2, column=0, columnspan=2, pady=10)

# Прогресс-бар
progress_var = tk.DoubleVar()
progress_bar = ttk.Progressbar(root, maximum=1.0, variable=progress_var, length=300)
progress_bar.grid(row=3, column=0, columnspan=2, pady=5)

progress_label = ttk.Label(root, text="0%")
progress_label.grid(row=4, column=0, columnspan=2)

# Результат
label_result = ttk.Label(root, text="Выберите даты и нажмите 'Рассчитать'")
label_result.grid(row=5, column=0, columnspan=2, pady=10)

root.mainloop()
