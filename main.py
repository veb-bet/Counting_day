
import datetime
import calendar

def count_workdays(start_date, end_date):
    workdays = 0
    for n in range(int((end_date - start_date).days)):
        day = start_date + datetime.timedelta(n)
        if day.weekday() < 5:  # Monday to Friday are workdays
            workdays += 1
    return workdays

start_date = datetime.date.today()
end_date = datetime.date(2023, 12, 31)  # Change this to the desired end date

workdays = count_workdays(start_date, end_date)

print(f"Обратный отсчёт дней до {end_date}:")
for day in range(workdays, 0, -1):
    print(f"{day} дней до конца года (будние дни)")

