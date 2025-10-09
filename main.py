# Модулі datetime та time. Робота з випадковими величинами. 
# Модуль math.

# Перед роботою з датами і часом потрібно імпортувати модуль в нашому скрипті:
import datetime
now = datetime.datetime.now()
print(now)

# об'єкт datetime в свій скрипт ми також можемо отримати, просто витягнув його з модуля:
from datetime import datetime, date, time

current_datetime = datetime.now()

print(current_datetime.year)
print(current_datetime.month)
print(current_datetime.day)
print(current_datetime.hour)
print(current_datetime.minute)
print(current_datetime.second)
print(current_datetime.microsecond)
print(current_datetime.tzinfo)

# В об'єкта datetime є методи, щоб отримати дату (без часу) та час (без дати):
print(current_datetime.date())
print(current_datetime.time())

# Є зворотний метод datetime.combine який використовується для створення нового об'єкта datetime шляхом комбінування об'єктів date та time. 
# datetime.datetime.combine(date_object, time_object)

# Створення об'єктів date і time
date_part = date(2023, 12, 14)
time_part = time(12, 30, 15)

# Комбінування дати і часу в один об'єкт datetime
combined_datetime = datetime.combine(date_part, time_part)

print(combined_datetime)  # Виведе "2023-12-14 12:30:15"

# Створення об'єкта datetime з конкретною датою
specific_date = datetime(year=2020, month=1, day=7)

print(specific_date)  # Виведе "2020-01-07 00:00:00"

# Створення об'єкта datetime з конкретною датою і часом
specific_datetime = datetime(2020, 1, 7, 14, 30, 15)

print(specific_datetime)  # Виведе "2020-01-07 14:30:15"

# Отримання номера дня тижня
day_of_week = now.weekday()

# Поверне число від 0 (понеділок) до 6 (неділя)
print(f"Сьогодні: {day_of_week}") # Виведе номер дня тижня

# Створення двох об'єктів datetime
datetime1 = datetime(2023, 3, 14, 12, 0)
datetime2 = datetime(2023, 3, 15, 12, 0)

# Порівняння дат
print(datetime1 == datetime2)  # False, тому що дати не однакові
print(datetime1 != datetime2)  # True, тому що дати різні
print(datetime1 < datetime2)   # True, тому що datetime1 передує datetime2
print(datetime1 > datetime2)   # False, тому що datetime1 не наступає за datetime2

# Робота з часовими проміжками timedelta

from datetime import timedelta
delta = timedelta(
    days=50,
    seconds=27,
    microseconds=10,
    milliseconds=29000,
    minutes=5,
    hours=8,
    weeks=2
)
print(delta)
print(f"days: {delta.days}, seconds: {delta.seconds}, microseconds: {delta.microseconds}")

seventh_day_2019 = datetime(year=2019, month=1, day=7, hour=14)
seventh_day_2020 = datetime(year=2020, month=1, day=7, hour=14)

difference = seventh_day_2020 - seventh_day_2019
print(difference)  # 365 days, 0:00:00
print(difference.total_seconds())  # 31536000.0

now = datetime.now()
future_date = now + timedelta(days=10)  # Додаємо 10 днів до поточної дати
print(future_date)

seventh_day_2020 = datetime(year=2020, month=1, day=7, hour=14)
four_weeks_interval = timedelta(weeks=4)

print(seventh_day_2020 + four_weeks_interval)  # 2020-02-04 14:00:00
print(seventh_day_2020 - four_weeks_interval)  # 2019-12-10 14:00:00

# Ми можемо використати метод toordinal(), який повертає порядковий номер дня, 
# враховуючи кількість днів з 1 січня року 1 нашої ери (тобто з початку християнського календаря). 
# Цей метод перетворює об'єкт datetime в ціле число, що представляє порядковий номер даного дня.

# Створення об'єкта datetime
date = datetime(year=2023, month=12, day=18)

# Отримання порядкового номера
ordinal_number = date.toordinal()
print(f"Порядковий номер дати {date} становить {ordinal_number}")

from datetime import datetime

# Встановлення дати спалення Москви Наполеоном (14 вересня 1812 року)
napoleon_burns_moscow = datetime(year=1812, month=9, day=14)

# Поточна дата
current_date = datetime.now()

# Розрахунок кількості днів
days_since = current_date.toordinal() - napoleon_burns_moscow.toordinal()
print(days_since)
# Виведе кількість днів, що минули з 14 вересня 1812 року до сьогоднішнього дня

# Робота з timestamp
# ☝ timestamp є універсальним способом представлення часу, оскільки він не залежить від часових зон і календарних систем.

# Конвертація datetime в timestamp

# Поточний час
now = datetime.now()

# Конвертація datetime в timestamp
timestamp = datetime.timestamp(now)
print(timestamp)  # Виведе timestamp поточного часу

# Конвертація timestamp в datetime
# Припустимо, є timestamp
timestamp = 1617183600

# Конвертація timestamp назад у datetime
dt_object = datetime.fromtimestamp(timestamp)
print(dt_object)  # Виведе відповідний datetime

