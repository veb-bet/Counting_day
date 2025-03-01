# Обратный отсчёт дней (будние дни)

Это программа для счёта обратного отсчёта дней, учитывая только будни.

## Использование

Чтобы использовать эту программу, вам потребуется Python и библиотеки datetime и calendar.

1. Установите Python, если ещё не сделали этого. Вы можете скачать его с официального сайта python.org.
2. Убедитесь, что у вас установлены библиотеки datetime и calendar. Они должны быть встроены в Python, так что вам не нужно устанавливать их отдельно.
3. Скопируйте и вставьте код в файл с расширением .py.
4. Запустите программу в среде Python.

## Как работает код

Эта программа создает функцию count_workdays, которая принимает две даты (начальную и конечную) в качестве аргументов и возвращает количество рабочих дней между ними. Функция использует цикл for для перебора дней между начальной и конечной датами и проверяет, является ли каждый день рабочим днем (с понедельника по пятницу). Если да, то функция увеличивает счетчик рабочих дней.

В приведенном примере начальная дата установлена равной текущей дате, а конечная дата установлена равной последнему дню 2023 года. Вы можете изменить конечную дату на любую другую, выбрав соответствующий формат даты (год, месяц, день).

## Результат

Чтобы увидеть результат работы программы, запустите её в среде Python. Результат будет выведен в консоль. 
