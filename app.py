import datetime
import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar

# Праздники для разных стран
HOLIDAYS_RUSSIA = [
    datetime.date(2025, 1, 1),   # Новый год
    datetime.date(2025, 1, 7),   # Рождество Христово
    datetime.date(2025, 2, 23),  # День защитника Отечества
    datetime.date(2025, 3, 8),   # Международный женский день
    datetime.date(2025, 5, 1),   # Праздник Весны и Труда
    datetime.date(2025, 5, 9),   # День Победы
    datetime.date(2025, 6, 12),  # День России
    datetime.date(2025, 11, 4),  # День народного единства
    datetime.date(2025, 12, 31), # Новый год (переходящий)
]

HOLIDAYS_USA = [
    datetime.date(2025, 1, 1),   # Новый год
    datetime.date(2025, 7, 4),   # День независимости
    datetime.date(2025, 9, 1),   # День труда
    datetime.date(2025, 10, 31), # Хэллоуин
    datetime.date(2025, 12, 25), # Рождество
    datetime.date(2025, 11, 26), # День благодарения
]

HOLIDAYS_GERMANY = [
    datetime.date(2025, 1, 1),   # Новый год
    datetime.date(2025, 5, 1),   # Праздник труда
    datetime.date(2025, 10, 3),  # День единства Германии
    datetime.date(2025, 12, 25), # Рождество
    datetime.date(2025, 12, 26), # День святого Стефана
]

HOLIDAYS_UK = [
    datetime.date(2025, 1, 1),   # Новый год
    datetime.date(2025, 5, 25),  # Праздник весны
    datetime.date(2025, 8, 31),  # Праздник труда
    datetime.date(2025, 12, 25), # Рождество
    datetime.date(2025, 12, 26), # День святого Стефана
]

HOLIDAYS_FRANCE = [
    datetime.date(2025, 1, 1),   # Новый год
    datetime.date(2025, 5, 1),   # Праздник труда
    datetime.date(2025, 7, 14),  # День взятия Бастилии
    datetime.date(2025, 12, 25), # Рождество
]

# Дополнительные страны
COUNTRIES = ["Russia", "USA", "Germany", "UK", "France"]

# Изначальные праздники для России
HOLIDAYS = HOLIDAYS_RUSSIA

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
    # Получаем выбранные даты
    start_date = cal_start.selection_get()
    end_date = cal_end.selection_get()
    
    # Убедимся, что начальная дата раньше или равна конечной
    true_start = min(start_date, end_date)
    true_end = max(start_date, end_date)
    
    # Текущая дата
    today = datetime.datetime.now().date()

    # Количество рабочих дней
    total = count_workdays(true_start, true_end, HOLIDAYS)

    # Если сегодняшняя дата позже начальной, то считаем, что прошло рабочих дней
    if today >= true_start:
        passed = count_workdays(true_start, today, HOLIDAYS)
    else:
        passed = 0

    if total > 0:
        percent = passed / total
    else:
        percent = 1

    progress_var.set(percent)
    label_result.config(text=f"Рабочих дней всего: {total}\nПрошло: {passed}")
    progress_label.config(text=f"{int(percent * 100)}%")

def load_holidays_for_country(country):
    """Загружает праздники для выбранной страны"""
    global HOLIDAYS
    if country == "Russia":
        HOLIDAYS = HOLIDAYS_RUSSIA
    elif country == "USA":
        HOLIDAYS = HOLIDAYS_USA
    elif country == "Germany":
        HOLIDAYS = HOLIDAYS_GERMANY
    elif country == "UK":
        HOLIDAYS = HOLIDAYS_UK
    elif country == "France":
        HOLIDAYS = HOLIDAYS_FRANCE
    update_holidays_display()

def add_custom_holiday():
    """Добавляет пользовательский праздник в список"""
    date_str = entry_custom_holiday.get()
    try:
        custom_date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
        if custom_date not in HOLIDAYS:
            HOLIDAYS.append(custom_date)
            update_holidays_display()
            entry_custom_holiday.delete(0, tk.END)  # Очистить поле
        else:
            label_result.config(text="Этот праздник уже существует!")
    except ValueError:
        label_result.config(text="Неверный формат даты! Используйте yyyy-mm-dd.")

def update_holidays_display():
    """Обновляет отображение списка праздников"""
    holidays_text = "\n".join([str(holiday) for holiday in sorted(HOLIDAYS)])
    label_holidays.config(text=f"Праздники:\n{holidays_text}")

# --- Интерфейс ---
root = tk.Tk()
root.title("Рабочие дни между датами")

# Выбор страны
ttk.Label(root, text="Выберите страну:").grid(row=0, column=0, padx=10, pady=5)
country_combobox = ttk.Combobox(root, values=COUNTRIES)
country_combobox.grid(row=1, column=0, padx=10, pady=5)
country_combobox.set(COUNTRIES[0])  # Установить значение по умолчанию
ttk.Button(root, text="Загрузить праздники", command=lambda: load_holidays_for_country(country_combobox.get())).grid(row=2, column=0, pady=10)

# Календарь начала
ttk.Label(root, text="Дата начала:").grid(row=0, column=1, padx=10, pady=5)
cal_start = Calendar(root, selectmode='day', date_pattern='yyyy-mm-dd')
cal_start.grid(row=1, column=1, padx=10, pady=5)

# Календарь окончания
ttk.Label(root, text="Дата окончания:").grid(row=0, column=2, padx=10, pady=5)
cal_end = Calendar(root, selectmode='day', date_pattern='yyyy-mm-dd')
cal_end.grid(row=1, column=2, padx=10, pady=5)

# Кнопка расчета
ttk.Button(root, text="Рассчитать", command=calculate_workdays).grid(row=2, column=1, columnspan=2, pady=10)

# Прогресс-бар
progress_var = tk.DoubleVar()
progress_bar = ttk.Progressbar(root, maximum=1.0, variable=progress_var, length=300)
progress_bar.grid(row=3, column=0, columnspan=3, pady=5)

progress_label = ttk.Label(root, text="0%")
progress_label.grid(row=4, column=0, columnspan=3)

# Результат
label_result = ttk.Label(root, text="Выберите даты и нажмите 'Рассчитать'")
label_result.grid(row=5, column=0, columnspan=3, pady=10)

# Текстовое поле для ввода пользовательских праздников
ttk.Label(root, text="Введите пользовательский праздник (формат yyyy-mm-dd):").grid(row=6, column=0, padx=10, pady=5)
entry_custom_holiday = ttk.Entry(root)
entry_custom_holiday.grid(row=7, column=0, padx=10, pady=5)

# Кнопка для добавления пользовательского праздника
ttk.Button(root, text="Добавить праздник", command=add_custom_holiday).grid(row=8, column=0, pady=10)

# Отображение списка праздников
label_holidays = ttk.Label(root, text="Праздники:\n")
label_h
