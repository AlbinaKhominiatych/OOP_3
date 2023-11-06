"""Завдання 1
Створіть клас "Користувач" з атрибутами "ім'я", "вік" та
"email". Застосуйте інкапсуляцію, щоб забезпечити, що ці
дані можна отримати лише через методи класу."""
#Рівень доступу Private (приватний)
from dataclasses import dataclass

@dataclass
class User:
    _name: str
    __age: int
    __email: str

    def get_name(self):
        return self._name

    def get_age(self):
        return self.__age

    def get_email(self):
        return self.__email

    def change_name(self, name): #set
        self._name = name

    def set_mail(self, mail):
        self.__email = mail

user1 = User("Ivan", 19, "example@email.com")
print(user1.get_name())
print(user1.get_age())
print(user1.get_email())
print(user1)
user1.change_name('Ivane')
print(user1)
user1.set_mail("new_mail@mail.com")
print(user1)