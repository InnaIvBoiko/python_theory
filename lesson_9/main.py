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
