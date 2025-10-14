# В цьому прикладі ми створили (або перезаписали, якщо він вже існував) файл test.txt для запису та записали туди рядок 'hello!' завдовжки 6 символів. Для запису даних у файл ми використали метод write у об'єкта fh. 
# Цей метод повертає кількість записаних у файл символів - в нашому випадку число 6.

fh = open('test.txt', 'w')
symbols_written = fh.write('hello!')
print(symbols_written) # 6
fh.close()

# В цьому прикладі ми відкрили файл в режимі для читання та запису, але сам файл ми перезаписуємо, якщо він існує, бо використовується режим w+. 
# Записали у файл рядок 'hello!' та прочитали перші два символи із файлу за допомогою методу read, вказавши у якості аргументу двійку. Метод read повертає прочитанні символи і оскільки ми прочитали 2 символи, то змінна first_two_symbols буде зберігати рядок "he". Для того, щоб повернути вказівник на початок файлу ми викликали метод seek та передали йому позицію, куди потрібно переміститися 0. 

fh = open('test.txt', 'w+')
fh.write('hello!')
fh.seek(0)

first_two_symbols = fh.read(2)
print(first_two_symbols)  # 'he'

fh.close()

# Щоб прочитати увесь вміст файлу за раз, можна викликати метод read без аргументів:

fh = open('test.txt', 'w')
fh.write('hello!')
fh.close()

fh = open('test.txt', 'r')
all_file = fh.read()
print(all_file)  # 'hello!'

fh.close()

# Доки файловий дескриптор не закритий, ви можете читати із нього частинами, продовжуючи читання з того самого місця, на якому зупинилися:

fh = open('test.txt', 'w')
fh.write('hello!')
fh.close()

fh = open('test.txt', 'r')
while True:
    symbol = fh.read(1)
    if len(symbol) == 0:
        break
    print(symbol) # h
                 # e
                 # l
                 # l
                 # o
                 # !

fh.close()

# Метод readline() читає один рядок з файлу за раз. Якщо readline() повертає порожній рядок, це означає, що досягнуто кінця файлу, тому цикл переривається за допомогою break. 
# Кожен прочитаний рядок виводиться на екран. 
# Оскільки readline() зберігає символи переходу на новий рядок, кожен виведений рядок буде виведено з нового рядка.

fh = open('test_2.txt', 'w')
fh.write('first line\nsecond line\nthird line')
fh.close()

fh = open('test_2.txt', 'r')
while True:
    line = fh.readline()
    if not line:
        break
    print(line) # first line
                # second line
                # third line

fh.close()

# Та аналогічний метод readlines, який читає увесь файл повністю, але повертає список рядків, де елемент списку — це один рядок з файлу.

fh = open('test_3.txt', 'w')
fh.write('first line\nsecond line\nthird line')
fh.close()

fh = open('test_3.txt', 'r')
lines = fh.readlines()
print(lines) # ['first line\n', 'second line\n', 'third line']

fh.close()

# всі методи, які читають файли порядково, залишають (не видаляють) символ перенесення рядка \n.
# Його, за необхідності, треба видаляти самостійно 
# (наприклад, за допомогою методу рядків strip()):

fh = open("test_4.txt", "w")
fh.write("first line\nsecond line\nthird line")
fh.close()

fh = open("test_4.txt", "r")
lines = [el.strip() for el in fh.readlines()]
print(lines) # ['first line', 'second line', 'third line']

fh.close()

# Python дає можливість управляти положенням курсора (вказівника) у файлі та довільно переміщатися файлом за допомогою методу seek. 
# Цей метод приймає один аргумент — це кількість символів, на які потрібно змістити курсор у файлі:
# В цьому прикладі після запису у файл курсор буде зупинений на останньому символі. У виразі fh.seek(1) ми перемістили курсор на другий символ у файлі.

fh = open('test.txt', 'w+')
fh.write('hello!')

fh.seek(1)
second = fh.read(1)
print(second)  # 'e'

fh.close()


# Щоб дізнатися положення курсора в цей момент, можна скористатися методом tell, 
# він повертає позицію (номер) символу з початку файлу, де зараз знаходиться курсор.

fh = open("test.txt", "w+")
fh.write("hello!")

position = fh.tell()
print(position)  # 6

fh.seek(1)
position = fh.tell()
print(position)  # 1

fh.read(2)
position = fh.tell()
print(position)  # 3

fh.close()

# ===========================================================================
# Менеджер контексту

# Використання менеджера контексту (інструкції with) є кращою практикою для роботи з файлами в Python.
fh = open('text_.txt', 'w')
try:
    # Виконання операцій з файлом
    fh.write('Some data')
finally:
    # Закриття файлу в блоку finally гарантує, що файл закриється навіть у разі помилки
    fh.close()

with open("test_5.txt", "w") as fh:
    fh.write("first line\nsecond line\nthird line")

with open("test_5.txt", "r") as fh:
    lines = [el.strip() for el in fh.readlines()]

print(lines) # ['first line', 'second line', 'third line']

# ===========================================================================
# Робота з не текстовими файлами у Python

with open('raw_data.bin', 'wb') as fh:
    fh.write(b'Hello world!')

s = b'Hello!'
print(s[1])  # Виведе: 101 (це ASCII-код символу 'e')
print(s[1:4])  # Виведе: b'ell'

byte_str = 'some text'.encode()
print(byte_str) # b'some text'

# Перетворення списку чисел у байт-рядок
numbers = [0, 128, 255]
byte_numbers = bytes(numbers)
print(byte_numbers)  # Виведе байтове представлення чисел b'\x00\x80\xff'

for num in [127, 255, 156]:
  print(hex(num))
    # Виведе: 0x7f
    # Виведе: 0xff
    # Виведе: 0x9c

ord('a')  # 97

chr(97)  # 'a'

s = "Привіт!"

utf8 = s.encode()
print(f"UTF-8: {utf8}") # UTF-8: b'\xd0\x9f\xd1\x80\xd0\xb8\xd0\xb2\xd1\x96\xd1\x82!'

utf16 = s.encode("utf-16")
print(f"UTF-16: {utf16}") # UTF-16: b'\xff\xfeP\x00r\x00i\x00v\x00i\x00t\x00!\x00'

cp1251 = s.encode("cp1251")
print(f"CP-1251: {cp1251}") # CP-1251: b'\xcf\xf0\xe8\xe2\xe8\xf2!'

s_from_utf16 = utf16.decode("utf-16")
print(s_from_utf16 == s) # True

# Відкриття текстового файлу з явним вказівкам UTF-8 кодування
with open('example.txt', 'r', encoding='utf-8') as file:
    content = file.read()
    print(content)

