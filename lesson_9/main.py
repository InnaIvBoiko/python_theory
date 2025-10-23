# Ми створимо клас Pokemon, що ілюструє основні принципи об'єктно-орієнтованого програмування (ООП), а потім створимо об'єкт класу Pokemon - pikachu. Клас Pokemon буде містити атрибути: name, type, і health.

# Для класу ми визначимо наступні методи:

# attack (напад) - дозволяє покемону атакувати іншого покемона.
# dodge (уклон) - дає можливість уникнути атаки.
# evolve (еволюціонувати) - дозволяє покемону еволюціонувати в іншу форму.

class Pokemon:
    def __init__(self, name, type, health):
        self.name = name # Ініціалізація атрибута імені
        self.type = type # Ініціалізація атрибута типу
        self.health = health # Ініціалізація атрибута здоров'я

    def attack(self, other_pokemon):
        print(f"{self.name} attacks {other_pokemon.name}!")

    def dodge(self):
        print(f"{self.name} dodged the attack!")

    def evolve(self, new_form):
        print(f"{self.name} is evolving into {new_form}!")
        self.name = new_form

# Створення об'єкта Pikachu
pikachu = Pokemon("Pikachu", "Electric", 100)

# Використання методів
pikachu.attack(Pokemon("Charmander", "Fire", 100)) # Pikachu attacks Charmander!
pikachu.dodge() # Pikachu dodged the attack!
pikachu.evolve("Raichu") # Pikachu is evolving into Raichu!

# За допомогою атрибутів та методів класу ми виконуємо інкапсуляцію — приховуємо деталі реалізації під інтерфейсом класу. 
# Це дозволяє легко створювати нові об'єкти покемонів з однаковою структурою, але різними значеннями атрибутів, що ілюструє принцип абстракції.

class PersonPublic:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def greeting(self) -> str:
        return f"Hi {self.name}"

p = PersonPublic("Boris", 34) 
print(p.greeting()) # Hi Boris

class Person:
    def __init__(self, name: str, age: int, is_active: bool):
        self.name = name
        self.age = age
        self._is_active = is_active

    def greeting(self):
        return f"Hi {self.name}"

p = Person("Boris", 34, True)
print(p.name, p.age, p._is_active)
print(p.greeting())


# Protected used _
class PersonProtected:
    def __init__(self, name: str, age: int, is_active: bool):
        self.name = name
        self.age = age
        self._is_active = is_active

    def greeting(self):
        return f"Hi {self.name}"
    
    def is_active(self):
        return self._is_active

    def set_active(self, active: bool):
        self._is_active = active

p = PersonProtected("Boris", 34, True)
print(p.name, p.age, p.is_active())
print(p.greeting())


# Private used __
class PersonPrivate:
    def __init__(self, name: str, age: int, is_active: bool, is_admin: bool):
        self.name = name
        self.age = age
        self._is_active = is_active
        self.__is_admin = is_admin

    def greeting(self):
        return f"Hi {self.name}"

    def is_active(self):
        return self._is_active

    def set_active(self, active: bool):
        self._is_active = active

p = PersonPrivate("Boris", 34, True, False)
#print(p.__is_admin) # AttributeError: 'PersonPrivate' object has no attribute '__is_admin'

print(p._PersonPrivate__is_admin) # False (accessing private attribute using name mangling)

# Щоб реалізувати методи доступу до приватного поля __is_admin у класі Person, ми можемо використати той самий підхід, що і до захищеного поля _is_active
class Person:
    def __init__(self, name: str, age: int, is_active: bool, is_admin: bool):
        self.name = name
        self.age = age
        self._is_active = is_active
        self.__is_admin = is_admin

    def greeting(self):
        return f"Hi {self.name}"

    def is_active(self):
        return self._is_active

    def set_active(self, active: bool):
        self._is_active = active

    def get_is_admin(self):
        return self.__is_admin

    def set_is_admin(self, is_admin: bool):
        # Тут можна додати будь-яку логіку перевірки або обробки
        self.__is_admin = is_admin

        
p = Person("Boris", 34, True, False)
print(p.get_is_admin())
p.set_is_admin(True)
print(p.get_is_admin())

