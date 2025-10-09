this_is_string = "Hi there!"

the_same_string = 'Hi there!'

this_is_string == the_same_string # True

text = """This is first line
And second line
Last third line"""

print(text)

song = '''Jingle bells, jingle bells
Jingle all the way
Oh, what fun it is to ride
In a one horse open sleigh'''

print(song)

one_line_text = "Textual data in Python is handled with str objects," \
                " or strings. Strings are immutable sequences of Unicode" \
                " code points. String literals are written in a variety " \
                " of ways: single quotes, double quotes, triple quoted."

print(one_line_text)

("spam " "eggs") == "spam eggs"  # True
('spam ' + 'eggs') == "spam eggs"  # True

print("Hello\nWorld") # Hello (new line) World
print("Hello\tWorld") # Hello (tab) World
print("Hello my little\rsister") # sistermy little
print("Hello\bWorld") # HelloWorld
print("Hello\\World") # Hello\World
print('I\'m a programmer') # I'm a programmer
print("He said: \"Hello!\"") # He said: "Hello!"

text = "  Hello World! Welcome to Python programming.  "

print(text.upper())  # Перетворення всіх літер на великі
print(text.lower())  # Перетворення всіх літер на малі
print(text.title())  # Перетворення першої літери кожного слова на велику
print(text.capitalize())  # Перетворення першої літери речення на велику
print(text.strip())  # Видалення пробілів на початку та в кінці рядка

# Методи рядків
# Пошук у рядку

s = "Hi there!"

start = 0
end = 7

print(s.find("er", start, end)) # 5
print(s.find("q")) # -1

s = 'Some words'

print(s.find("o")) # 1
print(s.rfind('o')) # 6

s = 'Some words'

print(s.index("o")) # 1
print(s.rindex('o')) # 6    

# Поділ та об'єднання рядків 
# Метод split()  str.split(separator=None, maxsplit=-1)

text = "hello world"
result = text.split()
print(result)  # Виведе: ['hello', 'world']
text = "apple,banana,cherry"
result = text.split(',')
print(result)  # Виведе: ['apple', 'banana', 'cherry']

# Метод join() string.join(iterable)

list_of_strings = ['Hello', 'world']
result = ' '.join(list_of_strings)
print(result)  # Виведе: 'Hello world'

elements = ['earth', 'air', 'fire', 'water']
result = ', '.join(elements)
print(result)  # Виведе: 'earth, air, fire, water'


# Якщо потрібно видалити зайві пробіли на початку і в кінці рядка, є спеціальний метод strip(). У цього метода є два "брати":
# "лівий", lstrip, видаляє тільки пробіли на початку рядка;
# "правий", rstrip, видаляє тільки пробіли в кінці рядка.

clean = '   spacious   '.strip()
print(clean) # spacious

# Метод replace() має наступний синтаксис str.replace(old, new, count=-1)

text = "Hello world"
new_text = text.replace("world", "Python")
print(new_text) # Виведе: Hello Python

text = "one fish, two fish, red fish, blue fish"
new_text = text.replace("fish", "bird", 2)
print(new_text)  # Виведе: one bird, two bird, red fish, blue fish

# Метод replace() також застосовують для видалення підрядка
text = "Hello, world!"
new_text = text.replace(" world", "")
print(new_text) # Виведе: Hello!

# Для видалення фіксованої послідовності на початку рядка є метод removeprefix:
print('TestHook'.removeprefix('Test')) # Hook
print('TestHook'.removeprefix('Hook')) # TestHook

# Є парний метод для видалення послідовності в кінці рядка, removesuffix:
print('TestHook'.removesuffix('Test')) # TestHook
print('TestHook'.removesuffix('Hook')) # Test

# ==============================================================================

# Розглянемо наступну задачу та використаємо основні інструменти для роботи з рядками - методи split() та replace(). Ви маєте URL пошукового запиту, і ваше завдання - видобути та обробити параметри цього запиту. Наприклад пошуковий запит "Cat and dog"

# Спочатку нам треба отримати частини запиту з URL:

url_search = "<https://www.google.com/search?q=Cat+and+dog&ie=utf-8&oe=utf-8&aq=t>"
url_search = url_search.strip('<>') # Видаляємо кутові дужки
_, query = url_search.split('?')
print(query) # q=Cat+and+dog&ie=utf-8&oe=utf-8&aq=t

obj_query = {}
for el in query.split('&'):
    key, value = el.split('=')
    obj_query.update({key: value.replace('+', ' ')})
print(obj_query) # {'q': 'Cat and dog', 'ie': 'utf-8', 'oe': 'utf-8', 'aq': 't'}

# ==============================================================================

# isdigit() використовується для перевірки, чи складається рядок повністю з цифр. Цей метод повертає True, якщо всі символи в рядку є цифрами та рядок складається принаймні з одного символу, інакше повертає False.

