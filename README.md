# Рабочие Дни Калькулятор с Tkinter

Этот проект представляет собой графическое приложение для расчёта числа рабочих дней между двумя выбранными датами, с учётом официальных праздников. В качестве графического интерфейса используется библиотека `Tkinter`, а для работы с календарем — `tkcalendar`.

## Основные функции:

- **Выбор дат**: пользователи могут выбрать дату начала и окончания через графический календарь.
- **Расчёт рабочих дней**: программа вычисляет количество рабочих дней, исключая выходные и официальные праздники.
- **Прогресс-бар**: отображает прогресс выполнения (процент рабочих дней, которые уже прошли по сравнению с общим количеством рабочих дней).
- **Праздники**: учитываются официальные праздники в России для 2025 года.

## Зависимости

Для работы программы требуется установить несколько зависимостей. Вы можете установить их с помощью `pip`:

```bash
pip install pytz tkcalendar tkinter
```

## Использование

1. Скачайте или клонируйте репозиторий.
2. Убедитесь, что у вас установлены необходимые библиотеки, используя команду выше.
3. Запустите скрипт.
4. В интерфейсе программы выберите даты начала и окончания с помощью календаря.
5. Нажмите кнопку "Рассчитать", чтобы увидеть количество рабочих дней и прогресс выполнения.
6. Прогресс-бар будет показывать процент выполнения (сколько рабочих дней прошло).
7. Результат будет отображаться внизу экрана.

## Пример интерфейса

- Два календаря для выбора даты начала и окончания.
- Кнопка "Рассчитать" для запуска вычислений.

![image](https://github.com/user-attachments/assets/4195865b-2123-4edc-a22a-2eb9e92e6280)

- Прогресс-бар для отображения процента завершения.
- Результат в виде текста: "Рабочих дней всего: X" и "Прошло: Y".

![image](https://github.com/user-attachments/assets/c1ac7a05-5d6c-4502-b040-0a5044a0cea6)
![image](https://github.com/user-attachments/assets/2ba010c8-5c74-48aa-8ad1-78d0f3b26dfe)

## Будущие улучшения:

- Обработка исключений
- Улучшенный интерфейс

# Консольное приложение

Простая консольная программа на Python, которая рассчитывает количество **рабочих дней** между двумя датами и отображает **прогресс-бар**.

## Возможности

- Учёт **только будних дней** (Пн–Пт).
- Ввод **начальной** и **конечной** даты вручную (или использование текущей по умолчанию).
- Отображение **прогресса** в виде визуального барa.
- **Цикличный режим работы** — можно выполнять расчёты снова и снова.
- Возможность **выхода по команде**.

## Зависимости

Используются только стандартные библиотеки Python:
- `datetime`
- `calendar`
- `sys`

Ничего устанавливать не нужно!

## Как запустить

1. Убедитесь, что у вас установлен Python 3.x.
2. Скопируйте код в файл, например, `workday_progress.py`.
3. Запустите скрипт в терминале или командной строке:

```bash
python workday_progress.py
```

4. Следуйте инструкциям в консоли:
- Введите дату начала (или нажмите Enter для текущей даты).
- Введите дату окончания (или нажмите Enter для даты по умолчанию).
- Программа выведет прогресс-бар с текущим прогрессом рабочих дней.
- После этого вы можете повторить расчёт или выйти.

## Пример вывода

![image](https://github.com/user-attachments/assets/18dd7efd-fe15-4ece-85b0-fb1fe95c83c4)