# =============================== Наслідування - це механізм, який дозволяє створювати нові класи на основі існуючих. ===============================
# Розглянемо приклад де буде базовий клас Animal. Він може мати загальні властивості для всіх тварин, наприклад, nickname (ім'я), age (вік) і метод make_sound() (видавати звук). 
# А також похідні класи Cat, Dog та Cow, які наслідують властивості та методи від класу Animal, але також можуть мати свої унікальні методи або перевизначені методи базового класу.

class Animal:
    def __init__(self, nickname: str, age: int):
        self.nickname = nickname
        self.age = age

    def make_sound(self):
        pass

class Cat(Animal):
    def make_sound(self) -> str:
        return "Meow"

class Dog(Animal):
    def make_sound(self) -> str:
        return "Woof"

class Cow(Animal):  
    def make_sound(self):
        return "Moo"

my_cat = Cat("Simon", 4)
my_dog = Dog("Rex", 5)
my_cow = Cow("Bessie", 3)

print(my_cat.make_sound())  # Виведе "Meow"
print(my_dog.make_sound())  # Виведе "Woof"
print(my_cow.make_sound())  # Виведе "Moo"


class Dog(Animal):
    def __init__(self, nickname: str, age: int, breed: str):
        super().__init__(nickname, age)  # Викликаємо конструктор базового класу
        self.breed = breed  # Додаємо нову властивість

    def make_sound(self):
        return "Woof"

    def chase_tail(self):
        return f"{self.nickname} is chasing its tail!"

my_dog = Dog("Rex", 5, "Golden Retriever")
print(my_dog.make_sound())  # Виведе "Woof"
print(my_dog.chase_tail())  # Виведе "Rex is chasing its tail!"

# ============================== Багаторівневе наслідування та Method Resolution Order (MRO) ==============================

class Bird(Animal):
    def make_sound(self):
        return "Chirp"

class Parrot(Bird):
    def can_fly(self):
        return True

class TalkingParrot(Parrot):
    def say_phrase(self, phrase):
        return f"The parrot says: '{phrase}'"

my_parrot = TalkingParrot("Alice", 2)
print(my_parrot.make_sound())
print(my_parrot.can_fly())
print(my_parrot.say_phrase("Hello, World!"))


# ============================= Поліморфізм =============================

class Animal:
    def __init__(self, nickname: str, age: int):
        self.nickname = nickname
        self.age = age

    def make_sound(self):
        pass

class Cat(Animal):
    def make_sound(self):
        return "Meow"

class Dog(Animal):
    def make_sound(self):
        return "Woof"

def animal_sounds(animals):
    for animal in animals:
        print(animal.make_sound())

animals = [Cat("Simon", 4), Dog("Rex", 5)]
animal_sounds(animals)


class Duck:
    def quack(self):
        print("Quack, quack!")

class Person:
    def quack(self):
        print("I'm Quacking Like a Duck!")

def make_it_quack(duck):
    duck.quack()

duck = Duck()
person = Person()

make_it_quack(duck)
make_it_quack(person)


class Dog:
    def speak(self) -> str:
        return "Woof"

class Cat:
    def speak(self) -> str:
        return "Meow"

class Robot:
    def speak(self) -> str:
        return "Beep boop"

def make_it_speak(speaker) -> None:
    print(speaker.speak())

dog = Dog()
cat = Cat()
robot = Robot()

make_it_speak(dog)  # Виведе: Woof
make_it_speak(cat)  # Виведе: Meow
make_it_speak(robot)  # Виведе: Beep boop


# ============================= Детальний приклад: Клас з декількома методами =============================

