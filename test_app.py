import pytest
import datetime
from app import (
    count_workdays, 
    load_holidays_for_country, 
    HOLIDAYS_RUSSIA, 
    HOLIDAYS_USA, 
    HOLIDAYS_GERMANY, 
    HOLIDAYS_UK, 
    HOLIDAYS_FRANCE,
    HOLIDAYS
)

# Тестируем функцию count_workdays
def test_count_workdays():
    start_date = datetime.date(2025, 1, 1)
    end_date = datetime.date(2025, 1, 7)
    holidays = [datetime.date(2025, 1, 1), datetime.date(2025, 1, 7)]  # Новый год
    workdays = count_workdays(start_date, end_date, holidays)
    
    # В данном случае выходные дни: 1 и 7 января, должны быть 3 рабочих дня
    assert workdays == 3

def test_count_workdays_no_holidays():
    start_date = datetime.date(2025, 1, 1)
    end_date = datetime.date(2025, 1, 7)
    holidays = []  # Без праздников
    workdays = count_workdays(start_date, end_date, holidays)
    
    # Всего 5 рабочих дней с 1 по 7 января
    assert workdays == 5

# Тестируем функцию load_holidays_for_country
def test_load_holidays_for_country():
    # Проверка загрузки праздников для России
    load_holidays_for_country("Russia")
    assert HOLIDAYS == HOLIDAYS_RUSSIA
    
    # Проверка загрузки праздников для США
    load_holidays_for_country("USA")
    assert HOLIDAYS == HOLIDAYS_USA
    
    # Проверка загрузки праздников для Германии
    load_holidays_for_country("Germany")
    assert HOLIDAYS == HOLIDAYS_GERMANY
    
    # Проверка загрузки праздников для Великобритании
    load_holidays_for_country("UK")
    assert HOLIDAYS == HOLIDAYS_UK
    
    # Проверка загрузки праздников для Франции
    load_holidays_for_country("France")
    assert HOLIDAYS == HOLIDAYS_FRANCE

# Тестируем добавление пользовательского праздника
def test_add_custom_holiday():
    custom_holiday = datetime.date(2025, 5, 9)  # День Победы (будет добавлен к праздникам России)
    
    # Добавляем праздник
    load_holidays_for_country("Russia")
    initial_holidays = list(HOLIDAYS)
    HOLIDAYS.append(custom_holiday)
    
    # Проверим, что праздник добавлен
    assert custom_holiday in HOLIDAYS
    assert len(HOLIDAYS) == len(initial_holidays) + 1
    
    # Проверим, что если добавим его снова, он не добавится
    if custom_holiday not in initial_holidays:
        HOLIDAYS.append(custom_holiday)
    assert len(HOLIDAYS) == len(initial_holidays) + 1  # Количество праздников не изменится

# Тестируем корректность вычисления рабочих дней с праздниками и выходными
def test_calculate_workdays_with_custom_holidays():
    start_date = datetime.date(2025, 1, 1)
    end_date = datetime.date(2025, 1, 10)
    holidays = [datetime.date(2025, 1, 1), datetime.date(2025, 1, 7), datetime.date(2025, 1, 8)]  # Праздники на Новый год и Рождество
    
    workdays = count_workdays(start_date, end_date, holidays)
    # Из 10 дней, 3 дня — праздники (1, 7, 8 января), остаётся 7 рабочих дней
    assert workdays == 7