print("123".isdigit())  # True
print("123a".isdigit()) # False

number = "12345"
print(number.isdigit())  # Виведе: True

text = "Number123"
print(text.isdigit())  # Виведе: False


user_input = input("Введіть число: ")
if user_input.isdigit():
    print("Це дійсно число!")
else:
    print("Це не число!")
    
for char in "Hello 123":
    if char.isdigit():
        print(f"'{char}' - це цифра")
    else:
        print(f"'{char}' - не цифра")

# Метод translate()

intab = "aeiou"
outtab = "12345"
trantab = str.maketrans(intab, outtab)

str = "This is string example"
print(str.translate(trantab)) # Th3s 3s str3ng 2x1mpl2

intab = "aeiou"
trantab = str.maketrans('', '', intab)

str = "This is string example"
print(str.translate(trantab)) # Ths s strng xmpl

symbols = "0123456789ABCDEF"
code = [
        '0000', '0001', '0010', '0011', '0100', '0101', '0110', '0111',
        '1000', '1001', '1010', '1011', '1100', '1101', '1110', '1111'
        ]

MAP = {}

for s, c in zip(symbols, code):
    MAP[ord(s)] = c
    MAP[ord(s.lower())] = c

print(MAP)
result = "34 DF 56 AC".translate(MAP)
print(result) # 00110100 11011111 01010110 10101100

# ===============================================================================
# розробити програму, яка перетворює вхідний текстовий рядок на відповідний код мови Морзе.

morze_dict = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
              'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
              'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
              'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
              'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---',
              '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
              '8': '---..', '9': '----.'}

# Перетворення ключів словника на Unicode коди
table_morze_dict = {}
for k, v in morze_dict.items():
    table_morze_dict[ord(k)] = v

string = "Hello world"

result = ""

for ch in string:
    result = result + ch.upper().translate(table_morze_dict)

print(result)
# .... . .-.. .-.. --- / .-- --- .-. .-.. -..
# ===============================================================================

# Форматування рядків

for i in range(8):
    s = f"int: {i:d};  hex: {i:#x};  oct: {i:#o};  bin: {i:#b}"
    print(s)

# int: 0;  hex: 0x0;  oct: 0o0;  bin: 0b0
# int: 1;  hex: 0x1;  oct: 0o1;  bin: 0b1
# int: 2;  hex: 0x2;  oct: 0o2;  bin: 0b10
# int: 3;  hex: 0x3;  oct: 0o3;  bin: 0b11
# int: 4;  hex: 0x4;  oct: 0o4;  bin: 0b100
# int: 5;  hex: 0x5;  oct: 0o5;  bin: 0b101
# int: 6;  hex: 0x6;  oct: 0o6;  bin: 0b110
# int: 7;  hex: 0x7;  oct: 0o7;  bin: 0b111

price = 19.99
quantity = 3
total = f"Total: {price * quantity:.2f}"
print(total) # Total: 59.97

width = 5
for num in range(12):
    print(f'{num:^10} {num**2:^10} {num**3:^10}')

# Вирівнювання визначає, як вміст буде вирівняний всередині вказаної ширини поля. Можливі варіанти вирівнювання:

# <: Вирівнювання вмісту по лівому краю.
# >: Вирівнювання вмісту по правому краю.
# ^: Вирівнювання вмісту по центру.
# =: Використовується для вирівнювання чисел, при цьому знак (якщо він є) відображається зліва, а число - по правому краю поля.


name = "Alice"
formatted = f"{name:>10}"
print(formatted)  # Виведе: '     Alice' (вирівнювання праворуч)

# Форматування відсотків у f-рядках виглядає так:
# f"{value:<ширина>.<точність>%}"

completion = 0.756
formatted = f"{completion:.1%}"
print(formatted)  # Виведе: '75.6%'

progress = 0.5
formatted = f"{progress:.0%}"
print(formatted) # Виведе: '50%'

# Регулярні вирази
# Метод search() re.search(pattern, string) 
# Результат виконання re.search() це спеціальний об'єкт Match, якщо знаходить відповідність. Якщо відповідність не знайдена, повертає None.

# Об'єкт Match має властивості та методи, що використовуються для отримання інформації про пошук та результат:
# Match.span() повертає кортеж, що містить початкову та кінцеву позиції збігу.
# Match.string повертає рядок, переданий у функцію,
# Match.group() повертає частину рядка, в якому був збіг

import re

text = "Вивчення Python може бути веселим."
pattern = "Python"
match = re.search(pattern, text)

if match:
    print("Знайдено:", match.group())
else:
    print("Не знайдено.") 
# Знайдено: Python

text = "Вивчення Python може бути веселим."
pattern = r"в\w*м"
match = re.search(pattern, text, re.IGNORECASE)

if match:
    print("Знайдено:", match.group())
# Знайдено: веселим

