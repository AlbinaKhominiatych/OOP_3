#Рівень доступу Protected (внутрішній або захищений)
class MyClass:
    def __init__(self):
        self._protected_attribute = 10 #захищенний атрибут

    def _protected_method(self): #захищенний метод
        print("Це захищений метод")

class SubClass(MyClass):
    def access_protected(self):
        print(self._protected_attribute)
        self._protected_method()

a = MyClass()
obj = SubClass()
#print(dir(a))
print(a._protected_attribute) #моветон
obj.access_protected()
#Рівень доступу Private (приватний)
class MyClass:
    def __init__(self):
        self.__private_attribute = 20

    def __private_method(self):
        print("Це приватний метод")

obj = MyClass()
#print(obj.__private_attribute)
#obj.__private_method()
print(dir(obj))
print(obj._MyClass__private_attribute)
#приклад з банком
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Недостатньо коштів на рахунку")

    def get_balance(self):
        return self.__balance

# Використання:
account = BankAccount(1000)
account.deposit(500)
account.withdraw(200)
#print(account.__balance)
print(account.get_balance())  # Результат: 1300

# практика
"""Розробіть систему для організації подій та завдань.
Кожна подія має мати назву, дату та опис. Реалізуйте
методи для додавання нових подій, зміни дати та опису.
Використайте інкапсуляцію для захисту дати від неправильних змін."""

class CalendarApp:
    def __init__(self, name, date, description):
        self.__name = name
        self.__date = date
        self.__description = description

    def get_name(self):
        return self.__name

    def get_date(self):
        return self.__date

    def get_description(self):
        return self.__description

    def set_data(self, new_data):
        self.__date = new_data

    def set_description(self, new_description):
        self.__description = new_description