# Парсинг дати із рядка datetime_object.strftime(format)

# Форматування дати і часу
formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")
print('formatted_date', formatted_date)

# Форматування лише дати
formatted_date_only = now.strftime("%A, %d %B %Y")
print('formatted_date_only', formatted_date_only)

# Форматування лише часу
formatted_time_only = now.strftime("%I:%M %p")
print('formatted_time_only', formatted_time_only)

# Форматування лише дати
formatted_date_only = now.strftime("%d.%m.%Y")
print('formatted_date_only', formatted_date_only)

# Синтаксис методу strptime виглядає наступним чином:
# datetime_object = datetime.strptime(string, format)
# string - рядок, який потрібно розпарсити у дату
# format - формат рядка, який потрібно розпарсити

# Припустимо, у нас є дата у вигляді рядка
date_string = "2023.03.14"

# Перетворення рядка в об'єкт datetime
datetime_object = datetime.strptime(date_string, "%Y.%m.%d")
print(datetime_object)  # Виведе об'єкт datetime, що відповідає вказаній даті та часу

# Конвертація у формат ISO 8601
iso_format = now.isoformat()
print(iso_format)  # Виведе дату і час у форматі ISO 8601

iso_date_string = "2023-03-14T12:39:29.992996"

# Конвертація з ISO формату
date_from_iso = datetime.fromisoformat(iso_date_string)
print(date_from_iso)  # Виведе об'єкт datetime, що відповідає вказаній даті та часу

# Метод isoweekday() у об'єкті datetime використовується для отримання дня тижня відповідно до ISO 8601. Згідно з цим стандартом, тиждень починається з понеділка, який має значення 1, і закінчується неділею, яка має значення 7.
# Використання isoweekday() для отримання дня тижня
day_of_week = now.isoweekday()

print(f"Сьогодні: {day_of_week}")  # Поверне число від 1 до 7, що відповідає дню тижня

# isocalendar() - це кортеж (ISO_рік, ISO_тиждень, ISO_день_тижня), де:
# ISO_рік - це рік у форматі ISO.
# ISO_тиждень - номер тижня в році за ISO 8601 (від 1 до 53).
# ISO_день_тижня - день тижня за ISO 8601, де 1 означає понеділок, а 7 - неділю.

# Отримання ISO календаря
iso_calendar = now.isocalendar()

print(f"ISO рік: {iso_calendar[0]}, ISO тиждень: {iso_calendar[1]}, ISO день тижня: {iso_calendar[2]}")

# Робота з часовими зонами
from datetime import timezone, timedelta

local_now = datetime.now()
utc_now = datetime.now(timezone.utc)

print(local_now)
print(utc_now)  # Виведе поточний час в UTC

# для перетворення UTC часу в час, що відповідає Східному часовому поясу США (UTC-5 годин), можна зробити наступне:

from datetime import datetime, timezone, timedelta

utc_time = datetime.now(timezone.utc)

# Створення часової зони для Східного часового поясу (UTC-5)
eastern_time = utc_time.astimezone(timezone(timedelta(hours=-5)))
# Перетворює час UTC в час Східного часового поясу
print(eastern_time)  

# Щоб перетворити локальний час у час UTC, спочатку потрібно призначити
# локальному часу відповідну часову зону, а потім використати метод astimezone() для конвертації його в UTC:

# Припустимо, місцевий час належить до часової зони UTC+2
local_timezone = timezone(timedelta(hours=2))
local_time = datetime(year=2023, month=3, day=14, hour=12, minute=30, second=0, tzinfo=local_timezone)

# Конвертація локального часу в UTC
utc_time = local_time.astimezone(timezone.utc)
print(utc_time)  # Виведе час в UTC

# Стандарт ISO 8601 також підтримує часові зони. 
# У Python це можна зробити, додавши інформацію про часову зону до об'єкта datetime:

from datetime import datetime, timezone, timedelta

# Час у конкретній часовій зоні
timezone_offset = timezone(timedelta(hours=2))  # Наприклад, UTC+2
timezone_datetime = datetime(year=2023, month=3, day=14, hour=12, minute=30, second=0, tzinfo=timezone_offset)

# Конвертація у формат ISO 8601
iso_format_with_timezone = timezone_datetime.isoformat()
print(iso_format_with_timezone)

# Робота з часом
# Метод time.time() повертає поточний час у секундах з 1 січня 1970 року (epoch time).

import time

current_time = time.time()
print(f"Поточний час: {current_time}")
# Виведе поточний час у секундах з 1 січня 1970 року

# Метод time.sleep(seconds) зупиняє виконання програми на вказану кількість секунд. 
# Наприклад цей код зупиняє виконання програми на 5 секунд.

print("Початок паузи")
time.sleep(5)
print("Кінець паузи")

# Метод time.ctime([seconds]) перетворює часову мітку (кількість секунд) у зрозуміле для людини текстове представлення. 
# Якщо аргумент не вказаний, використовується поточний час.

print(f"Поточний час: {current_time}")

readable_time = time.ctime(current_time)
print(f"Читабельний час: {readable_time}")  # Виведе поточний час у зрозумілому форматі