# ==============================================================================
# Розглянемо простеньку задачу - знаходження електронної адреси в рядку.

text = "Моя електронна адреса: example@example.com"
pattern = r"\w+@\w+\.\w+"
match = re.search(pattern, text)

if match:
    print("Електронна адреса:", match.group())
else:
    print("Не знайдено.")
# Електронна адреса: example@example.com

# Припустимо, у нас є рядок з електронною адресою, і ми хочемо вилучити ім'я користувача та домен цієї електронної адреси окремо. 
# Треба розділити "username@domain.com" на "username" (ім'я користувача) та "domain.com" (домен).

email = "username@domain.com"
pattern = r"(\w+)@(\w+\.\w+)"
match = re.search(pattern, email)

if match:
    user_name = match.group(1)
    domain_name = match.group(2)
    print("Ім'я користувача:", user_name)
    print("Домен:", domain_name)
# Ім'я користувача: username
# Домен: domain.com

# ==============================================================================

import random
coin = {1: 'Orel', 2: 'Peshcka'}

count_O = 0
count_P = 0

seq = []
while count_O < 4 and count_P < 4:
    choice = random.randint(1, 2)
    if choice == 1:
        count_O += 1
        count_P = 0
    else:
        count_P += 1
        count_O = 0

    seq.append(coin[choice])

print(seq)
print(len(seq))

# ==============================================================================
# Метод re.findall() використовується для знаходження всіх входжень шаблону, заданого регулярним виразом, у заданому рядку.

text = "Рік 2023 був складнішим, ніж 2022"
pattern = r"\d+"
matches = re.findall(pattern, text)

print(matches) # ['2023', '2022']

# У цьому прикладі регулярний вираз \d+ шукає одну або більше цифр у рядку підряд та знаходить їх, на виході ми отримуємо список всіх чисел в рядку.

text = "Python - це проста, але потужна мова програмування."
pattern = r"\w+"
matches = re.findall(pattern, text)

print(matches)  # Виведе список всіх слів у рядку
# ['Python', 'це', 'проста', 'але', 'потужна', 'мова', 'програмування']

text = "Контакти: example1@example.com, example2@sample.org"
pattern = r"\w+@\w+\.\w+"
matches = re.findall(pattern, text)

print(matches)  # Виведе всі знайдені електронні адреси
# ['example1@example.com', 'example2@sample.org']

# Метод re.sub() в модулі re Python використовується для заміни входжень регулярного виразу pattern в рядку string на рядок repl. 
# modified_string = re.sub(pattern, repl, string)

# Замінити всі пробільні символи на підкреслення.
file_name = "Мій документ Python.txt"
pattern = r"\s"
replacement = "_"
formatted_name = re.sub(pattern, replacement, file_name)

print(formatted_name)  # Мій_документ_Python.txt

# Видалимо всі пунктуаційні знаки з рядка.

text = "Python - потужна, універсальна; мова!"
pattern = r"[;,\-:!\.]"
replacement = ""
modified_text = re.sub(pattern, replacement, text)

print(modified_text) # Python потужна універсальна мова

# Нам необхідно змінити формат телефонних номерів. 
# В тексті в нас телефони записані в такому форматі 050-171-1634, 
# нам необхідно замінити їх на формат (050) 171-1634

phone = """
        Михайло Куліш: 050-171-1634
        Вікторія Кущ: 063-134-1729
        Оксана Гавриленко: 068-234-5612
        """
pattern = r"(\d{3})-(\d{3})-(\d{4})"
replacement = r"(\1) \2-\3"
formatted_phone = re.sub(pattern, replacement, phone)

print(formatted_phone) 
# Михайло Куліш: (050) 171-1634
# Вікторія Кущ: (063) 134-1729
# Оксана Гавриленко: (068) 234-5612

# Функція re.split() в модулі re Python використовується для розбивання рядка за заданим регулярним виразом. Це дозволяє розділяти текст на частини за складнішими критеріями, ніж простий рядковий метод split().
# list_of_elements = re.split(pattern, string)

# розділимо рядок на слова, використовуючи пробіли як роздільники.
text = "Python - це проста, але потужна мова програмування."
pattern = r"\s+"
words = re.split(pattern, text)

print(words)  # ['Python', '-', 'це', 'проста,', 'але', 'потужна', 'мова', 'програмування.']

# розділити рядок на частини, використовуючи пунктуаційні знаки як роздільники.

text = "Python - потужна; проста, універсальна: мова!"
pattern = r"[;,\-:!\s]+"
elements = re.split(pattern, text)

print(elements)  # ['Python', 'потужна', 'проста', 'універсальна', 'мова', '']

import re

text = "apple#banana!mango@orange;kiwi"
pattern = r"[#@;!]"
fruits = re.split(pattern, text)

print(fruits)
# ['apple', 'banana', 'mango', 'orange', 'kiwi']