class Student:
    """Клас для представлення студента з різними методами"""
    
    # Атрибут класу (спільний для всіх екземплярів)
    university = "Київський національний університет"
    
    def __init__(self, name: str, age: int, student_id: str):
        """Конструктор класу - ініціалізує поля екземпляра"""
        self.name = name
        self.age = age
        self.student_id = student_id
        self.grades = []  # Список оцінок
        self.subjects = []  # Список предметів
    
    def introduce(self) -> str:
        """Метод для представлення студента"""
        return f"Привіт! Мене звати {self.name}, мені {self.age} років. ID: {self.student_id}"
    
    def add_subject(self, subject: str) -> None:
        """Метод для додавання предмета"""
        if subject not in self.subjects:
            self.subjects.append(subject)
            print(f"Предмет '{subject}' додано до списку")
        else:
            print(f"Предмет '{subject}' вже є в списку")
    
    def add_grade(self, subject: str, grade: int) -> None:
        """Метод для додавання оцінки з предмета"""
        if subject in self.subjects:
            if 1 <= grade <= 5:
                self.grades.append({"subject": subject, "grade": grade})
                print(f"Додано оцінку {grade} з предмета '{subject}'")
            else:
                print("Оцінка повинна бути від 1 до 5")
        else:
            print(f"Спочатку додайте предмет '{subject}' до списку")
    
    def get_average_grade(self) -> float:
        """Метод для обчислення середньої оцінки"""
        if not self.grades:
            return 0.0
        total = sum(grade["grade"] for grade in self.grades)
        return round(total / len(self.grades), 2)
    
    def get_grades_by_subject(self, subject: str) -> list:
        """Метод для отримання оцінок з конкретного предмета"""
        return [grade["grade"] for grade in self.grades if grade["subject"] == subject]
    
    def display_info(self) -> None:
        """Метод для відображення повної інформації про студента"""
        print(f"\n=== Інформація про студента ===")
        print(f"Ім'я: {self.name}")
        print(f"Вік: {self.age}")
        print(f"ID: {self.student_id}")
        print(f"Університет: {self.university}")
        print(f"Предмети: {', '.join(self.subjects) if self.subjects else 'Немає'}")
        print(f"Кількість оцінок: {len(self.grades)}")
        print(f"Середня оцінка: {self.get_average_grade()}")
    
    def is_excellent_student(self) -> bool:
        """Метод для перевірки, чи є студент відмінником"""
        avg_grade = self.get_average_grade()
        return avg_grade >= 4.5
    
    @classmethod
    def create_freshman(cls, name: str, age: int):
        """Метод класу для створення першокурсника"""
        student_id = f"FR_{name[:3].upper()}_{age}"
        return cls(name, age, student_id)
    
    @staticmethod
    def validate_age(age: int) -> bool:
        """Статичний метод для валідації віку"""
        return 16 <= age <= 65

# ============================= Демонстрація використання класу =============================

print("\n🎓 Демонстрація роботи з класом Student 🎓\n")

# Створення екземпляра класу
student1 = Student("Анна Петренко", 20, "STU001")

# Виклик методів екземпляра
print("1. Представлення студента:")
print(student1.introduce())

print("\n2. Додавання предметів:")
student1.add_subject("Математика")
student1.add_subject("Фізика")
student1.add_subject("Програмування")

print("\n3. Додавання оцінок:")
student1.add_grade("Математика", 5)
student1.add_grade("Математика", 4)
student1.add_grade("Фізика", 5)
student1.add_grade("Програмування", 5)

print("\n4. Отримання оцінок з математики:")
math_grades = student1.get_grades_by_subject("Математика")
print(f"Оцінки з математики: {math_grades}")

print("\n5. Перевірка, чи є студент відмінником:")
if student1.is_excellent_student():
    print("✅ Студент є відмінником!")
else:
    print("❌ Студент не є відмінником")

print("\n6. Повна інформація про студента:")
student1.display_info()

# Використання методу класу
print("\n7. Створення першокурсника за допомогою методу класу:")
freshman = Student.create_freshman("Іван Сидоренко", 18)
print(freshman.introduce())

# Використання статичного методу
print("\n8. Валідація віку:")
ages_to_check = [15, 20, 25, 70]
for age in ages_to_check:
    is_valid = Student.validate_age(age)
    print(f"Вік {age}: {'✅ валідний' if is_valid else '❌ невалідний'}")

# Створення ще одного студента для демонстрації
print("\n9. Створення другого студента:")
student2 = Student("Марія Коваленко", 19, "STU002")
student2.add_subject("Хімія")
student2.add_subject("Біологія")
student2.add_grade("Хімія", 3)
student2.add_grade("Біологія", 4)

print(f"\nПорівняння студентів:")
print(f"{student1.name}: середня оцінка {student1.get_average_grade()}")
print(f"{student2.name}: середня оцінка {student2.get_average_grade()}")

# Доступ до атрибуту класу
print(f"\nВсі студенти навчаються в: {Student.university}")

print("\n🎯 Демонстрацію завершено! 🎯")