# Метод time.localtime([seconds]) перетворює часову мітку в структуру struct_time у місцевій часовій зоні.

local_time = time.localtime(current_time)
print(f"Місцевий час: {local_time}")



# Записуємо час на початку виконання
start_time = time.perf_counter()

# Виконуємо якусь операцію
for _ in range(1_000_000):
    pass  # Просто проходить цикл мільйон разів

# Записуємо час після виконання операції
end_time = time.perf_counter()

# Розраховуємо та виводимо час виконання
execution_time = end_time - start_time
print(f"Час виконання: {execution_time} секунд")

# Один мільйон
a = 1_000_000
print(a)  # Виведе 1000000

# Десять мільйонів
b = 10_000_000
print(b)  # Виведе 10000000

# Один мільярд
c = 1_000_000_000
print(c)  # Виведе 1000000000


# ============================================================================== # 
# Модуль random використовується для генерації випадкових чисел та вибору випадкових елементів з послідовностей.

import random
# Генерація випадкового цілого числа в діапазоні від 1 до 10
random_integer = random.randint(1, 10)
print(f"Випадкове ціле число: {random_integer}")

# Симуляція кидка кубика

dice_roll = random.randint(1, 6)
print(f"Ви кинули {dice_roll}")

# Метод random.random() потрібен, щоб отримати випадкове число в інтервалі 0, 1. 
# Він генерує випадкове дійсне число між 0.0 (включно) та 1.0 (не включно):

random_float = random.random()
print(f"Випадкове дійсне число: {random_float}")

# Припустимо, вам потрібно симулювати випадкове відсоткове заповнення. Можна використовувати random.random() для цього:

percentage_fill = random.random() * 100
print(f"Випадкове відсоткове заповнення: {percentage_fill:.2f}%")

# Метод random.randrange(start, stop[, step]) повертає випадково вибране число з заданого діапазону.

random_range = random.randrange(0, 101, 5)  # Випадкове число від 0 до 100 з кроком 5
print(f"Випадкове число з діапазону: {random_range}")

# Симуляція пострілу по мішені, але необхідно вибрати випадковий номер від 1 до 10, та лише непарні числа:

target = random.randrange(1, 11, 2)
print(f"Ціль: {target}")

# Перемішування колоди карт:

cards = ["Туз", "Король", "Дама", "Валет", "10", "9", "8", "7", "6"]

random.shuffle(cards)

print(f"Перемішана колода: {cards}")

# Вибір випадкового фрукта:

fruits = ['apple', 'banana', 'orange']
print(random.choice(fruits))

items = ['яблуко', 'банан', 'вишня', 'диня']
chosen_item = random.choices(items, k=1)
chosen_item_3 = random.choices(items, k=3)
print(chosen_item)  # Виведе випадковий фрукт з списку
print(chosen_item_3)  # Виведе список з трьох випадкових фруктів

numbers = [1, 2, 3, 4, 5]
chosen_numbers = random.choices(numbers, k=3)
print(chosen_numbers)  # Виведе список з трьох випадкових чисел

# Вибір з вагами
colors = ['червоний', 'зелений', 'синій']
weights = [10, 1, 1]
chosen_color = random.choices(colors, weights, k=1)
print(chosen_color)  # Виведе 'червоний' з ймовірністю 10/12, 'зелений' або 'синій' з ймовірністю 1/12

import random

participants = ['Анна', 'Богдан', 'Віктор', 'Галина', 'Дмитро', 'Олена', 'Женя', 'Зорян', 'Ігор', 'Йосип']
team = random.sample(participants, 4)
print(f"Команда: {team}") # Виведе випадкову команду з 4 учасників


price = random.uniform(50, 100)
print(f"Випадкова ціна: {price:.2f}")  # Виведе випадкове дійсне число між 50 і 100

#  =============================================================================== #
# Модуль math надає доступ до математичних функцій і констант.
import math

# Вихідне число
x = 3.7

# Використання різних методів округлення
ceil_result = math.ceil(x)  # Округлення вгору
floor_result = math.floor(x)  # Округлення вниз
trunc_result = math.trunc(x)  # Відсікання дробової частини

print(ceil_result, floor_result, trunc_result) # Виведе: 4 3 3
print(math.pi)  # Виведе значення числа π (пі)
print(math.e)   # Виведе значення числа e (основа натурального логарифму)
print(math.tau)  # Виведе значення числа τ (тау)
print(math.inf)  # Виведе позитивну нескінченність
print(math.nan)  # Виведе "не число" (NaN)

# Тригонометрія
angle = math.radians(60)  # Конвертація з градусів у радіани
print(math.sin(angle))  # Синус кута

# Корінь числа
print(math.sqrt(9))  # Квадратний корінь з 9

# Логарифми
print(math.log(10, 2))  # Логарифм 10 за основою 2

print(math.factorial(5))  # Факторіал числа 5 (5!) = 120

r = math.isclose(0.1 + 0.2, 0.3)
print(r)  # Це поверне True

r1 = math.isclose(0.1, 0.10000000009)
print(r1)  # Це поверне True
